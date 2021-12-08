

*  $\char"10003$
* Things to look
  * Examples
  * All Connections
  * Write as little as you can to describe the most you wish
  * Order
 
* Common themes
  * Operation between two objects
    * Identity
    * Associative
    * Commutative
  * Relation between two objects
    * Identity
    * Reflexive
    * Transitive
  * Specific object

Consider $f$ and $A$ and $f(A)$. What is the identity? Can there always be an inverse? 
No, consider $f(x)=x^2$ and $ A = \{ 0 < x < 1 \}$. We see that $f^{-1}(f(A)) = \{ -1 < x < 1 \}$. 
What condition can guarantee that you can always find an inverse?
From a new idea, how many more ideas can be formed in combination with existing ideas?
Set of existing ideas = [ identity, inverse, transitive, union, intersection, equality, less than or equal, subset ]


# Boolean Logic
Statements that are True or False
When we write 
* $A$, means $A$ is true
* $\lnot A$ means $A$ is false
* $A \land B$ means $A$ and $B$ is true
* $A \lor B$ means $A$ or $B$ is true
* $A \rightarrow B$ means $\lnot A$ or $B$ is true

# 1.1 Sets and Functions

## DEF Set
* $A$ a set is a collection of objects
* $a \in A$ if the element $a$ is in A
* $A \subset B$ if B contains all the elements of A
* $A = B$  if they contain the same elements
* $ \cup \cap \setminus $ are binary operations  $S \times S \rightarrow S$
* $ \varnothing $

## PROPERTIES Set
* $ A \cup (B \cap C) = (A \cup B) \cap (A \cup C) $
* $ A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
* $ ( A \cup B )^c = (A^c \cap B^c) $
* $ ( A \cap B )^c = (A^c \cup B^c) $
* $ A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$
* $ A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$

## DEF Function
* Mapping from a set $A$ to $B$
* Such that an element of $A$ maps to exactly one element in $B$

# 1.2 Mathematical Induction


# 1.3 Finite and Infinite Sets

## THM 1.3.2 Cardinality of a finite set is unique
* Given $A \subset B$ it is not possible to form a bijection from B to A

## THM 1.3.3 $\mathbb{N}$ is infinite set
## THM 1.3.4 Cardinality and Set operations
* Cardinality of finite members are preserved under disjoint union and set difference by a subset
* Cardinality of infinite finite sets 
* ? inf<x contrapositive to x<fin ?
  * Lets see how to contrapositive flips within the argument

## THM 1.3.5 $T \subset S$
* Conclusion (finite/infinite) drawn about one set from another set based on ordering

## DEF denumerable - bijection to N, countable - finite or denum, uncountable - not countable

## THM 1.3.8 $N \times N$ is denumerable
* You have comeup with an interesting function. How to show 

>! $N(a,b) = b + sum_prev_diags$
>! $diag(a,b) = a+b-1 = d$
>! we know $b  \leq diag(a,b) $
>! if diag is same, then it is clear N is injective
>! suppose diag is different, let diag2 bigger than diag1 so $b1 < diag1 < diag2$
>! $b1+diag0..1 = b2 + diag0..1+diag1..2$
>! $b1 = b2 + diag1..2 > diag2$ contradiction
>! b1 cannot make up for the distance btw two diff diagonals

## THM 1.3.9 $T \subset S$
* Conclusion (countable/uncountable) drawn about one set from another set based on ordering

## THM 1.3.10
* Illustration on using the various properties of sets and bijections and subsets and it's effect on countable uncountable

## THM 1.3.11 Rational numbers are countable

# 2.1 The Real Numbers

## 2.1.1-2.1.3 Algebraic properties of field R
* Uniqueness of 1,0, inverse
* 0*a = 0
* a*b = 0 means one must be 0

## 2.1.4 $\sqrt{2}$ is irrational

## Order of $\mathbb{R}$
* Defined in terms of positive number
* Relation
 
## 2.1.7 Properties of order on R
* if $a>b$ and $b>c$ then $a>b>c$ Transitive
* if $a>b$ then $a+c>b+c$
* if $a>b$ and $c>0$ then $ca>cb$
* if $a>b$ and $c<0$ then $ca<cb$


## No smallest positive real number can exist

## 2.1.9 Thm
If $0 \geq a \gt e \forall e \gt 0$ then $a=0$
## 2.1.10 Thm
If $ab>0$ then $a>0$ $b>0$ or $a<0$ $b<0$

## Remark: Arithemetic-Geometric mean
* $\sqrt{ab} \leq \dfrac{1}{2}(a+b)$
* $(a_1 a_2 ... a_n)^{1/n} \leq \dfrac{1}{n}(a_1+a_2+..+a_n)$

## Remark: Bernoulli's Inequality
* If $x > -1$ then $(1+x)^n \geq 1+nx$ for all $n \in \mathbb{N}$

# 2.2 Absolute Value and Real Line

## Definition of ABS
## Properties of ABS
* Why are certain properties important?
* Usually when some property is given in a book, it is there for a reason
* What are equivalent statements with this new definition?

## 2.2.3 Triangle Inequality 
* $|a+b| \leq |a|+|b|$

## 2.2.4 Corallaries of Triangle Inequality
* $| |a|-|b| |<|a-b|$
* $|a-b|<|a|+|b|$

## 2.2.5 Triangle Inequality for N sums 
* $|a_1 + a_2 + ... + a_n| \leq |a_1|+|a_2|+ ... +|a_n|$

## 2.2.7 E neighborhood
* e neighborhood of $a \in \mathbb{R}$ is the set $V_e(a) := \{ x \mid |x-a| < e \} $

## 2.2.8 if x is in every e neighborhood of a then x is a

## 2.2.9

# 2.3 Completeness Property

## Def 2.3.1 Bounded above, below, bounded sets
* Given an subset, $S$, of $\mathbb{R}$ it is bounded if ...

## Def 2.3.2 Suprememum Infimum
* Supremum least upperbound 
  * if u is upper bound of $S$, then $sup S \leq u$
* Infimum greatest lowerbound

## Remark: uniqueness of suprememum infimum
## Remark: Consider the contrapositive of least upper bound condition of definition of suprememum
## Lemma 2.3.3
* What is smaller than supremum is not a upper bound
  * Why is this lemma here?
## Lemma 2.3.4
* Upperbound u is supremum iff $\forall e > 0$ there exists $s_e \in S$ sutch that $u-e < s_e$
## 2.3.6 Completeness Property of R
* Every nonempty set of real numbers that has upper bound has a supremum in $\mathbb{R}$

## Lets break down definition supremum
* $sup S$ is a upper bound of $S$
* if u is upper bound of $S$, then $sup S \leq u$
* What are the inputs that define supremum? (S set)
* What are the output of the definition? (real value)
* Can anything other than input output influence or server some connection?
