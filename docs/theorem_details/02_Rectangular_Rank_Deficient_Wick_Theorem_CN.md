# 矩形与秩亏 Regular-Teacher Wick 谱定理

## 设置

令

\[
U\in\mathbb R^{d\times L},
\qquad
T=U^\top U\succeq0,
\qquad
T\mathbf1=\gamma\mathbf1,
\quad \gamma>0.
\]

记

\[
r=\operatorname{rank}T=\operatorname{rank}U.
\]

在 \(\mathbf1^\perp\) 上，设 \(T\) 的正特征值为

\[
\mu_1,\ldots,\mu_{r-1}>0,
\]

其余 \(L-r\) 个特征值为 0。定义

\[
W_\star=\frac1L UJ,
\qquad
b=(L-2)!\left(\frac\gamma L\right)^{L-2}.
\]

## 完整谱

| 扇区 | 特征值 | 重数 |
|---|---:|---:|
| Radial | \(L(L-1)\gamma b\) | 1 |
| Gauge | \(0\) | \(L-1\) |
| Teacher collective \(i\) | \((L-1)(\gamma+\mu_i)b\) | 每个 \(i\) 一个 |
| Teacher specialization \(i\) | \(-\mu_i b\) | 每个 \(i\) 重复 \(L-1\) |
| Ambient collective | \((L-1)\gamma b\) | \(d-r\) |
| Ambient null | \(0\) | \((d-r)(L-1)\) |

所以

\[
\operatorname{index}=(r-1)(L-1),
\]

\[
\operatorname{nullity}=(d-r+1)(L-1),
\]

\[
n_+=d.
\]

## 扇区分解

令

\[
e=\frac{\mathbf1}{\sqrt L},
\qquad
p_0=\frac{Ue}{\sqrt\gamma}.
\]

对每个正 \(\mu_i\)，取

\[
Tq_i=\mu_iq_i,
\qquad
p_i=\frac{Uq_i}{\sqrt{\mu_i}}.
\]

再令 \(n_a\) 为 \(\operatorname{col}(U)^\perp\) 的正交基。参数空间由

\[
p_0e^\top,
\quad p_0q_j^\top,
\quad p_ie^\top,
\quad p_iq_j^\top,
\quad n_ae^\top,
\quad n_aq_j^\top
\]

正交张成。将这些方向代入 permanent 二阶变分，双线性项在该基上对角化，即得到上表。

## 两个边界

### Rank-one boundary

当 \(r=1\) 时，\(T=(\gamma/L)J\)，所有 teacher factors 相同，且 \(W_\star=U\)。此时

\[
\operatorname{index}=0,
\qquad
\operatorname{nullity}=d(L-1),
\qquad
n_+=d.
\]

### Zero-row-sum boundary

当 \(\gamma=0\) 时，PSD 性质推出 \(U\mathbf1=0\)，塌缩点为 \(W=0\)。对任意方向 \(H\)：

\[
\mathcal L(tH)-\mathcal L(0)
=-t^L\operatorname{perm}(H^\top U)
+\frac12t^{2L}\operatorname{perm}(H^\top H).
\]

因此对 \(L\ge3\)，gradient 与 Hessian 都完全为零；局部性质必须由第 \(L\) 阶项判断。
