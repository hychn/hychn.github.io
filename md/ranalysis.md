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

* Why are certain properties important?
* Usually when some property is given in a book, it is there for a reason
* What are equivalent statements with this new definition?

>! Consider $f$ and $A$ and $f(A)$. What is the identity? Can there always be an inverse? 
>! No, consider $f(x)=x^2$ and $ A = \{ 0 < x < 1 \}$. We see that $f^{-1}(f(A)) = \{ -1 < x < 1 \}$. 
>! What condition can guarantee that you can always find an inverse?
>! From a new idea, how many more ideas can be formed in combination with existing ideas?
>! Set of existing ideas = [ identity, inverse, transitive, union, intersection, equality, less than or equal, subset ]

# Boolean Logic
* Statements that are True or False
* When we write 
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

## DEF 1.3.1 Finite Infinite
* A set is finite iff there is a bijection between the set and $\{1...n\} n \in \mathbb{N}$

## THM 1.3.2 Cardinality of a finite set is unique
* Given $A \subset B$ it is not possible to form a bijection from B to A

## THM 1.3.3 $\mathbb{N}$ is infinite set
## THM 1.3.4 Cardinality and Set operations
* Cardinality of finite members are preserved under disjoint union and set difference by a subset
* Cardinality of infinite finite sets 
>! * ? inf<x contrapositive to x<fin ?
>! * Lets see how to contrapositive flips within the argument

## THM 1.3.5 $\subset$ and conditions for Finite/Infinite
* $INF \subset S \rightarrow S$ is infinite
* $S \subset FIN \rightarrow S$ is finite
* Conclusion (finite/infinite) drawn about one set from another set based on ordering

## DEF Denumerable, countable, uncountable
* A set $S$ is denumerable - bijection from $S$ to $\mathbb{N}$
* countable - finite or denum
* uncountable - not countable

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
* $|a|$ is a function from $\mathbb{R} \rightarrow \mathbb{R}$ such that
* $a>0 |a| = a$, $a<0 |a| = -a$, $a=0 |a| = 0$ 

## 2.2.3 Triangle Inequality 
* $|a+b| \leq |a|+|b|$

## 2.2.4 Corallaries of Triangle Inequality
* $||a|-|b|| < |a-b|$
* $|a-b| < |a|+|b|$

## 2.2.5 Triangle Inequality for N sums 
* $|a_1 + a_2 + ... + a_n| \leq |a_1|+|a_2|+ ... +|a_n|$

## 2.2.7 E neighborhood
* e neighborhood of $a \in \mathbb{R}$ is the set $V_e(a) := \{ x \mid |x-a| < e \} $

## 2.2.8 if x is in every e neighborhood of a then x is a


# 2.3 Completeness Property

## Def 2.3.1 Bounded above, below, bounded sets
* Given an subset, $S$, of $\mathbb{R}$ it is bounded if ...

## Def 2.3.2 Supremum Infimum
* Supremum least upperbound 
  * if u is upper bound of $S$, then $sup S \leq u$
* Infimum greatest lowerbound

## Remark: Uniqueness of suprememum infimum
## Remark: Consider the contrapositive of least upper bound condition of definition of suprememum

## Lemma 2.3.3
* What is smaller than supremum is not a upper bound
* Contrapositive of definition of Supremum

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

# 2.4 Application of Supremum

## 2.4.1 
* $a + supS = sup\{ a+s | \forall \ in S \}$
* Suppose $a \leq b \forall a b \in A B $. Then $sup A \leq inf B$

## 2.4.2 
* $f(x) \leq g(x) \forall x \in D$ then $sup f(D) \leq sup g(D)$
* This does not guarantee $sup f(D) \leq inf g(D)$


## 2.4.3 Archemdean Property
* For any $r \in \mathbb{R}$ there is $n_r \in \mathbb{N}$ such that $r \leq n_r$
* There is no real number larger than all natural numbers

## 2.4.4 Corollary
* $S = \{ \dfrac{1}{n} | n \in \mathbb{N} \}$ then $inf S = 0$

## 2.4.7 $ \ sqrt{2} is a real number$
<! * This is a consequence of the Supremum property of $\mathbb{R}$
<! * Can show 

# 2.5 Intervals

## DEF Interval
* (a,b) := {x | a < x < b}
* (a,b), (a,b], [a,b), [a,b]
* (-inf,b), (-inf,b], (a,inf), [a,inf), (-inf,inf)

## 2.5.1 THM Characterization of Interval
* if $S$ has the property, then $S$ is an interval
*  property: if $a,b \in S$ and $a<b$ then $[ a, b ] \subset S$ 

## DEF Nested Intervals
* A sequence of intervals $I_n, n \in \mathbb{N}$ is nested if $ ... I_3 \subset I_2 \subset I_1$

## QUESTION
* Why must these intervals be index by N?
* Supremum does not require
* Does any other part require us?

## 2.5.2 THM Nested Interval Property
* If $I_n = [a_n,b_n], n \in \mathbb{N}$ is a sequence of closed bounded intervals, there is $ c \in I_n \forall n \in \mathbb{N}$

## 2.5.3 THM Uniqueness of Common Nested Interval Point
* If $I_n = [a_n,b_n], n \in \mathbb{N}$ is a sequenc of closed bounded intervals, and $inf \{b_n - a_n | n \in \mathbb{N} \} = 0$
* then $ c \in I_n \forall n \in \mathbb{N}$ is unique

## 2.5.4 Set of $\mathbb{R}$ is not countable
* Assume is countable
* $ \{x_1, x_2, ...  \} = S$
* want to find a number that is not in the set that includes all numbers
* $ c \in \forall I_n $ then make each $s \in S$ be the negation of $\in \forall I_n$

## DEF Binary representation
* A bijection?
* homorphism under addition/sub?

## 2.5.5 THM $\mathbb{R}$ is uncountable


# 3.1 Sequences and Their Limits

## 3.1.1 DEF Sequence
* Sequence in $S$ is a function from $\mathbb{N} \rightarrow \S$
* $( s_n | n \in \mathbb{N} )$
* inductively/recursively defined sequences $x_{n+1} = x_n + 5$

## 3.1.3 DEF Limit of Sequence
* $L$ is limit of sequence $(s_n)$ if $ \forall e \: \exists m $ s.t. $m<i \rightarrow |L-s_i| < e$
* If $(s_n)$ has a limit, it is convergent
* If $(s_n)$ doesn't have limit, it is divergent

>! * $Lim(s_n+x_n) = s+x$
>! * Effect of limit on s_x operated on by a constant
>! * Effect on limit on s_x operated by another sequence
>! * $s_n < x_n \rightarrow s < x$
>! * $s_i \in V_e(L)$
>! * $(s_n) is a ordered set, how about ordered subset?$
>! * Uniqueness of Limit 

## 3.1.4 Uniqueness of Limit

* Let $m$ be the point where $|A-s_m| < e$ and $|B-s_m| < e$ for $e = \dfrac{|B-A|}{2}$
* $ |B-A| = |B-s_m+s_m-A| \leq |B-s_m| + |A-s_m| < \dfrac{|B-A|}{2} + \dfrac{|B-A|}{2} = |B-A| $

## 3.1.5 Explanation of Convergence of Limits in terms of Neighborhoods

## 3.1.8 DEF Tail of a Sequence
* Given a sequence, $X = (x_1, x_2,...)$, the m-tail of X is a sequence, $(x_m, x_{m+1}, ...)$
* We denote this as $X_m$

## 3.1.9 THM Tail of a Sequence has same limit as sequence
* for all epsilon, the tail or the original sequence will give an value that will guarantee $|L-x_i|<e$

## 3.1.10 THM
* Not a big fan of this thm. I think one can build a more constructive approach (see below)
* $Lim(k-s_n) = 0 \iff Lim(s_n)=k$
* $Lim(|s_n|) = | Lim(s_n) |$
* $s_n \leq t_n \rightarrow  Lim(s_n) \leq Lim(t_n)$

## Bounded increasing sequence is convergent
* Converges to the supremum

## Bounded sequences have convergent subsequence

* Existence of an increasing or decreasing sequence in a bounded sequence
