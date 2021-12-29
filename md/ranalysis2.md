# Cauchy
## 3.5.0 Introduction
* Way to show convergence of a limit without knowing the limit
* Our goal is to show a Cauchy sequence is  equivalent Convergent

## 3.5.1 DEF Cauchy Sequence
* Sequence $(x_n)$ is a Cauchy sequence if for all $e$, there is $H$ such that if $i,j>H$ then $|x_i-x_j|<e$

## 3.5.2 THM Convergent Sequence is Cauchy
* $|x_i-L| < e/2$, $|L-x_j| < e/2$
* $|x_i-L+L-x_j| < |x_i-L|+|L-x_j| < e/2+e/2$

## 3.5.3 THM Cauchy sequence is Bounded
* Let $x_n$ be our sequence, consider e. Then for $i,H+1>H$, $x_i \in V_e(x_{H+1})$
* So the sequence's bounds can be determined by {x_1,...x_H, x_{H+1}+e, x_{H+1}-e }

## 3.5.4 THM Cauchy sequence is Convergent
* We have shown cauchy sequence is bounded so it has a convergent subsequence $(x_{s_n})$
* Suppose this subsequence converges to $L$
* Then for any $e/2$ we can find $K$ such that $i>K |L-x_{s_i}| < e/2$
* Also since the sequence is cauchy we can find H such that for $i,k>H$ $|x_{i}-x_{k}|<e/2$
* Let X be max(K,H) and both these conditions hold true
* $|L-x_{k}|<|L-x_{s_i}|+|x_{s_i}-x_{k}|< e$


