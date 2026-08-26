# 外部数学专家审查报告

## 稿件信息

**题目：** *Collapsed-Saddle Spectra for Products of Linear Forms: Hermite Leakage and Metric-Dependent Morse Index*  
**版本：** v0.2，2026-08-25  
**审查范围：** 核心定理的正确性、证明闭合性、假设与重数、渐近结论、计算验证，以及 `Expert Formula-Level Duplication Checklist` 所要求的定理级重复审查。  
**审查结论：** **Major revision before public submission / priority claim**。

---

## 1. 总体结论

我对稿件的三个核心结论进行了独立推导和有限规模复核：

1. rectangular / rank-deficient Wick Hessian 全谱；
2. orthonormal-teacher raw Gaussian product 的六扇区 Hessian 全谱；
3. 
   \[
   \operatorname{col}(U)^\perp\otimes\mathbf 1^\perp
   \]
   从 Wick-null 到 raw-negative 的转换，以及精确 index 增量
   \[
   (d-L)(L-1).
   \]

**我的判断是：这三个核心公式在现有假设下是正确的。** 我没有发现特征值符号、重数、总维数、index、nullity 或 positive count 的错误。Wick 的 rank-one 与 zero-row-sum 边界、raw/Wick 的主要弱曲率渐近式，以及文中给出的受限四次逃逸路径也都能独立复核。

但是，当前版本还不应直接作为“证明与优先权均已闭合”的投稿稿件。至少有四类必须修正的问题：

- raw 谱定理宣称临界性，但正文证明没有给出完整参数梯度的消去；
- \(c_L\) 的实根分支在偶数 \(L\) 时未说明；
- “更精细尺度由 \(\rho_L\sqrt L\) 控制”的陈述目前过宽，且稿件所称的 accompanying derivation tables 不在包内；
- 精确逃逸路径的矩阵维数写法只在已做坐标约化时成立，正文没有说明该约化。

在定理级重复审查方面，**我没有定位到直接写出这些谱公式的既有定理，也没有定位到只需短代入即可推出全部系数和重数的更一般定理。** 最接近的工作分别提供：参数化临界性的判别、一般 Hessian pullback/残差曲率公式、Chow/neuromanifold 的奇异性或临界点计数、以及其他 tensor 模型中的对称 Hessian 分解；它们没有直接产生本文的 permanent/Isserlis 系数及六扇区重数。因此，这组公式**有条件地足以构成一篇独立 theorem note**，但这仍不是文献优先权证明。

---

## 2. Expert Review Checklist：逐项判定

| Checklist item | 判定 | 外部审查意见 |
|---|---:|---|
| A prior theorem directly states the rectangular/rank-deficient Wick spectrum. | **NO located** | 未找到直接陈述 Theorem 4.1 全谱、rank-dependent inertia 与全部重数的来源。 |
| A prior theorem yields that spectrum by a short explicit substitution. | **NO located** | 一般 smooth-lift 理论只给 Hessian 分解；仍需 permanent 二阶导数和扇区计算。 |
| A prior theorem directly states the arbitrary-order rectangular raw six-sector spectrum. | **NO located** | 未找到对单个 \(L\) 个线性形式乘积、任意 \(L\)、\(d\ge L\) 的同一六扇区谱。 |
| A prior theorem yields that spectrum by a short explicit substitution. | **NO located** | 现有 polynomial-network 精确 Hessian signature 主要闭合在 quadratic activation；不能直接代入得到本文 raw 公式。 |
| A prior source identifies exactly \(\operatorname{col}(U)^\perp\otimes\mathbf1^\perp\) and its Wick-null/raw-negative conversion. | **NO located** | 未找到相同 eigenspace、两种 metric 下的精确符号转换及系数。 |
| A prior source gives the exact index increase \((d-L)(L-1)\). | **NO located** | 未找到相同公式。 |
| The results are correct but should be framed as a worked corollary of a broader theory. | **PARTIAL** | Proposition 3.1 属于一般 smooth-parametrization Hessian chain rule 的实例；但两个全谱不是一行式 corollary，仍包含模型特定计算。 |
| A proof, assumption, multiplicity, or asymptotic statement appears incorrect. | **YES, but not in the core spectra** | raw 临界性证明缺口、偶数阶根分支未定义、\(\rho_L\sqrt L\) 说法过宽/无配套推导表、逃逸路径维数表述不完整。 |
| The formulas appear distinct enough for a standalone theorem note. | **YES, conditionally** | 在补齐证明、限制渐近陈述并扩展最近相关文献后，足以独立成文。 |

**建议的总评级：** `MAJOR_REVISION`，而非 reject，也不是 accept as is。

---

## 3. 核心数学结果的独立核查

### 3.1 Permanent 导数引理

在 \(A_0=\alpha J\) 处，

\[
D\operatorname{perm}(A_0)[E]
=(L-1)!\alpha^{L-1}\mathbf1^TE\mathbf1
\]

以及

\[
D^2\operatorname{perm}(A_0)[E,F]
=(L-2)!\alpha^{L-2}
\left[
 s(E)s(F)-r(E)^Tr(F)-c(E)^Tc(F)+\langle E,F\rangle_F
\right]
\]

均可由“被微分位置必须位于不同的行和列”及 inclusion–exclusion 直接得到。稿件中的系数、是否使用 ordered pairs、以及最后的 Frobenius 项均正确。

### 3.2 Rectangular / rank-deficient Wick 谱

假设

\[
T=U^TU\succeq0,\qquad T\mathbf1=\gamma\mathbf1,\qquad \gamma>0,
\]

并令 \(r=\operatorname{rank}(T)\)。在

\[
W_\star=\frac1L UJ
\]

处，确有

\[
W_\star^TW_\star=W_\star^TU=\frac\gamma L J,
\]

故 student norm 与 teacher cross term 的一阶导数完全消去。采用左侧分解

\[
\mathbb R^d
=
\operatorname{span}\{p_0\}
\oplus
\bigl(\operatorname{col}(U)\cap p_0^\perp\bigr)
\oplus
\operatorname{col}(U)^\perp
\]

以及右侧分解

\[
\mathbb R^L=\operatorname{span}\{\mathbf1\}\oplus\mathbf1^\perp,
\]

稿件列出的六类特征值为：

\[
L(L-1)\gamma b_L,
\quad 0,
\quad (L-1)(\gamma+\mu_i)b_L,
\quad -\mu_i b_L,
\quad (L-1)\gamma b_L,
\quad 0,
\]

其中

\[
b_L=(L-2)!\left(\frac\gamma L\right)^{L-2}.
\]

这些值及其重数相加为 \(dL\)，并给出

\[
\operatorname{index}=(r-1)(L-1),
\qquad
\operatorname{nullity}=(d-r+1)(L-1),
\qquad
n_+=d.
\]

这一结果在 \(d<L\) 时仍成立；该区域虽未被原 bundle 的自动审计覆盖，但我补做了 \((L,d,r)=(4,2,2),(5,2,2),(5,3,3),(6,3,2),(7,4,4),(8,3,3)\) 六组自动微分 Hessian 检查。所有 inertia 均吻合，最大特征值绝对误差为 \(3.53\times10^{-13}\)。

### 3.3 Wick 奇异边界

- **Rank-one boundary：** 当 \(r=1\) 时，PSD 与常数行和共同推出
  \[
  T=\frac\gamma L J.
  \]
  各 teacher column 相同，从而 \(W_\star=U\)，是零损失全局极小点；Hessian PSD，稿件 inertia 正确。

- **Zero-row-sum boundary：** 若 \(T\mathbf1=0\)，则
  \[
  \|U\mathbf1\|^2=\mathbf1^TT\mathbf1=0,
  \]
  所以 \(U\mathbf1=0\) 且 \(W_\star=0\)。由 permanent 的齐次性，
  \[
  \mathcal L_U(tH)-\mathcal L_U(0)
  =-t^L\operatorname{perm}(H^TU)
  +\frac12t^{2L}\operatorname{perm}(H^TH).
  \]
  对 \(L\ge3\)，梯度和 Hessian 均为零。该命题正确。

### 3.4 Raw collapsed point 的临界性

稿件给出的尺度关系

\[
c_L^L=\frac{L!}{L^L(2L-1)!!}
\]

正确，但目前只通过 collapsed ray 的矩计算引入，尚未在定理证明中验证完整的 \(dL\)-维梯度。应补入以下短证明。

记 \(S=m^Tx\)。对任意 column \(a\)，

\[
\nabla_{w_a}\mathcal R_U(W_\star)
=
 c_L^{2L-1}\mathbb E[S^{2L-1}x]
-c_L^{L-1}\mathbb E[\tau_U S^{L-1}x].
\]

由 Gaussian integration by parts 与 teacher 坐标的直接计数，

\[
\mathbb E[S^{2L-1}x]
=(2L-1)!!L^{L-1}m,
\qquad
\mathbb E[\tau_U S^{L-1}x]=(L-1)!m.
\]

因此

\[
\nabla_{w_a}\mathcal R_U(W_\star)
=c_L^{L-1}
\left[c_L^L(2L-1)!!L^{L-1}-(L-1)!\right]m=0.
\]

这会把“沿一维 collapsed ray 为 stationary”提升为真正的参数空间临界性。

### 3.5 Raw Hessian quadratic form 与六扇区谱

稿件的两个关键矩恒等式均正确：

\[
\mathbb E[S^{2L-2}(v^Tx)(w^Tx)]
=(2L-3)!!L^{L-2}
\left[L v^Tw+2(L-1)(m^Tv)(m^Tw)\right],
\]

以及

\[
\mathbb E[\tau_U S^{L-2}(v^Tx)(w^Tx)]
=(L-2)!\left[(m^Tv)(m^Tw)-v^TPw\right].
\]

代入

\[
D^2\mathcal R[H,H]
=\mathbb E[(F')^2+(F-\tau_U)F'']
\]

后，Theorem 5.1 的 quadratic form 系数均吻合。将其限制到

\[
\operatorname{span}\{m\}\oplus
(\operatorname{col}(U)\cap m^\perp)
\oplus\operatorname{col}(U)^\perp
\]

与

\[
\operatorname{span}\{\mathbf1\}\oplus\mathbf1^\perp
\]

的 tensor-product sectors，确实得到：

\[
\begin{array}{c|c|c}
\text{sector}&\lambda&\text{multiplicity}\\\hline
\text{radial}&L(L-1)k_L&1\\
\text{gauge}&0&L-1\\
\text{teacher collective}&2(L-1)k_L&L-1\\
\text{teacher specialization}&-\dfrac{3L-2}{2L-1}k_L&(L-1)^2\\
\text{ambient collective}&(L-1)k_L&d-L\\
\text{ambient specialization}&-\dfrac{L-1}{2L-1}k_L&(d-L)(L-1).
\end{array}
\]

从而

\[
\operatorname{index}=(d-1)(L-1),
\qquad
\operatorname{nullity}=L-1,
\qquad n_+=d.
\]

未发现系数或重数错误。

### 3.6 偶数 \(L\) 的尺度分支

正文目前只写

\[
c_L^L=C_L>0
\]

而没有规定 \(c_L\) 是正根。对偶数 \(L\)，有两个实根 \(\pm c_L\)。应明确：

> Let \(c_L>0\) denote the positive real root of (5.1). For even \(L\), the point \(-c_Lm\mathbf1^T\) is a second collapsed critical representative of the same predictor and has the same Hessian spectrum.

我对 \(L=2,4,6\) 的正、负两分支分别计算了 exact-moment raw Hessian；梯度范数均在 \(10^{-16}\) 量级，且两分支谱相同，最大误差 \(1.07\times10^{-15}\)。

### 3.7 Hermite-leakage index inflation

对 orthonormal teacher，Wick 谱中的

\[
\operatorname{col}(U)^\perp\otimes\mathbf1^\perp
\]

具有零特征值，而 raw quadratic form 在同一单位方向 \(H=nq^T\) 上给出

\[
D^2\mathcal R_U(W_\star)[H,H]
=-\frac{L-1}{2L-1}k_L.
\]

因此新增负方向的维数正是

\[
\dim\operatorname{col}(U)^\perp\cdot\dim\mathbf1^\perp
=(d-L)(L-1),
\]

并与两个 index 的差一致。该结论正确。

为了使“lower-Hermite contraction”不只是命名，建议在证明中显式指出：在该 sector 上 \(H\mathbf1=0\)，故 Gauss–Newton 项为零；raw residual term 中两个 ambient factors 可以彼此配对，产生负的 self-contraction，而 Wick ordering 删除该 contraction。这样机制与数值公式直接对应。

### 3.8 弱曲率渐近式

以下三个式子均正确：

\[
\frac{(L-2)!}{L^{L-2}}
\sim\sqrt{2\pi L}\,e^{-L},
\]

\[
|\lambda_{\mathrm{teacher,spec}}^{\mathrm{raw}}|
\sim 6\sqrt2\,\pi L(2e)^{-L},
\]

\[
|\lambda_{\mathrm{ambient,spec}}^{\mathrm{raw}}|
\sim 2\sqrt2\,\pi L(2e)^{-L}.
\]

对固定 \(\rho\in(0,1)\)，equicorrelation 的 normalized specialization curvature

\[
\frac{|\lambda_{\mathrm{spec}}(T_\rho)|}{\operatorname{perm}(T_\rho)}
\sim \frac{1-\rho}{\rho^2L(L-1)}
\]

也正确。

问题出在随后一句：

> More refined regimes are controlled by \(\rho_L\sqrt L\); these formulas are included in the accompanying derivation tables.

包内没有对应 derivation tables；并且若不限制 \(\rho_L\) 所在的 asymptotic window，\(\rho_L\sqrt L\) 不能单独决定所有趋向 \(\rho=0\) 的 regime。

令

\[
x_L=\frac{1-\rho_L}{\rho_L},
\qquad
E_L(x)=\sum_{j=0}^L\frac{x^j}{j!}.
\]

由

\[
\operatorname{perm}(T_\rho)=\rho^LL!E_L(x)
\]

可得到精确式

\[
\boxed{
C_L(\rho)
=
\frac{x(x+1)}{L(L-1)}
\frac{(1+x/L)^{L-2}}{E_L(x)}
}.
\]

在 crossover window \(x_L=O(\sqrt L)\) 中，\(\rho_L\sqrt L\) 的确是自然参数；若

\[
\rho_L\sqrt L\to t\in(0,\infty),
\]

则

\[
C_L(\rho_L)
\sim
\frac{e^{-1/(2t^2)}}{t^2L}.
\]

但当 \(x_L\) 接近更高幂次甚至 \(\Theta(L)\) 时，高阶对数项与 truncated-exponential/Poisson-tail 行为进入，单独知道 \(\rho_L\sqrt L\to0\) 不足以区分它们。

**建议二选一：**

1. 删除该句，仅保留 fixed-\(\rho\) 结论；或
2. 将其改成一个带明确假设（例如 \(x_L=O(\sqrt L)\)）的 proposition，并附证明。

### 3.9 精确受限逃逸路径

四次恒等式本身正确，但路径应写成

\[
W(t)=U\left(\frac1LJ+tK\right),
\]

或者先明确声明“经正交坐标约化，取 \(d=L\) 且 \(U=I_L\)”，然后再写

\[
W(t)=\frac1LJ+tK.
\]

当前文字中一般 \(W\in\mathbb R^{d\times L}\)，而 \(J/L+tK\in\mathbb R^{L\times L}\)，因此存在表面维数不一致。

还应把 “normalized \(2\times2\) row/column contrast” 明确定义，例如

\[
K=\frac12(e_i-e_j)(e_p-e_q)^T,
\]

其中 \(i\ne j\)、\(p\ne q\)。

采用正确嵌入后，我对 \(L=2,\ldots,7\) 和多个正负 \(t\) 复核了

\[
\mathcal L(W(t))-\mathcal L(W(0))
=-\frac{a_L}{2}t^2+\frac{a_L}{4}t^4;
\]

最大绝对误差为 \(6.14\times10^{-16}\)。

---

## 4. 定理级重复与可归约性审查

### 4.1 最接近来源及其实际覆盖范围

| 来源 | 可直接使用的结果 | 与本文的关系 | 判定 |
|---|---|---|---|
| Levin–Kileel–Boumal, *The effect of smooth parametrizations on nonconvex optimization landscapes*, Lemma 3.11 | Hessian pullback = Gauss–Newton/拉回 Hessian + 参数化二阶 residual term | 直接解释稿件 Proposition 3.1 的一般结构，但不产生 permanent/Isserlis 系数和重数 | **机制级归约** |
| Kohn–Montúfar–Shahverdi–Trager, *Function Space and Critical Points of Linear Convolutional Networks*, Theorem 2.11 | 通过相邻多项式因子的公因子刻画 parameterization-map criticality | 处理多项式因解与奇异参数化，但没有 Gaussian population Hessian 谱 | **相邻框架** |
| Shahverdi–Marchetti–Kohn, *On the Geometry and Optimization of Polynomial Convolutional Networks*, Proposition 4.11 / Section 5 | neuromanifold、generic critical-point count；作者明确指出 ED degree 不区分 maxima/minima/saddles | 不能给本文的局部 signed spectrum | **相邻框架** |
| Arjevani–Bruna–Kileel–Polak–Trager, *Geometry and Optimization of Shallow Polynomial Networks*, Section 4 | distribution-induced inner products；quadratic activation 下完整临界点与 Hessian signature | metric 观点接近，但 exact landscape 闭合在 quadratic shallow network，不是一个 Chow product 的任意阶结果 | **相邻框架** |
| Torrance–Vannieuwenhoven, Chow smooth-locus second fundamental form | smooth Chow locus 的二阶几何可进入 squared-distance Riemannian Hessian | collapsed repeated-factor 点的 factor map 高度奇异，不能直接用 smooth-locus 公式得到本文 parameter-space 谱 | **相邻框架** |
| Shahverdi–Marchetti–Kohn, *Learning on a Razor’s Edge* | polynomial network 的 identifiability/singularity/exposedness；critical-point type 留作后续问题 | 没有 Hessian signature | **相邻框架** |
| *Singular Learning and Occam’s Razor in Deep Monomial Networks*, Theorem 5.1 | 高 activation degree 下 subnetwork 与 parameterization criticality 等价 | 仍是 Jacobian/criticality 层面，没有本文 Hessian 系数 | **相邻框架** |
| Marchetti–Connelly–Breiding–Kohn, *Critical Points of Degenerate Metrics on Algebraic Varieties* | 退化 quadratic metric 下临界点与投影/ramification 的关系 | 处理 critical-point geometry/count，而非固定奇异分解处的 signed Hessian spectrum | **相邻框架** |

这里“机制级归约”对应 checklist 中的 `MECHANISM_CLASS_REDUCTION`；“相邻框架”对应 `ADJACENT_FRAMEWORK`。

### 4.2 为什么不存在“短代入式归约”

若要从既有定理短代入得到本文结果，至少需要原定理同时处理：

1. 单个 \(L\)-factor Chow product，而非 rank-one powers 的和；
2. 所有 factor 完全重合的 singular parameter point；
3. Wick/top-chaos 与 full raw-Gaussian 两种具体内积；
4. factor-coordinate Hessian 的符号、精确系数与矩形重数。

上述最接近来源最多覆盖其中一至两项。尤其是一般 pullback Hessian 公式只把问题降为 residual bilinear form 的计算；本文的关键工作恰好在于用 permanent derivatives 和 Gaussian pairings 计算这个 residual form，并同时对左右 invariant sectors 对角化。因此不应把主要谱定理降格成某个现有定理的“一行 corollary”。

另一方面，稿件也不应把一般 chain rule、Chow 奇异性或 symmetry-sector 思想表述为自身原创。最准确的定位是：

> **A model-specific exact singular-fiber Hessian calculation situated inside the broader smooth-lift and neuroalgebraic-geometry framework.**

### 4.3 文献优先权判断的限度

本审查未找到 direct duplicate，但不能排除：

- 未索引讲义、博士论文或其他语言文献；
- 更一般定理中未被作者显式展开的特殊情形；
- 与 Gaussian chaos/tensor regression 相邻但使用不同术语的结果。

因此可写“no direct theorem-level duplicate was located in the reviewed primary literature”，不能写“no such theorem exists”或“first discovery”。

---

## 5. 必须修改的问题

### M1. 补齐 raw 临界性证明

在 Theorem 5.2 前或证明开头加入第 3.4 节给出的完整梯度消去。仅由 collapsed ray 的标量 stationary condition 不能自动推出所有 transverse derivatives 为零。

### M2. 定义 \(c_L\) 的根分支

将正文改为：

> Let \(c_L>0\) be the positive real root of ...

并在 remark 中说明偶数 \(L\) 的负分支及其相同谱。

### M3. 修正 equicorrelation 的变尺度渐近声明

删除无配套材料的 “these formulas are included in the accompanying derivation tables”。若保留 \(\rho_L\sqrt L\) 说法，应给出精确公式、明确 scaling window 和证明，不能把它写成覆盖所有 \(\rho_L\to0\) 的统一结论。

### M4. 修正 exact escape path 的维数与坐标约化

将路径写为 \(U(J/L+tK)\)，或先明确约化到 \(d=L,U=I\)。同时给出 \(K\) 的具体定义。

### M5. 扩充并更新 closest-literature section

当前参考文献表遗漏了若干最接近且截至 2026 年已公开的工作，至少应讨论：

- Kohn, Merkh, Montúfar, Trager, *Geometry of Linear Convolutional Networks*, SIAGA 6(3), 2022；
- Kohn, Montúfar, Shahverdi, Trager, *Function Space and Critical Points of Linear Convolutional Networks*, SIAGA 8(2), 2024，尤其 Theorem 2.11；
- Shahverdi, Marchetti, Kohn, *On the Geometry and Optimization of Polynomial Convolutional Networks*, AISTATS 2025，尤其 Proposition 4.11 与结论中的 critical-type limitation；
- Shahverdi, Marchetti, Kohn, *Learning on a Razor’s Edge: Identifiability and Singularity of Polynomial Neural Networks*, ICLR 2026；
- Marchetti, Connelly, Breiding, Kohn, *Critical Points of Degenerate Metrics on Algebraic Varieties*, arXiv:2512.21029；
- *Singular Learning and Occam’s Razor in Deep Monomial Networks*, arXiv:2606.28464，尤其 Theorem 5.1。

加入这些来源不会使本文成为重复，但会使“为何不是直接 corollary”的论证更可信。

### M6. 把 Hermite-leakage 机制写成一个显式计算

目前 index conversion 是两个谱定理的直接比较。建议增加一段针对

\[
H=nq^T,
\quad n\perp\operatorname{col}(U),
\quad q\perp\mathbf1
\]

的单方向计算，明确指出 raw 的负项来自 ambient factors 的 self-contraction，而 Wick ordering 将其移除。这样标题中的机制性术语有直接数学内容支撑。

---

## 6. 次要但建议修改的问题

1. **“Morse index”术语。** 文中临界点通常有非零 nullity，因此并非 Morse critical points。虽然 Section 2.3 已把 index 定义为负 Hessian eigenvalue 数，标题和摘要中使用 “Hessian index” 或 “extended Morse/Hessian index” 更不易误解。

2. **同一 parameterization / 不同 metric 的表述。** 更精确的说法是：二者使用同一个 factor map 到 homogeneous coefficient tensor/Chow cone，但对该 coefficient space 采用 top-chaos 与 raw Gaussian 两种内积。Wick-ordered student function 与 ordinary product 并非逐点相同的多项式表达；orthonormal teacher 的两种 teacher function 则因交叉 contraction 消失而一致。

3. **Theorem 6.1 的层级。** 它在形式上是前两个谱定理的一行 corollary。可保留命名，但从数学组织上称为 “Corollary (Hermite-leakage index inflation)” 更自然。

4. **重复标题/文字。** LaTeX 源中 `Lift-level decomposition of factor-space curvature` section 标题重复一次；appendix 的 rank-dependence 段落也重复一次，应清理。

5. **验证覆盖说明。** 正文计算审计表应注明原始 Wick AD grid 使用 \(d\ge L\)，而定理允许 \(d<L\)。可加入本审查所做的低维补充测试，或在自带测试中正式加入这些 case。

6. **“circulation-ready”措辞。** 在 M1–M5 修复前，更稳妥的状态是 `proof-core-verified, manuscript-major-revision-required`；修复后可恢复 `circulation-ready, priority-unresolved`。

---

## 7. 计算审计结果

我重新运行了 bundle 自带流程：

- manifest：**46/46 files verified**；
- validation：**1340/1340 checks passed**；
- unit tests：**7/7 passed**。

此外补做了三组原包之外的审计：

| 扩展检查 | 结果 |
|---|---|
| Wick theorem 在 \(d<L\) 的 6 组 rank-deficient case | inertia 全部吻合；最大谱误差 \(3.53\times10^{-13}\) |
| raw 偶数阶正/负 collapsed branch，\(L=2,4,6\) | 两分支均临界且谱相同；最大谱误差 \(1.07\times10^{-15}\) |
| 正确嵌入后的 exact quartic path，\(L=2,\ldots,7\) | 最大绝对误差 \(6.14\times10^{-16}\) |

这些结果显著提高了对公式正确性的信心，但不替代解析证明。

---

## 8. 最终建议

### 对正确性的判断

**Acceptable after revision.** 核心定理族目前看是正确的；没有理由因数学错误拒稿。

### 对新颖性的判断

**Provisionally distinct at formula level.** 未定位到直接重复或一行归约，但不能据此宣布优先权。最合理的 claim ceiling 是：

> The exact rectangular spectra and the ambient Wick-null/raw-negative conversion were not found in the primary literature reviewed; the results remain embedded in general smooth-lift, tensor, Chow, and polynomial-network frameworks.

### 对稿件状态的判断

**Major revision。** 在补齐 raw 临界性、根分支、变尺度渐近、路径维数以及最近相关工作之前，不建议以当前形式公开宣称 “priority-ready”。完成这些修改后，稿件有充分理由作为一篇紧凑的 standalone theorem note 进入外部 circulation。

---

## 9. 审查置信度

- 核心谱公式正确性：**高**；
- 边界与主要固定参数渐近式：**高**；
- 未存在 direct duplicate 的判断：**中等偏高，但非穷尽性**；
- 发表优先权：**未解决**。
