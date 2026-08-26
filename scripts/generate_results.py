from __future__ import annotations

import csv
import json
from pathlib import Path

from src.theory import (
    equicorrelated_crossover_limit,
    equicorrelated_normalized_specialization_curvature,
    equicorrelated_wick_spectrum,
    hermite_leakage_inertia,
    raw_rectangular_spectrum,
    wick_regular_psd_spectrum,
)


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results = root / "results"

    inertia_rows = []
    for L in range(2, 21):
        for d in range(L, 4 * L + 1):
            inertia_rows.append({"L": L, "d": d, **hermite_leakage_inertia(L, d)})
    write_csv(results / "rectangular_inertia.csv", inertia_rows)

    rank_rows = []
    L, d, gamma = 12, 18, 1.0
    for rank in range(1, L + 1):
        mus = [1.0] * (rank - 1)
        neg, zero, pos = wick_regular_psd_spectrum(L, d, gamma, mus).inertia()
        rank_rows.append({"L": L, "d": d, "rank": rank, "index": neg, "nullity": zero, "positive": pos})
    write_csv(results / "wick_rank_sweep.csv", rank_rows)

    boundary_rows = []
    rho_values = [0.0, 0.25, 0.5, 0.75, 0.9, 0.95, 0.98, 0.99, 0.995, 0.999, 0.9999]
    for L in (4, 8, 16):
        for rho in rho_values:
            spec = equicorrelated_wick_spectrum(L, L, rho, normalize=False)
            spec_norm = equicorrelated_wick_spectrum(L, L, rho, normalize=True)
            negative = [abs(v) for v in spec.eigenvalues if v < -1e-14]
            negative_norm = [abs(v) for v in spec_norm.eigenvalues if v < -1e-14]
            boundary_rows.append({
                "L": L,
                "rho": rho,
                "one_minus_rho": 1.0 - rho,
                "specialization_curvature": max(negative) if negative else 0.0,
                "normalized_specialization_curvature": max(negative_norm) if negative_norm else 0.0,
                "index": spec.inertia()[0],
                "nullity": spec.inertia()[1],
            })
    write_csv(results / "equicorrelation_boundary.csv", boundary_rows)

    crossover_rows = []
    for t in (0.5, 0.75, 1.0, 1.5, 2.0):
        for L in (50, 100, 200, 800, 1600):
            rho = t / (L**0.5)
            exact = equicorrelated_normalized_specialization_curvature(L, rho)
            approximation = equicorrelated_crossover_limit(L, t)
            crossover_rows.append({
                "L": L,
                "t": t,
                "rho": rho,
                "rho_sqrt_L": rho * (L**0.5),
                "exact": exact,
                "critical_window_asymptotic": approximation,
                "ratio": exact / approximation,
            })
    write_csv(results / "equicorrelation_critical_window.csv", crossover_rows)

    sector_rows = []
    L, d = 6, 10
    for metric, spectrum in (
        ("wick", wick_regular_psd_spectrum(L, d, 1.0, [1.0] * (L - 1))),
        ("raw", raw_rectangular_spectrum(L, d)),
    ):
        groups: dict[str, list[float]] = {}
        for label, value in zip(spectrum.labels, spectrum.eigenvalues):
            sector = label.split("[")[0]
            groups.setdefault(sector, []).append(float(value))
        for sector, values in groups.items():
            sector_rows.append({
                "metric": metric,
                "L": L,
                "d": d,
                "sector": sector,
                "eigenvalue": values[0],
                "multiplicity": len(values),
            })
    write_csv(results / "sector_spectra_L6_d10.csv", sector_rows)

    audit = json.loads((results / "audit_results.json").read_text(encoding="utf-8"))
    summary = {
        "wick_rectangular_cells": audit["wick_rectangular_rank_deficient"]["cells"],
        "wick_d_lt_L_cells": audit["wick_rectangular_rank_deficient"]["d_lt_L_cells"],
        "wick_rectangular_max_eigenvalue_error": audit["wick_rectangular_rank_deficient"]["max_eigenvalue_error"],
        "wick_d_lt_L_max_eigenvalue_error": audit["wick_rectangular_rank_deficient"]["max_d_lt_L_eigenvalue_error"],
        "rank_one_boundary_cells": audit["wick_rank_one_boundary"]["cells"],
        "rank_one_boundary_max_eigenvalue_error": audit["wick_rank_one_boundary"]["max_eigenvalue_error"],
        "gamma_zero_identity_cells": audit["wick_gamma_zero_boundary"]["cells"],
        "gamma_zero_max_identity_error": audit["wick_gamma_zero_boundary"]["max_identity_error"],
        "raw_spectrum_cells": audit["raw_rectangular"]["spectrum_cells"],
        "raw_quadratic_form_cells": audit["raw_rectangular"]["quadratic_form_cells"],
        "raw_max_eigenvalue_error": audit["raw_rectangular"]["max_eigenvalue_error"],
        "raw_max_quadratic_form_error": audit["raw_rectangular"]["max_quadratic_form_error"],
        "raw_even_branch_cells": audit["raw_even_negative_branch"]["cells"],
        "raw_even_branch_max_gradient_norm": audit["raw_even_negative_branch"]["max_gradient_norm"],
        "raw_even_branch_max_eigenvalue_error": audit["raw_even_negative_branch"]["max_eigenvalue_error"],
        "embedded_quartic_path_cells": audit["embedded_quartic_path"]["cells"],
        "embedded_quartic_path_max_abs_error": audit["embedded_quartic_path"]["max_abs_error"],
        "ambient_hermite_direction_cells": audit["ambient_hermite_leakage_direction"]["cells"],
        "ambient_hermite_direction_max_abs_error": audit["ambient_hermite_leakage_direction"]["max_abs_error"],
        "inertia_formula_cells": audit["hermite_leakage_counts"]["cells"],
        "inertia_formula_mismatches": audit["hermite_leakage_counts"]["mismatches"],
    }
    (results / "audit_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
