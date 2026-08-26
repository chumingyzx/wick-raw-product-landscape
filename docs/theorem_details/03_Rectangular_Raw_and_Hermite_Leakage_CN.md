# 矩形 Raw Gaussian 谱与 Hermite-Leakage Index Inflation

## 设置

令 \(U\in\mathbb R^{d\times L}\) 满足

\[
U^\top U=I_L,
\qquad d\ge L,
\]

teacher 为

\[
\tau_U(x)=\prod_{i=1}^L u_i^\top x,
\qquad x\sim\mathcal N(0,I_d).
\]

记

\[
m=U\mathbf1,
\qquad
W_\star=c_Lm\mathbf1^\top,
\]

其中

\[
c_L^L
=\frac{L!}{L^L(2L-1)!!}
=\frac{2^L(L!)^2}{L^L(2L)!},
\]

以及

\[
k_L=(L-2)!c_L^{L-2}.
\]

## 完整 quadratic form

令

\[
P=UU^\top,
\quad
r=H\mathbf1,
\quad
q=H^\top m,
\quad
s=m^\top H\mathbf1.
\]

则

\[
\begin{aligned}
\frac{D^2\mathcal R(W_\star)[H,H]}{k_L}
&=
\left[\frac{4(L-1)^2}{L(2L-1)}-1\right]s^2\\
&\quad+\frac{2(L-1)}{2L-1}\|r\|^2+\|Pr\|^2\\
&\quad+\frac{3L-2}{L(2L-1)}\|q\|^2\\
&\quad-\frac{L-1}{2L-1}\|H\|_F^2-\|PH\|_F^2.
\end{aligned}
\]

## 完整谱

| 扇区 | 特征值 | 重数 |
|---|---:|---:|
| Radial | \(L(L-1)k_L\) | 1 |
| Gauge | \(0\) | \(L-1\) |
| Teacher collective | \(2(L-1)k_L\) | \(L-1\) |
| Teacher specialization | \(-\dfrac{3L-2}{2L-1}k_L\) | \((L-1)^2\) |
| Ambient collective | \((L-1)k_L\) | \(d-L\) |
| Ambient specialization | \(-\dfrac{L-1}{2L-1}k_L\) | \((d-L)(L-1)\) |

所以

\[
\operatorname{index}_{\rm raw}=(d-1)(L-1),
\]

\[
\operatorname{nullity}_{\rm raw}=L-1,
\qquad
n_{+,\rm raw}=d.
\]

## Hermite leakage

同一个正交 teacher 的 Wick 模型具有：

\[
\operatorname{index}_{\rm Wick}=(L-1)^2,
\]

\[
\operatorname{nullity}_{\rm Wick}=(d-L+1)(L-1).
\]

raw 模型增加的负方向数量精确为

\[
(d-L)(L-1).
\]

这些方向恰好是

\[
\operatorname{col}(U)^\perp\otimes\mathbf1^\perp.
\]

在 Wick top-chaos metric 下，它们是一阶与二阶均不可见的 Hessian-null directions；raw student self-moment 中的 lower-Hermite contractions 将其提升为严格负方向。

因此，删除或保留 lower-order Gaussian contractions 不只是重新缩放同一个 Hessian：它会改变 Hessian 的 inertia。
