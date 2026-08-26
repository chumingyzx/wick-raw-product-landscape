# Completed Expert Formula-Level Duplication Checklist

**Manuscript:** *Collapsed-Saddle Spectra for Products of Linear Forms: Hermite Leakage and Metric-Dependent Morse Index*, v0.2  
**Recommendation:** **Major revision**  
**Core mathematical assessment:** The three central spectrum/index results appear correct. No direct theorem-level duplicate or one-line reduction was located in the reviewed primary literature. Publication priority remains unresolved.

- [ ] **A prior theorem directly states the rectangular/rank-deficient Wick spectrum.**  
  **Finding: NO LOCATED.** No reviewed source states the full factor-coordinate spectrum, multiplicities, rank-dependent index, and nullity of Theorem 4.1.

- [ ] **A prior theorem yields that spectrum by a short explicit substitution.**  
  **Finding: NO LOCATED.** Levin–Kileel–Boumal, Lemma 3.11, supplies the general pullback-Hessian decomposition, but a new permanent derivative and invariant-sector calculation is still required.

- [ ] **A prior theorem directly states the arbitrary-order rectangular raw six-sector spectrum.**  
  **Finding: NO LOCATED.** The nearest polynomial-network signature theorem closes the quadratic-activation case, not an arbitrary-order single Chow product.

- [ ] **A prior theorem yields that spectrum by a short explicit substitution.**  
  **Finding: NO LOCATED.** None of the reviewed tensor, Chow, polynomial-network, or degenerate-metric results fixes the Isserlis coefficients and rectangular multiplicities without a model-specific Hessian calculation.

- [ ] **A prior source identifies the exact ambient eigenspace `col(U)^perp tensor 1^perp` and its Wick-null/raw-negative conversion.**  
  **Finding: NO LOCATED.**

- [ ] **A prior source gives the exact index increase `(d-L)(L-1)`.**  
  **Finding: NO LOCATED.**

- [x] **The results are correct but should be framed as a worked corollary of a broader theory.**  
  **Finding: PARTLY.** The Gauss–Newton/residual decomposition is a standard smooth-lift specialization. The exact Wick and raw spectra are not one-line corollaries; they remain model-specific theorem-level calculations.

- [x] **A proof, assumption, multiplicity, or asymptotic statement appears incorrect.**  
  **Finding: YES, OUTSIDE THE CORE SPECTRA.** Required corrections: (i) explicitly prove full raw criticality; (ii) define the positive root `c_L` and mention the negative even-order branch; (iii) restrict or remove the claim that all refined equicorrelation regimes are controlled by `rho_L sqrt(L)`; (iv) correct the dimensionally incomplete escape-path notation; and (v) remove the reference to missing derivation tables. No error was found in the stated central eigenvalues or multiplicities.

- [x] **The formulas appear distinct enough for a standalone theorem note.**  
  **Finding: YES, CONDITIONALLY.** This judgment is contingent on completing the revisions and expanding the closest-literature discussion. It is not a proof of priority.

## Closest reductions reviewed

1. **Levin, Kileel, Boumal**, *The effect of smooth parametrizations on nonconvex optimization landscapes*, Lemma 3.11.  
   Mapping: `y = W`, `phi = factor-to-polynomial/tensor map`, `f = squared distance under the chosen metric`.  
   It gives the pullback Hessian plus residual-curvature term, but not the permanent/Isserlis bilinear form or sector multiplicities.

2. **Kohn, Montúfar, Shahverdi, Trager**, *Function Space and Critical Points of Linear Convolutional Networks*, Theorem 2.11.  
   It characterizes critical points of a polynomial factorization map via common factors. It does not evaluate a Gaussian population Hessian at the repeated-factor point.

3. **Shahverdi, Marchetti, Kohn**, *On the Geometry and Optimization of Polynomial Convolutional Networks*, Proposition 4.11 and Section 5.  
   It addresses regularity, singularities, and critical-point counts; the paper explicitly leaves critical-point type/Morse index unresolved.

4. **Arjevani, Bruna, Kileel, Polak, Trager**, *Geometry and Optimization of Shallow Polynomial Networks*, Section 4.  
   It studies distribution-induced metrics and complete signatures for quadratic networks, not the arbitrary-order product model here.

5. **Torrance, Vannieuwenhoven**, Chow smooth-locus second fundamental form.  
   The repeated-factor parameterization in the present manuscript is singular; the smooth-locus formula does not directly produce the factor-coordinate spectra.

## Final external-review disposition

```text
CORE_SPECTRA_INDEPENDENTLY_VERIFIED
NO_DIRECT_DUPLICATE_LOCATED
NO_ONE_LINE_REDUCTION_LOCATED
MAJOR_REVISION_REQUIRED
PUBLICATION_PRIORITY_UNRESOLVED
STANDALONE_THEOREM_NOTE_PLAUSIBLE_AFTER_REVISION
```
