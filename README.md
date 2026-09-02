# Collapsed-Saddle Spectra for Products of Linear Forms

Code, figures, and manuscript source for the preprint:

> **Collapsed-Saddle Spectra for Products of Linear Forms: Hermite Leakage and Metric-Dependent Hessian Inertia**

[Read the current preprint](paper/Wick_Raw_Product_Landscape_Preprint_v0.3.1.pdf)

## Overview

We study population least-squares landscapes for a single product of linear forms under isotropic Gaussian input. The paper derives complete parameter-space Hessian spectra at fully collapsed repeated-factor critical points and compares two population metrics induced by the same factorized top-degree coefficient map: a Wick/top-chaos metric and the ordinary Gaussian product metric.

For a regular PSD Wick teacher with Gram rank `r`, the collapsed Hessian has

```text
index    = (r - 1)(L - 1)
nullity  = (d - r + 1)(L - 1)
positive = d
```

For the ordinary Gaussian product with an orthonormal teacher frame,

```text
index    = (d - 1)(L - 1)
nullity  = L - 1
positive = d
```

For the corresponding collapsed critical representatives, the additional negative-curvature sector has dimension

```text
(d - L)(L - 1)
```

and is exactly `col(U)^perp ⊗ 1^perp`: it is Hessian-null in the Wick metric and strictly negative in the raw Gaussian metric.

## Repository structure

```text
paper/        manuscript source and current PDF
src/          closed-form formulas and independent numerical checks
scripts/      result generation, plotting, and reproduction entry point
tests/        unit tests
results/      numerical tables used in the analysis
plots/        generated figures
```

## Reproduction

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests, numerical checks, figure generation, and manuscript build:

```bash
python scripts/run_all.py
```

A working LaTeX installation with `pdflatex` is required to rebuild the manuscript.

## AI assistance

This project was developed through an AI-assisted mathematical research workflow with OpenAI's ChatGPT (**GPT-5.6 Sol Pro**). ChatGPT was used extensively for hypothesis generation, theorem exploration, symbolic derivations, proof checking, counterexample search, computational audit design, code development, literature comparison, and manuscript revision.

The mathematical statements are documented through explicit derivations and reproducible computational checks in this repository. AI assistance does not constitute independent authorship or human peer review.

## License

See [LICENSE](LICENSE).
