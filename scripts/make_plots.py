from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results = root / "results"
    plots = root / "plots"
    plots.mkdir(parents=True, exist_ok=True)

    rows = read_csv(results / "rectangular_inertia.csv")
    L = 6
    selected = [r for r in rows if int(r["L"]) == L and int(r["d"]) <= 30]
    d = [int(r["d"]) for r in selected]
    wick = [int(r["wick_index"]) for r in selected]
    raw = [int(r["raw_index"]) for r in selected]
    inflation = [int(r["index_inflation"]) for r in selected]
    plt.figure(figsize=(7.2, 4.6))
    plt.plot(d, wick, marker="o", label="Wick index")
    plt.plot(d, raw, marker="s", label="Raw Gaussian index")
    plt.plot(d, inflation, marker="^", label="Index inflation")
    plt.xlabel("Ambient dimension d")
    plt.ylabel("Number of negative Hessian eigenvalues")
    plt.title(f"Hermite-leakage index inflation (L={L})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots / "hermite_leakage_index_inflation.png", dpi=220)
    plt.close()

    rows = read_csv(results / "wick_rank_sweep.csv")
    rank = [int(r["rank"]) for r in rows]
    index = [int(r["index"]) for r in rows]
    nullity = [int(r["nullity"]) for r in rows]
    positive = [int(r["positive"]) for r in rows]
    plt.figure(figsize=(7.2, 4.6))
    plt.plot(rank, index, marker="o", label="Index")
    plt.plot(rank, nullity, marker="s", label="Nullity")
    plt.plot(rank, positive, marker="^", label="Positive eigenvalues")
    plt.xlabel("Teacher Gram rank r")
    plt.ylabel("Multiplicity")
    plt.title("Rank-deficient Wick inertia (L=12, d=18)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots / "wick_rank_deficiency_bifurcation.png", dpi=220)
    plt.close()

    rows = read_csv(results / "equicorrelation_boundary.csv")
    plt.figure(figsize=(7.2, 4.6))
    for L in (4, 8, 16):
        selected = [r for r in rows if int(r["L"]) == L and float(r["one_minus_rho"]) > 0]
        x = [float(r["one_minus_rho"]) for r in selected]
        y = [float(r["specialization_curvature"]) for r in selected]
        plt.loglog(x, y, marker="o", label=f"L={L}")
    plt.xlabel("Distance to rank-one boundary, 1-rho")
    plt.ylabel("Absolute specialization curvature")
    plt.title("Collapse of negative curvature near rho=1 (unnormalized)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(plots / "equicorrelation_rank_one_boundary.png", dpi=220)
    plt.close()

    rows = read_csv(results / "sector_spectra_L6_d10.csv")
    labels = [f"{r['metric']}:{r['sector']}" for r in rows]
    values = [float(r["eigenvalue"]) for r in rows]
    multiplicities = [int(r["multiplicity"]) for r in rows]
    positions = list(range(len(rows)))
    plt.figure(figsize=(9.2, 4.8))
    bars = plt.bar(positions, values)
    for bar, mult in zip(bars, multiplicities):
        y = bar.get_height()
        va = "bottom" if y >= 0 else "top"
        plt.text(bar.get_x() + bar.get_width() / 2, y, f"x{mult}", ha="center", va=va, fontsize=8)
    plt.axhline(0.0, linewidth=0.8)
    plt.xticks(positions, labels, rotation=40, ha="right")
    plt.ylabel("Eigenvalue")
    plt.title("Exact Hessian sectors (L=6, d=10)")
    plt.tight_layout()
    plt.savefig(plots / "sector_spectrum_comparison.png", dpi=220)
    plt.close()


if __name__ == "__main__":
    main()
