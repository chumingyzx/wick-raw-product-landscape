"""Closed-form formulas for Wick and raw Gaussian product landscapes.

The module implements the theorem statements consolidated in the accompanying
technical note.  No learned-model code is included.
"""
from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class Spectrum:
    """A labeled finite Hessian spectrum."""

    eigenvalues: np.ndarray
    labels: tuple[str, ...]

    def sorted(self) -> np.ndarray:
        return np.sort(np.asarray(self.eigenvalues, dtype=float))

    @property
    def dimension(self) -> int:
        return int(self.eigenvalues.size)

    def inertia(self, tol: float = 1e-10) -> tuple[int, int, int]:
        vals = np.asarray(self.eigenvalues, dtype=float)
        neg = int(np.sum(vals < -tol))
        zero = int(np.sum(np.abs(vals) <= tol))
        pos = int(np.sum(vals > tol))
        return neg, zero, pos


def permanent_numpy(A: np.ndarray) -> float:
    """Permanent of a small square matrix by direct permutation enumeration."""
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    if A.shape != (n, n):
        raise ValueError("A must be square")
    total = 0.0
    for p in itertools.permutations(range(n)):
        prod = 1.0
        for i, j in enumerate(p):
            prod *= float(A[i, j])
        total += prod
    return total


def wick_orthogonal_scale(L: int) -> float:
    """a_L=(L-2)!/L^(L-2), the orthogonal-teacher Wick scale."""
    if L < 2:
        raise ValueError("L must be at least 2")
    return math.factorial(L - 2) / (L ** (L - 2))


def equicorrelated_permanent(L: int, rho: float) -> float:
    """perm((1-rho)I + rho J), evaluated by its exact finite sum."""
    if L < 1:
        raise ValueError("L must be positive")
    return sum(
        math.comb(L, k)
        * ((1.0 - rho) ** (L - k))
        * (rho**k)
        * math.factorial(k)
        for k in range(L + 1)
    )


def _log_truncated_exponential(L: int, x: float) -> float:
    """Return log(sum_{j=0}^L x^j/j!) stably for x>=0."""
    if L < 0:
        raise ValueError("L must be nonnegative")
    if x < 0.0:
        raise ValueError("x must be nonnegative")
    if x == 0.0:
        return 0.0
    terms = np.asarray(
        [j * math.log(x) - math.lgamma(j + 1) for j in range(L + 1)],
        dtype=float,
    )
    peak = float(np.max(terms))
    return peak + math.log(float(np.exp(terms - peak).sum()))


def equicorrelated_normalized_specialization_curvature(L: int, rho: float) -> float:
    """Exact |lambda_spec(T_rho)|/perm(T_rho) for 0<rho<1.

    With x=(1-rho)/rho and E_L(x)=sum_{j=0}^L x^j/j!,

      C_L(rho)=x(x+1)/(L(L-1)) * (1+x/L)^(L-2) / E_L(x).

    The logarithmic implementation remains stable when x or L is moderately
    large and does not invoke an asymptotic approximation.
    """
    if L < 2:
        raise ValueError("L must be at least 2")
    if not (0.0 < rho < 1.0):
        raise ValueError("rho must lie in (0,1)")
    x = (1.0 - rho) / rho
    log_value = (
        math.log(x)
        + math.log1p(x)
        - math.log(L)
        - math.log(L - 1.0)
        + (L - 2) * math.log1p(x / L)
        - _log_truncated_exponential(L, x)
    )
    return math.exp(log_value)


def equicorrelated_normalized_specialization_curvature_direct(L: int, rho: float) -> float:
    """Direct permanent-based evaluation of the same normalized curvature."""
    if L < 2:
        raise ValueError("L must be at least 2")
    if not (0.0 < rho < 1.0):
        raise ValueError("rho must lie in (0,1)")
    gamma = 1.0 + (L - 1) * rho
    lam = (1.0 - rho) * math.factorial(L - 2) * ((gamma / L) ** (L - 2))
    return lam / equicorrelated_permanent(L, rho)


def equicorrelated_crossover_limit(L: int, t: float) -> float:
    """Leading C_L approximation when rho_L*sqrt(L)->t>0."""
    if L < 2 or t <= 0.0:
        raise ValueError("require L>=2 and t>0")
    return math.exp(-1.0 / (2.0 * t * t)) / (t * t * L)


def wick_regular_psd_spectrum(
    L: int,
    d: int,
    gamma: float,
    positive_mus: Iterable[float],
) -> Spectrum:
    """Rectangular/rank-deficient Wick spectrum at W*=U J/L.

    Assumptions
    -----------
    U is d-by-L, T=U^T U is positive semidefinite, T 1=gamma 1 with
    gamma>0.  ``positive_mus`` contains the strictly positive eigenvalues of
    T on 1^perp.  If there are r-1 such values, rank(T)=r.
    """
    if L < 2:
        raise ValueError("L must be at least 2")
    if gamma <= 0:
        raise ValueError("gamma must be positive")
    mus = tuple(float(mu) for mu in positive_mus)
    if any(mu <= 0 for mu in mus):
        raise ValueError("positive_mus must be strictly positive")
    if len(mus) > L - 1:
        raise ValueError("at most L-1 non-radial eigenvalues are allowed")
    r = 1 + len(mus)
    if d < r:
        raise ValueError("ambient dimension d must be at least rank r")

    b = math.factorial(L - 2) * ((gamma / L) ** (L - 2))
    vals: list[float] = []
    labels: list[str] = []

    vals.append(L * (L - 1) * gamma * b)
    labels.append("radial")

    for j in range(L - 1):
        vals.append(0.0)
        labels.append(f"gauge[{j}]")

    for i, mu in enumerate(mus):
        vals.append((L - 1) * (gamma + mu) * b)
        labels.append(f"teacher_collective[{i}]")

    for i, mu in enumerate(mus):
        for j in range(L - 1):
            vals.append(-mu * b)
            labels.append(f"teacher_specialization[{i},{j}]")

    for a in range(d - r):
        vals.append((L - 1) * gamma * b)
        labels.append(f"ambient_collective[{a}]")

    for a in range(d - r):
        for j in range(L - 1):
            vals.append(0.0)
            labels.append(f"ambient_null[{a},{j}]")

    spec = Spectrum(np.asarray(vals, dtype=float), tuple(labels))
    if spec.dimension != d * L:
        raise AssertionError("internal multiplicity error")
    return spec


def wick_orthonormal_rectangular_spectrum(L: int, d: int) -> Spectrum:
    """Wick spectrum for an orthonormal L-frame in R^d."""
    if d < L:
        raise ValueError("orthonormal teacher requires d>=L")
    return wick_regular_psd_spectrum(L, d, gamma=1.0, positive_mus=[1.0] * (L - 1))


def equicorrelated_wick_spectrum(L: int, d: int, rho: float, normalize: bool = False) -> Spectrum:
    """Full-rank equicorrelated Wick spectrum for -1/(L-1)<rho<1."""
    lower = -1.0 / (L - 1)
    if not (lower < rho < 1.0):
        raise ValueError(f"rho must lie in ({lower},1)")
    gamma = 1.0 + (L - 1) * rho
    mu = 1.0 - rho
    spec = wick_regular_psd_spectrum(L, d, gamma, [mu] * (L - 1))
    if not normalize:
        return spec
    denom = equicorrelated_permanent(L, rho)
    return Spectrum(spec.eigenvalues / denom, spec.labels)


def equicorrelated_rank_one_boundary_spectrum(L: int, d: int) -> Spectrum:
    """rho=1 boundary: rank-one teacher, where the collapsed point is exact."""
    return wick_regular_psd_spectrum(L, d, gamma=float(L), positive_mus=[])


def wick_gamma_zero_loss_delta(H: np.ndarray, U: np.ndarray, t: float) -> float:
    """Exact loss change at W=0 when U 1=0.

    For the Wick loss, homogeneity gives
      Delta L = -t^L perm(H^T U) + 1/2 t^(2L) perm(H^T H).
    """
    H = np.asarray(H, dtype=float)
    U = np.asarray(U, dtype=float)
    if H.shape != U.shape:
        raise ValueError("H and U must have the same shape")
    L = H.shape[1]
    return -(t**L) * permanent_numpy(H.T @ U) + 0.5 * (t ** (2 * L)) * permanent_numpy(H.T @ H)


def raw_collapsed_scale(L: int) -> float:
    """Positive real root c_L for W*=c_L (U1)1^T in the raw model."""
    if L < 2:
        raise ValueError("L must be at least 2")
    log_c = (
        L * math.log(2.0)
        + 2.0 * math.lgamma(L + 1)
        - L * math.log(L)
        - math.lgamma(2 * L + 1)
    ) / L
    return math.exp(log_c)


def raw_collapsed_scale_signed(L: int, sign: int = 1) -> float:
    """Return a real collapsed branch.

    The negative branch exists only for even ``L``.  It represents the same
    product predictor and has the same Hessian spectrum as the positive branch.
    """
    if sign not in (-1, 1):
        raise ValueError("sign must be +1 or -1")
    if sign < 0 and L % 2:
        raise ValueError("negative real branch exists only for even L")
    return float(sign) * raw_collapsed_scale(L)


def raw_scale(L: int) -> float:
    """k_L=(L-2)! c_L^(L-2)."""
    return math.factorial(L - 2) * (raw_collapsed_scale(L) ** (L - 2))


def raw_ambient_specialization_curvature(L: int) -> float:
    """Unit-direction curvature on col(U)^perp tensor 1^perp."""
    if L < 2:
        raise ValueError("L must be at least 2")
    return -((L - 1.0) / (2.0 * L - 1.0)) * raw_scale(L)


def normalized_two_by_two_contrast(
    L: int,
    i: int = 0,
    j: int = 1,
    p: int = 0,
    q: int = 1,
) -> np.ndarray:
    """Return K=(e_i-e_j)(e_p-e_q)^T/2 with unit Frobenius norm."""
    if L < 2:
        raise ValueError("L must be at least 2")
    indices = (i, j, p, q)
    if any(idx < 0 or idx >= L for idx in indices):
        raise ValueError("indices must lie in range(L)")
    if i == j or p == q:
        raise ValueError("contrast indices must be distinct")
    u = np.zeros(L, dtype=float)
    v = np.zeros(L, dtype=float)
    u[i], u[j] = 1.0, -1.0
    v[p], v[q] = 1.0, -1.0
    return 0.5 * np.outer(u, v)


def raw_rectangular_spectrum(L: int, d: int) -> Spectrum:
    """Raw Gaussian spectrum for an orthonormal L-frame in R^d."""
    if L < 2:
        raise ValueError("L must be at least 2")
    if d < L:
        raise ValueError("orthonormal teacher requires d>=L")
    k = raw_scale(L)
    vals: list[float] = []
    labels: list[str] = []

    vals.append(L * (L - 1) * k)
    labels.append("radial")

    for j in range(L - 1):
        vals.append(0.0)
        labels.append(f"gauge[{j}]")

    for i in range(L - 1):
        vals.append(2.0 * (L - 1) * k)
        labels.append(f"teacher_collective[{i}]")

    lam_teacher_spec = -((3.0 * L - 2.0) / (2.0 * L - 1.0)) * k
    for i in range(L - 1):
        for j in range(L - 1):
            vals.append(lam_teacher_spec)
            labels.append(f"teacher_specialization[{i},{j}]")

    for a in range(d - L):
        vals.append((L - 1) * k)
        labels.append(f"ambient_collective[{a}]")

    lam_ambient_spec = -((L - 1.0) / (2.0 * L - 1.0)) * k
    for a in range(d - L):
        for j in range(L - 1):
            vals.append(lam_ambient_spec)
            labels.append(f"ambient_specialization[{a},{j}]")

    spec = Spectrum(np.asarray(vals, dtype=float), tuple(labels))
    if spec.dimension != d * L:
        raise AssertionError("internal multiplicity error")
    return spec


def raw_rectangular_quadratic_form(H: np.ndarray, U: np.ndarray) -> float:
    """Closed raw-Gaussian Hessian quadratic form at the collapsed point.

    U must have orthonormal columns.  The returned value is D^2 R(W*)[H,H].
    """
    H = np.asarray(H, dtype=float)
    U = np.asarray(U, dtype=float)
    if H.shape != U.shape:
        raise ValueError("H and U must have the same d-by-L shape")
    d, L = U.shape
    if L < 2 or d < L:
        raise ValueError("require d>=L>=2")
    if not np.allclose(U.T @ U, np.eye(L), atol=1e-9, rtol=1e-9):
        raise ValueError("U must have orthonormal columns")

    P = U @ U.T
    one = np.ones(L)
    m = U @ one
    rvec = H @ one
    qvec = H.T @ m
    s = float(m @ rvec)
    coeff_s = 4.0 * ((L - 1) ** 2) / (L * (2 * L - 1)) - 1.0
    value = (
        coeff_s * s * s
        + (2.0 * (L - 1) / (2 * L - 1)) * float(rvec @ rvec)
        + float((P @ rvec) @ (P @ rvec))
        + ((3.0 * L - 2.0) / (L * (2 * L - 1))) * float(qvec @ qvec)
        - ((L - 1.0) / (2.0 * L - 1.0)) * float(np.sum(H * H))
        - float(np.sum((P @ H) ** 2))
    )
    return raw_scale(L) * value


def hermite_leakage_inertia(L: int, d: int) -> dict[str, int]:
    """Closed inertia counts for rectangular Wick and raw metrics."""
    if d < L or L < 2:
        raise ValueError("require d>=L>=2")
    return {
        "wick_index": (L - 1) ** 2,
        "wick_nullity": (d - L + 1) * (L - 1),
        "wick_positive": d,
        "raw_index": (d - 1) * (L - 1),
        "raw_nullity": L - 1,
        "raw_positive": d,
        "index_inflation": (d - L) * (L - 1),
    }


def wick_restricted_specialization_loss_delta(L: int, t: float) -> float:
    """Exact orthogonal-Wick loss change along a normalized 2-by-2 contrast."""
    a = wick_orthogonal_scale(L)
    return -0.5 * a * t * t + 0.25 * a * (t**4)


def projected_escape_time(L: int, eps: float, radius: float) -> float:
    """Exact time for dt/dtau=a_L t(1-t^2), 0<eps<radius<1."""
    if not (0.0 < eps < radius < 1.0):
        raise ValueError("require 0<eps<radius<1")
    a = wick_orthogonal_scale(L)
    primitive = lambda x: math.log(x) - 0.5 * math.log(1.0 - x * x)
    return (primitive(radius) - primitive(eps)) / a
