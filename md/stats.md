$\def\rarrow{ \rightarrow}$
$\def\R{\mathbb{R}}$
$\def\finv{f^{-1}}$

# Probability
* $P(A) = u(A)$
* $P(A \cup B)$, when $A,B$ disjoint, is $u(A)+u(B)$
* $P(A|B) = \dfrac{P(A \cap B)}{P(B)}$

* $P(B|A) = \dfrac{P(A \cap B)}{P(A)} = \dfrac{P(A|B)*P(B)}{P(A)}$

# GOMO
* Expand sample size of higher up nodes?
  * tried (N*.2)**2*100



# Prob Basics
* Probability Space $(\Omega, F, P)$
  * outcome :=  a single result from a single experiment run
  * event := set of outcomes
  * $\Omega$ := set of all outcomes
  * $F$ := set of all events, a sigma algebra
  * $P$ Measure on $P: F \rarrow [0,1]$
* measurable function: function between two underlying sets of two measurable spaces that preserve structure of two spaces
    * let $(\Omega, \Sigma)$ $(R,B)$ be measurable spaces Set of outcomes and Set of all events, sigma algebra
    * $f: \Omega \rarrow R$ is measurable if for every $E \in B$, $\finv(E) \in \Sigma$

* Random variable
  * is a measurable function from probability space to measure space, (called sample space)
    * $X:\Omega \rarrow R$


