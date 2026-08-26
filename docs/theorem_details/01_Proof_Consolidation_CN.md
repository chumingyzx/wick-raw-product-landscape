# 证明统一与符号修订

## 1. 统一模型

令 \(x\sim\mathcal N(0,I_d)\)，参数矩阵

\[
W=[w_1,\ldots,w_L]\in\mathbb R^{d\times L}.
\]

本 note 比较两个函数：

\[
g_W(x)=:\prod_{a=1}^L w_a^\top x:
\]

和

\[
f_W(x)=\prod_{a=1}^L w_a^\top x.
\]

Wick product 只保留第 \(L\) 阶 Gaussian chaos；raw product 同时包含所有允许的 lower-Hermite contractions。

对任意 \(W,U\)：

\[
\mathbb E[g_Wg_U]=\operatorname{perm}(W^\top U).
\]

因此 Wick population loss 完全由 permanent 控制。

## 2. Permanent 导数的统一引理

令 \(p(A)=\operatorname{perm}(A)\)，\(A_0=\alpha J\)。定义

\[
s(E)=\mathbf1^\top E\mathbf1,\quad
r(E)=E\mathbf1,\quad
c(E)=E^\top\mathbf1.
\]

则

\[
Dp(A_0)[E]
=(L-1)!\alpha^{L-1}s(E),
\]

以及

\[
D^2p(A_0)[E,F]
=(L-2)!\alpha^{L-2}
\left[
 s(E)s(F)-r(E)^\top r(F)-c(E)^\top c(F)+\langle E,F\rangle_F
\right].
\]

这一引理同时支持 full-rank、rank-deficient 和 rectangular Wick theorem。

## 3. 参数化 Hessian 与函数空间 Hessian

塌缩点具有重复 factors，因此参数化映射

\[
\Phi(W)=\prod_a w_a^\top x
\]

的微分具有大核。参数空间 Hessian 包含两部分：

\[
D^2(\tfrac12\|\Phi(W)-\tau\|^2)
=
D\Phi^*D\Phi
+
\langle \Phi(W)-\tau,D^2\Phi\rangle.
\]

第一项是 Gauss--Newton 项；第二项由非零 residual 与参数化二阶曲率产生。正是第二项使一些一阶不可见方向成为严格 saddle directions。

## 4. 关键校正

v0.2 的 raw 方阵公式中存在一个排版控制字符错误：

```text
1-\frac{2(L-1)^2}{L(2L-1)}
```

曾被错误渲染。本阶段已在英文 note、中文证明与代码中统一修复。

此外，矩形 raw 不能通过把方阵 multiplicity 机械替换为 \(d-1\) 得到。ambient collective 与 ambient specialization 的曲率分别为

\[
(L-1)k_L,
\qquad
-\frac{L-1}{2L-1}k_L,
\]

不同于 teacher-span 内部的

\[
2(L-1)k_L,
\qquad
-\frac{3L-2}{2L-1}k_L.
\]

这一差异已由完整 quadratic form 和自动微分谱审计共同确认。
