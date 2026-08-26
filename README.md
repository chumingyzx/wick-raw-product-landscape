# Wick/Raw Product Landscape Preprint v0.3.1

This release contains the minor-revision version of

> **Collapsed-Saddle Spectra for Products of Linear Forms: Hermite Leakage and Metric-Dependent Hessian Inertia**

## Decision

```text
GO_V0_3_1_FOR_ACCOUNTABLE_HUMAN_EXPERT_CIRCULATION
```

Version 0.3.1 closes the three clarifications requested by the v0.3 formula-level re-audit: review provenance, the normalization qualifier for the correlation-dependent curvature statement, and the definition of the top-degree coefficient map `Phi`. The central theorems and numerical formulas are unchanged.

## Review provenance

The audit records in `reviews/` are **AI-assisted formula-level audits**, not anonymous or named human peer review. They used independent derivations, independently implemented permanent/Isserlis calculations, automatic differentiation, numerical checks, and targeted literature comparison. They support author-side quality control but do not establish publication priority or substitute for accountable human specialist review.

## Primary deliverables

- `paper/Wick_Raw_Product_Landscape_Preprint_v0.3.1.pdf` - revised English preprint.
- `paper/main.tex` - LaTeX source.
- `response/Response_to_v0.3_Formula_Level_ReAudit_v0.3.1.pdf` - response closing R1-R3.
- `response/Response_to_v0.3_Formula_Level_ReAudit_v0.3.1.md` - editable response.
- `reviews/v0.2/` and `reviews/v0.3/` - unchanged source audit records.
- `docs/01_v0.3.1_Minor_Revision_Matrix_CN.md` - R1-R3 closure matrix.
- `results/audit_summary.json` - mathematical audit.
- `VALIDATION_SUMMARY.json` - bundle validation.

## Core formulas

For a regular PSD Wick teacher with Gram rank `r`:

```text
index    = (r-1)(L-1)
nullity  = (d-r+1)(L-1)
positive = d
```

For the ordinary Gaussian product with an orthonormal teacher frame:

```text
index    = (d-1)(L-1)
nullity  = L-1
positive = d
```

For the respective collapsed critical representatives under the two metrics:

```text
raw index - Wick index = (d-L)(L-1)
```

## Reproduction

```bash
python -m pip install -r requirements.txt
python scripts/run_all.py
```

To verify the shipped immutable snapshot before regeneration:

```bash
python verify_manifest.py
```

Rebuilding the PDFs changes their binary hashes.

## License

The repository is distributed under the MIT License included in `LICENSE`. Manuscript authorship, citation metadata, and public-release timing still require separate decisions before dissemination.

## Status

```text
V0_3_1_MINOR_REVISION_COMPLETE
R1_R3_CLOSED
CORE_SPECTRA_INDEPENDENTLY_REAUDITED
AI_ASSISTED_AUDIT_PROVENANCE_DISCLOSED
HUMAN_PEER_REVIEW_NOT_ESTABLISHED
NO_DIRECT_DUPLICATE_LOCATED_IN_REVIEWED_SOURCES
PUBLICATION_PRIORITY_UNRESOLVED
MATHEMATICAL_BREAKTHROUGH_NOT_CLAIMED
```
