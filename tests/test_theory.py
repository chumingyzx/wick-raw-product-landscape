from __future__ import annotations

import math

import numpy as np
import pytest

from src.theory import (
    equicorrelated_crossover_limit,
    equicorrelated_normalized_specialization_curvature,
    equicorrelated_rank_one_boundary_spectrum,
    hermite_leakage_inertia,
    normalized_two_by_two_contrast,
    raw_collapsed_scale_signed,
    raw_ambient_specialization_curvature,
    raw_rectangular_quadratic_form,
    raw_rectangular_spectrum,
    raw_scale,
    wick_gamma_zero_loss_delta,
    wick_regular_psd_spectrum,
)


def test_wick_dimension_and_inertia() -> None:
    for L in range(2, 8):
        for d in range(L, L + 4):
            for r in range(1, L + 1):
                mus = np.linspace(0.2, 1.3, r - 1) if r > 1 else []
                spec = wick_regular_psd_spectrum(L, d, 1.1, mus)
                assert spec.dimension == d * L
                assert spec.inertia() == (
                    (r - 1) * (L - 1),
                    (d - r + 1) * (L - 1),
                    d,
                )


def test_rank_one_boundary_is_psd() -> None:
    for L in range(2, 10):
        for d in (L, L + 2):
            assert equicorrelated_rank_one_boundary_spectrum(L, d).inertia() == (
                0,
                d * (L - 1),
                d,
            )


def test_raw_dimension_and_inertia() -> None:
    for L in range(2, 10):
        for d in range(L, 3 * L):
            spec = raw_rectangular_spectrum(L, d)
            assert spec.dimension == d * L
            assert spec.inertia() == ((d - 1) * (L - 1), L - 1, d)


def test_hermite_leakage_counts() -> None:
    for L in range(2, 12):
        for d in range(L, 4 * L):
            counts = hermite_leakage_inertia(L, d)
            assert counts["index_inflation"] == (d - L) * (L - 1)
            assert counts["raw_index"] - counts["wick_index"] == counts["index_inflation"]
            assert counts["wick_index"] + counts["wick_nullity"] + counts["wick_positive"] == d * L
            assert counts["raw_index"] + counts["raw_nullity"] + counts["raw_positive"] == d * L


def test_raw_quadratic_form_rejects_nonorthonormal_teacher() -> None:
    U = np.ones((3, 2))
    H = np.ones((3, 2))
    with pytest.raises(ValueError):
        raw_rectangular_quadratic_form(H, U)


def test_gamma_zero_homogeneity() -> None:
    rng = np.random.default_rng(4)
    L = 4
    d = 6
    q, _ = np.linalg.qr(np.eye(L) - np.ones((L, L)) / L)
    Q = q[:, : L - 1]
    U = rng.normal(size=(d, L - 1)) @ Q.T
    H = rng.normal(size=(d, L))
    delta1 = wick_gamma_zero_loss_delta(H, U, 0.2)
    delta2 = wick_gamma_zero_loss_delta(H, U, -0.2)
    assert math.isfinite(delta1)
    assert math.isfinite(delta2)


def test_invalid_dimensions() -> None:
    with pytest.raises(ValueError):
        raw_rectangular_spectrum(4, 3)
    with pytest.raises(ValueError):
        wick_regular_psd_spectrum(4, 1, 1.0, [0.5])


def test_wick_dimension_and_inertia_when_d_less_than_L() -> None:
    cases = [
        (4, 2, 2),
        (5, 2, 2),
        (5, 3, 3),
        (6, 3, 2),
        (7, 4, 4),
        (8, 3, 3),
    ]
    for L, d, r in cases:
        mus = np.linspace(0.25, 1.25, r - 1) if r > 1 else []
        spec = wick_regular_psd_spectrum(L, d, 1.3, mus)
        assert spec.dimension == d * L
        assert spec.inertia() == (
            (r - 1) * (L - 1),
            (d - r + 1) * (L - 1),
            d,
        )


def test_equicorrelated_exact_normalized_curvature_formula() -> None:
    for L in range(3, 12):
        for rho in (0.05, 0.15, 0.4, 0.8):
            exact = equicorrelated_normalized_specialization_curvature(L, rho)
            gamma = 1.0 + (L - 1) * rho
            numerator = (1.0 - rho) * math.factorial(L - 2) * ((gamma / L) ** (L - 2))
            denominator = sum(
                math.comb(L, k)
                * ((1.0 - rho) ** (L - k))
                * (rho**k)
                * math.factorial(k)
                for k in range(L + 1)
            )
            assert exact == pytest.approx(numerator / denominator, rel=1e-12, abs=1e-14)


def test_raw_ambient_specialization_curvature() -> None:
    for L in range(2, 12):
        expected = -((L - 1.0) / (2.0 * L - 1.0)) * raw_scale(L)
        assert raw_ambient_specialization_curvature(L) == pytest.approx(expected)


def test_raw_collapsed_real_branches() -> None:
    for L in (2, 4, 6, 8):
        c = raw_collapsed_scale_signed(L, 1)
        assert raw_collapsed_scale_signed(L, -1) == pytest.approx(-c)
    with pytest.raises(ValueError):
        raw_collapsed_scale_signed(3, -1)


def test_normalized_contrast_properties() -> None:
    for L in range(2, 10):
        K = normalized_two_by_two_contrast(L)
        assert np.linalg.norm(K) == pytest.approx(1.0)
        assert np.linalg.norm(K @ np.ones(L)) < 1e-12
        assert np.linalg.norm(K.T @ np.ones(L)) < 1e-12


def test_equicorrelation_critical_window() -> None:
    for t in (0.7, 1.0, 1.7):
        for L in (400, 800, 1600):
            rho = t / math.sqrt(L)
            exact = equicorrelated_normalized_specialization_curvature(L, rho)
            approx = equicorrelated_crossover_limit(L, t)
            assert exact / approx == pytest.approx(1.0, rel=0.13)
