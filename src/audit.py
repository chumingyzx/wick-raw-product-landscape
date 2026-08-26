"""Independent automatic-differentiation audits of the closed-form spectra."""
from __future__ import annotations

import functools
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import torch
from scipy.linalg import null_space

from .theory import (
    equicorrelated_rank_one_boundary_spectrum,
    hermite_leakage_inertia,
    raw_ambient_specialization_curvature,
    raw_collapsed_scale,
    raw_rectangular_quadratic_form,
    raw_rectangular_spectrum,
    wick_restricted_specialization_loss_delta,
    wick_gamma_zero_loss_delta,
    wick_regular_psd_spectrum,
)

torch.set_default_dtype(torch.float64)


def permanent_torch(A: torch.Tensor) -> torch.Tensor:
    """Differentiable Ryser formula for a small square matrix."""
    n = int(A.shape[0])
    if tuple(A.shape) != (n, n):
        raise ValueError("A must be square")
    total = torch.zeros((), dtype=A.dtype, device=A.device)
    for mask in range(1, 1 << n):
        cols = [j for j in range(n) if mask & (1 << j)]
        row_sums = A[:, cols].sum(dim=1)
        parity = -1.0 if ((n - len(cols)) % 2) else 1.0
        total = total + parity * torch.prod(row_sums)
    return total


def wick_loss_torch(W: torch.Tensor, U: torch.Tensor) -> torch.Tensor:
    return 0.5 * (
        permanent_torch(W.T @ W)
        - 2.0 * permanent_torch(W.T @ U)
        + permanent_torch(U.T @ U)
    )


def _pairing_sum(C: torch.Tensor) -> torch.Tensor:
    """Sum over perfect matchings of a small covariance matrix."""
    n = int(C.shape[0])
    if n % 2:
        raise ValueError("pairing dimension must be even")

    @functools.lru_cache(maxsize=None)
    def rec(mask: int) -> torch.Tensor:
        if mask == 0:
            return torch.ones((), dtype=C.dtype, device=C.device)
        ibit = mask & -mask
        i = ibit.bit_length() - 1
        rem = mask ^ ibit
        out = torch.zeros((), dtype=C.dtype, device=C.device)
        jmask = rem
        while jmask:
            jbit = jmask & -jmask
            j = jbit.bit_length() - 1
            out = out + C[i, j] * rec(rem ^ jbit)
            jmask ^= jbit
        return out

    return rec((1 << n) - 1)


def raw_loss_torch(W: torch.Tensor, U: torch.Tensor) -> torch.Tensor:
    """Exact raw Gaussian population loss for an orthonormal teacher frame."""
    L = int(W.shape[1])
    A = W.T @ W
    C = A.repeat(2, 2)
    student_norm = _pairing_sum(C)
    cross = permanent_torch(W.T @ U)
    teacher_norm = torch.ones((), dtype=W.dtype, device=W.device)
    return 0.5 * (student_norm - 2.0 * cross + teacher_norm)


def _orthonormal_frame(d: int, L: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.normal(size=(d, L)))
    return Q[:, :L]


def _basis_one_perp(L: int) -> np.ndarray:
    e = np.ones((1, L), dtype=float) / math.sqrt(L)
    return null_space(e)


def _rank_deficient_regular_teacher(
    L: int,
    d: int,
    rank: int,
    gamma: float,
    seed: int,
) -> tuple[np.ndarray, np.ndarray]:
    if not (1 <= rank <= min(L, d)):
        raise ValueError("invalid rank")
    rng = np.random.default_rng(seed)
    e = np.ones(L) / math.sqrt(L)
    Q = _basis_one_perp(L)
    if L > 2:
        R, _ = np.linalg.qr(rng.normal(size=(L - 1, L - 1)))
        Q = Q @ R
    mus = np.zeros(L - 1)
    if rank > 1:
        mus[: rank - 1] = np.linspace(0.35, 1.75, rank - 1)
    T = gamma * np.outer(e, e) + Q @ np.diag(mus) @ Q.T
    vals, vecs = np.linalg.eigh(T)
    keep = vals > 1e-12
    vals_pos = vals[keep]
    vecs_pos = vecs[:, keep]
    P = _orthonormal_frame(d, rank, seed + 7919)
    U = P @ np.diag(np.sqrt(vals_pos)) @ vecs_pos.T
    return U, mus[mus > 1e-12]


def _hessian_matrix(loss_fn, W0: np.ndarray) -> tuple[np.ndarray, float]:
    W = torch.tensor(W0, requires_grad=True)
    loss = loss_fn(W)
    grad = torch.autograd.grad(loss, W, create_graph=False)[0]
    H4 = torch.autograd.functional.hessian(loss_fn, W)
    H = H4.detach().numpy().reshape(W0.size, W0.size)
    return H, float(torch.linalg.norm(grad).detach().cpu())


def audit_wick_rectangular_rank_deficient() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    cases: set[tuple[int, int, int]] = set()
    for L in range(2, 6):
        ranks = sorted({1, max(1, (L + 1) // 2), L})
        for d in (L, L + 2):
            for rank in ranks:
                cases.add((L, d, rank))
    cases.update({
        (4, 2, 2), (5, 2, 2), (5, 3, 3),
        (6, 3, 2), (7, 4, 4), (8, 3, 3),
    })
    for L, d, rank in sorted(cases):
        U, mus = _rank_deficient_regular_teacher(
            L=L, d=d, rank=rank, gamma=1.3,
            seed=100000 * L + 1000 * d + rank,
        )
        W0 = U @ np.ones((L, L)) / L
        Ut = torch.tensor(U)
        H, grad_norm = _hessian_matrix(lambda W: wick_loss_torch(W, Ut), W0)
        numerical = np.linalg.eigvalsh(H)
        predicted_spec = wick_regular_psd_spectrum(L, d, 1.3, mus)
        predicted = predicted_spec.sorted()
        err = float(np.max(np.abs(numerical - predicted)))
        n_num = (
            int(np.sum(numerical < -1e-8)),
            int(np.sum(np.abs(numerical) <= 1e-8)),
            int(np.sum(numerical > 1e-8)),
        )
        rows.append({
            "L": L, "d": d, "rank": rank,
            "gradient_norm": grad_norm,
            "max_eigenvalue_error": err,
            "numerical_inertia": list(n_num),
            "predicted_inertia": list(predicted_spec.inertia(1e-8)),
            "d_lt_L": d < L,
        })
    return {
        "cells": len(rows),
        "d_lt_L_cells": sum(r["d_lt_L"] for r in rows),
        "max_gradient_norm": max(r["gradient_norm"] for r in rows),
        "max_eigenvalue_error": max(r["max_eigenvalue_error"] for r in rows),
        "max_d_lt_L_eigenvalue_error": max(r["max_eigenvalue_error"] for r in rows if r["d_lt_L"]),
        "inertia_mismatches": sum(r["numerical_inertia"] != r["predicted_inertia"] for r in rows),
        "rows": rows,
    }


def audit_rank_one_boundary() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for L in range(2, 6):
        for d in (L, L + 2):
            rng = np.random.default_rng(77 * L + d)
            u = rng.normal(size=d)
            u /= np.linalg.norm(u)
            U = np.outer(u, np.ones(L))
            W0 = U.copy()
            Ut = torch.tensor(U)
            H, grad_norm = _hessian_matrix(lambda W: wick_loss_torch(W, Ut), W0)
            numerical = np.linalg.eigvalsh(H)
            predicted = equicorrelated_rank_one_boundary_spectrum(L, d).sorted()
            rows.append({
                "L": L, "d": d, "gradient_norm": grad_norm,
                "max_eigenvalue_error": float(np.max(np.abs(numerical - predicted))),
            })
    return {
        "cells": len(rows),
        "max_gradient_norm": max(r["gradient_norm"] for r in rows),
        "max_eigenvalue_error": max(r["max_eigenvalue_error"] for r in rows),
        "rows": rows,
    }


def audit_gamma_zero_boundary() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    max_identity_error = 0.0
    max_hessian_norm = 0.0
    for L in range(3, 6):
        d = L + 2
        rng = np.random.default_rng(191 * L)
        Q = _basis_one_perp(L)
        U = rng.normal(size=(d, L - 1)) @ Q.T
        Ut = torch.tensor(U)
        W0 = np.zeros_like(U)
        Hmat, grad_norm = _hessian_matrix(lambda W: wick_loss_torch(W, Ut), W0)
        max_hessian_norm = max(max_hessian_norm, float(np.linalg.norm(Hmat, ord=2)))
        base = float(wick_loss_torch(torch.tensor(W0), Ut))
        for trial in range(5):
            H = rng.normal(size=U.shape)
            for t in (-0.35, -0.1, 0.1, 0.35):
                actual = float(wick_loss_torch(torch.tensor(t * H), Ut)) - base
                predicted = wick_gamma_zero_loss_delta(H, U, t)
                err = abs(actual - predicted)
                max_identity_error = max(max_identity_error, err)
                rows.append({
                    "L": L, "trial": trial, "t": t,
                    "gradient_norm_at_zero": grad_norm,
                    "hessian_operator_norm_at_zero": float(np.linalg.norm(Hmat, ord=2)),
                    "identity_error": err,
                })
    return {
        "cells": len(rows),
        "max_identity_error": max_identity_error,
        "max_hessian_operator_norm": max_hessian_norm,
        "rows": rows,
    }


def audit_raw_rectangular() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    qrows: list[dict[str, Any]] = []
    for L in range(2, 5):
        for d in (L, L + 1, L + 2):
            U = _orthonormal_frame(d, L, seed=30000 + 100 * L + d)
            m = U @ np.ones(L)
            W0 = raw_collapsed_scale(L) * np.outer(m, np.ones(L))
            Ut = torch.tensor(U)
            Hmat, grad_norm = _hessian_matrix(lambda W: raw_loss_torch(W, Ut), W0)
            numerical = np.linalg.eigvalsh(Hmat)
            predicted_spec = raw_rectangular_spectrum(L, d)
            predicted = predicted_spec.sorted()
            rows.append({
                "L": L, "d": d, "gradient_norm": grad_norm,
                "max_eigenvalue_error": float(np.max(np.abs(numerical - predicted))),
                "numerical_inertia": [
                    int(np.sum(numerical < -1e-8)),
                    int(np.sum(np.abs(numerical) <= 1e-8)),
                    int(np.sum(numerical > 1e-8)),
                ],
                "predicted_inertia": list(predicted_spec.inertia(1e-8)),
            })
            rng = np.random.default_rng(40000 + 100 * L + d)
            for trial in range(8):
                direction = rng.normal(size=(d, L))
                v = direction.reshape(-1)
                qrows.append({
                    "L": L, "d": d, "trial": trial,
                    "quadratic_form_error": abs(float(v @ Hmat @ v) - raw_rectangular_quadratic_form(direction, U)),
                })
    return {
        "spectrum_cells": len(rows),
        "quadratic_form_cells": len(qrows),
        "max_gradient_norm": max(r["gradient_norm"] for r in rows),
        "max_eigenvalue_error": max(r["max_eigenvalue_error"] for r in rows),
        "inertia_mismatches": sum(r["numerical_inertia"] != r["predicted_inertia"] for r in rows),
        "max_quadratic_form_error": max(r["quadratic_form_error"] for r in qrows),
        "rows": rows,
        "quadratic_form_rows": qrows,
    }


def audit_raw_even_negative_branch() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for L in (2, 4, 6):
        d = L
        U = np.eye(L)
        m = U @ np.ones(L)
        c = raw_collapsed_scale(L)
        Ut = torch.tensor(U)
        predicted = raw_rectangular_spectrum(L, d).sorted()
        for sign in (1.0, -1.0):
            W0 = sign * c * np.outer(m, np.ones(L))
            Hmat, grad_norm = _hessian_matrix(lambda W: raw_loss_torch(W, Ut), W0)
            numerical = np.linalg.eigvalsh(Hmat)
            rows.append({
                "L": L, "d": d, "sign": int(sign),
                "gradient_norm": grad_norm,
                "max_eigenvalue_error": float(np.max(np.abs(numerical - predicted))),
                "numerical_inertia": [
                    int(np.sum(numerical < -1e-8)),
                    int(np.sum(np.abs(numerical) <= 1e-8)),
                    int(np.sum(numerical > 1e-8)),
                ],
            })
    return {
        "cells": len(rows),
        "max_gradient_norm": max(r["gradient_norm"] for r in rows),
        "max_eigenvalue_error": max(r["max_eigenvalue_error"] for r in rows),
        "rows": rows,
    }


def audit_embedded_quartic_path() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for L in range(2, 8):
        d = L + 2
        U = _orthonormal_frame(d, L, seed=80000 + L)
        Ut = torch.tensor(U)
        J = np.ones((L, L))
        u = np.zeros(L); v = np.zeros(L)
        u[0], u[1] = 1.0, -1.0
        v[0], v[1] = 1.0, -1.0
        K = 0.5 * np.outer(u, v)
        W0 = U @ (J / L)
        base = float(wick_loss_torch(torch.tensor(W0), Ut))
        max_err = 0.0
        for t in (-0.8, -0.35, -0.1, 0.1, 0.35, 0.8):
            Wt = U @ (J / L + t * K)
            actual = float(wick_loss_torch(torch.tensor(Wt), Ut)) - base
            max_err = max(max_err, abs(actual - wick_restricted_specialization_loss_delta(L, t)))
        rows.append({"L": L, "d": d, "max_abs_error": max_err})
    return {"cells": len(rows), "max_abs_error": max(r["max_abs_error"] for r in rows), "rows": rows}


def audit_ambient_hermite_leakage_direction() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for L in range(2, 7):
        d = L + 2
        U = _orthonormal_frame(d, L, seed=90000 + L)
        N = null_space(U.T)
        n = N[:, 0]
        q = np.zeros(L)
        q[0], q[1] = 1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0)
        H = np.outer(n, q)
        observed = raw_rectangular_quadratic_form(H, U)
        predicted = raw_ambient_specialization_curvature(L)
        rows.append({
            "L": L, "d": d, "observed": observed, "predicted": predicted,
            "abs_error": abs(observed - predicted),
        })
    return {"cells": len(rows), "max_abs_error": max(r["abs_error"] for r in rows), "rows": rows}


def audit_hermite_leakage_counts() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    mismatches = 0
    for L in range(2, 13):
        for d in range(L, 4 * L + 1):
            predicted = hermite_leakage_inertia(L, d)
            wick = wick_regular_psd_spectrum(L, d, 1.0, [1.0] * (L - 1)).inertia()
            raw = raw_rectangular_spectrum(L, d).inertia()
            observed = {
                "wick_index": wick[0], "wick_nullity": wick[1], "wick_positive": wick[2],
                "raw_index": raw[0], "raw_nullity": raw[1], "raw_positive": raw[2],
                "index_inflation": raw[0] - wick[0],
            }
            mismatch = observed != predicted
            mismatches += int(mismatch)
            rows.append({"L": L, "d": d, **predicted, "mismatch": mismatch})
    return {"cells": len(rows), "mismatches": mismatches, "rows": rows}


def run_all(output: Path) -> dict[str, Any]:
    result = {
        "wick_rectangular_rank_deficient": audit_wick_rectangular_rank_deficient(),
        "wick_rank_one_boundary": audit_rank_one_boundary(),
        "wick_gamma_zero_boundary": audit_gamma_zero_boundary(),
        "raw_rectangular": audit_raw_rectangular(),
        "raw_even_negative_branch": audit_raw_even_negative_branch(),
        "embedded_quartic_path": audit_embedded_quartic_path(),
        "ambient_hermite_leakage_direction": audit_ambient_hermite_leakage_direction(),
        "hermite_leakage_counts": audit_hermite_leakage_counts(),
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    result = run_all(root / "results" / "audit_results.json")
    summary = {}
    for key, value in result.items():
        summary[key] = {k: v for k, v in value.items() if not k.endswith("rows") and k != "rows"}
    print(json.dumps(summary, indent=2))
