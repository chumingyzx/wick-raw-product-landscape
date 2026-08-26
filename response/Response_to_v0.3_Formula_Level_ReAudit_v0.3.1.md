# Response to the v0.3 Formula-Level Re-audit

**Manuscript:** *Collapsed-Saddle Spectra for Products of Linear Forms: Hermite Leakage and Metric-Dependent Hessian Inertia*  
**Revision:** v0.3.1, 26 August 2026

## Audit provenance and disposition

The v0.3 re-audit was an AI-assisted formula-level audit performed with GPT-5.6 Pro using independent derivations, independently implemented Wick-permanent and raw Isserlis calculations, automatic differentiation, numerical spectrum checks, and targeted comparison with the closest located primary literature. It is an author-side quality-control record, not anonymous or named human peer review, and it does not establish publication priority.

The re-audit independently reproduced the core Wick and raw spectra, the Hermite-leakage sector, the embedded quartic path, and the restricted equicorrelation asymptotics. It found no new major mathematical defect and requested three local clarifications before public circulation or submission. Version 0.3.1 closes all three.

## R1. Review provenance and strength

**Request.** Remove or qualify wording such as `external mathematical review` and `externally reviewed`, which could be read as conventional human peer review.

**Revision.** The abstract and theorem paper no longer use those status claims. They now state only that independent formula-level rederivations and computational audits support the spectra, and that a targeted comparison did not locate a direct theorem-level duplicate or short explicit reduction in the primary sources examined. The paper explicitly states that accountable human peer review has not yet been established and that publication priority remains unresolved.

Repository-level provenance is recorded separately in `REVIEW_PROVENANCE.md` and `reviews/`. The original audit reports are preserved unchanged as source records.

## R2. Normalization qualifier for the curvature transition

**Request.** Qualify the statement that positive correlation changes the weak-curvature scale from exponential to polynomial, because that comparison is made after normalization by the teacher squared norm.

**Revision.** Contribution (iv) now states:

> after normalization by the teacher squared norm, fixed positive equicorrelation changes the specialization-curvature scale from the exponentially weak orthogonal case to polynomial order in L.

The exact normalization remains

\[
\frac{|\lambda_{\mathrm{spec}}(T_\rho)|}{\operatorname{perm}(T_\rho)}.
\]

No claim is made that the unnormalized curvature is polynomial in the same sense.

## R3. Definition of the map Phi

**Request.** Clarify that Section 3 uses the formal homogeneous top-degree coefficient map rather than the pointwise Wick random-function map.

**Revision.** Section 3 now states that `Phi` denotes the formal homogeneous top-degree coefficient map represented by its ordinary polynomial. In the Wick model, the same coefficient tensor is realized in the L-th Gaussian chaos by Wick ordering. The pointwise Wick differential is the Wick-ordered counterpart of the displayed ordinary-polynomial differential, and both have the kernel

\[
H\mathbf 1=0.
\]

This clarification leaves the chain-rule proposition, kernel, sector decomposition, and all spectrum formulas unchanged.

## Additional editorial improvements

The revision also:

1. labels the equicorrelation boundary figure as displaying **unnormalized** specialization curvature;
2. removes repeated audit-history prose from the theorem paper;
3. removes the redundant assumption `x_L = O(sqrt(L))` when `rho_L sqrt(L) -> t` is already imposed;
4. replaces `adjudication` with `assessment` where publication priority remains unresolved;
5. updates the release status, validation checks, and repository documentation to distinguish AI-assisted audit from human peer review.

## Mathematical scope

Version 0.3.1 changes wording and exposition only. The central theorems and their formulas are unchanged:

\[
\operatorname{index}_{\mathrm{Wick}}=(r-1)(L-1),
\qquad
\operatorname{nullity}_{\mathrm{Wick}}=(d-r+1)(L-1),
\]

\[
\operatorname{index}_{\mathrm{raw}}=(d-1)(L-1),
\qquad
\operatorname{nullity}_{\mathrm{raw}}=L-1,
\]

and, for orthonormal teachers and the respective collapsed representatives,

\[
\operatorname{index}_{\mathrm{raw}}-
\operatorname{index}_{\mathrm{Wick}}
=(d-L)(L-1).
\]

## Revised status

```text
V0_3_1_MINOR_REVISION_COMPLETE
R1_R3_CLOSED
CORE_SPECTRA_INDEPENDENTLY_REAUDITED
AI_ASSISTED_AUDIT_PROVENANCE_DISCLOSED
HUMAN_PEER_REVIEW_NOT_ESTABLISHED
NO_DIRECT_DUPLICATE_LOCATED_IN_REVIEWED_SOURCES
PUBLICATION_PRIORITY_UNRESOLVED
READY_FOR_ACCOUNTABLE_HUMAN_EXPERT_CIRCULATION
```
