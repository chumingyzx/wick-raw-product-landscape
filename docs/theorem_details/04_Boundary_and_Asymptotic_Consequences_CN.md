# 边界退化与渐近后果

## 1. Rank-one teacher boundary

对

\[
T_\rho=(1-\rho)I+\rho J,
\qquad -\frac1{L-1}<\rho<1,
\]

full-rank 区域内：

\[
\gamma=1+(L-1)\rho,
\qquad
\mu=1-\rho.
\]

全部 specialization eigenvalues 为

\[
-(1-\rho)(L-2)!
\left(\frac{1+(L-1)\rho}{L}\right)^{L-2}.
\]

当 \(\rho\uparrow1\) 时，它们连续趋于 0；但在所有 \(\rho<1\) 上，Morse index 仍为 \((L-1)^2\)。到达 \(\rho=1\) 后 teacher rank 突然变为 1，index 变为 0，nullity 跳升至 \(d(L-1)\)。

因此这是一个由 teacher-rank degeneration 控制的 singular boundary，而不是普通非退化 Morse critical point 的连续移动。

## 2. 弱曲率的阶数

正交 Wick specialization curvature：

\[
a_L=\frac{(L-2)!}{L^{L-2}}
\sim\sqrt{2\pi L}e^{-L}.
\]

raw teacher-span specialization curvature：

\[
\left|\lambda_{\rm teacher,spec}^{\rm raw}\right|
\sim6\sqrt2\pi L(2e)^{-L}.
\]

raw ambient specialization curvature：

\[
\left|\lambda_{\rm ambient,spec}^{\rm raw}\right|
\sim2\sqrt2\pi L(2e)^{-L}.
\]

所以 raw 模型拥有更多严格负方向，但每个新 ambient 方向仍然是指数弱曲率。

## 3. 不能仅凭 index 判断 escape difficulty

- Wick square model：负方向数 \((L-1)^2\)，单方向曲率约 \(e^{-L}\)。
- Raw rectangular model：负方向数 \((d-1)(L-1)\)，其中额外 ambient directions 的曲率约 \((2e)^{-L}\)。

因此更大的 saddle index 可以与更慢的局部 deterministic escape 同时出现。完整优化结论仍需 nonlinear invariant neighborhood、噪声协方差和初始化投影，而不能由 Hessian inertia 单独推出。
