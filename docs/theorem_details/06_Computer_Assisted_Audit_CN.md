# Computer-Assisted Audit

## 1. 审计原则

代码不承担证明，而用于检查：

- 临界点 gradient 是否为 0；
- 完整自动微分 Hessian 的 eigenvalues 是否与 closed form 一致；
- inertia multiplicities 是否一致；
- raw quadratic form 是否逐方向一致；
- 边界高阶恒等式是否逐点成立。

## 2. 审计结果

| 审计 | 单元数 | 最大误差 | Mismatch |
|---|---:|---:|---:|
| Rectangular/rank-deficient Wick full spectrum | 22 | \(7.15\times10^{-14}\) | 0 |
| Rank-one Wick boundary spectrum | 8 | \(2.05\times10^{-12}\) | 0 |
| \(\gamma=0\) exact high-order identity | 60 | \(4.46\times10^{-13}\) | 0 |
| Rectangular raw full spectrum | 9 | \(2.66\times10^{-15}\) | 0 |
| Raw quadratic-form directions | 72 | \(8.88\times10^{-15}\) | 0 |
| Analytic inertia formulas | 242 | exact integer check | 0 |

rank-one boundary 的绝对误差略大，原因是正特征值随 \(L\) 迅速增长，仍处于双精度自动微分的相对舍入范围内。

## 3. 独立性

- closed form 位于 `src/theory.py`；
- population loss 与 automatic Hessian 位于 `src/audit.py`；
- raw student norm 通过 Gaussian perfect-matching recursion 独立计算；
- permanent 通过 differentiable Ryser formula 计算；
- tests 只检查解析 multiplicities、输入契约与基本恒等式。
