* _Things_ to look
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

# Language

* Use of language in math
  * https://assets.press.princeton.edu/chapters/gowers/gowers_I_2.pdf

# Boolean Logic
* Statements that are True or False
* When we write 
* $A$, means $A$ is true
* $\lnot A$ means $A$ is false
* $A \land B$ means $A$ and $B$ is true
* $A \lor B$ means $A$ or $B$ is true
* $A \rightarrow B$ means $\lnot A$ or $B$ is true

# Negation
* A and !A
* When introduced to a new definition, do consider the negation as part of the elements you must permute to see the connections

## Implication and Contrapositive

>! * A -A  B -B  A->B  C
>! * F  T  F  T   T    T
>! * F  T  T  F   T    T
>! * T  F  F  T   F    F
>! * T  F  T  F   T    T

>! * A Truth table is a table of the domain and range of statement values
>! * Two statements are equivalent when they are the same function

>! * The implication is interesting because it *correlates* A and B in a way

* When we write $f(A,B),$ we mean $f(A,B)=true$
* To prove $f(A,B)=true$, we need to plug in all variables to see if it is constant

* To prove $A \rightarrow B = true$
  * 1 if $A$ is false $A \rightarrow B = true$
    * This means we only need to be concerned with the case where $A$ is true.
  * 2 if $A$ is true $A \rightarrow B = true$ only when $B$ is true, requiring us to show $B$ is true (This links A and B/that B can never be false when A is true)
    * This also mean when $B$ is false, $A$ must also be false because otherwise $A \rightarrow B = False$

* From this relationship can we draw another implication (which satistfies 1&2)?
  * To show an implication is true, we only need to be concerned with when hypothesis is true
  * $!B \rightarrow !A$


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

# 2.1 Algebraic and order properties of R

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

## 2.4.7 Sqrt of 2 is real number
* $ \ sqrt{2}$ is a real number
>! * This is a consequence of the Supremum property of $\mathbb{R}$
>! * Can show 

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

>! I started off with a diagram and realized, hey maybe the distance between the 2 different limits,(A,B), will show that the sequence will have to exist in 2 impossible places 
>! It came more down to if the sequence is within 1 limit V_e(A), it cannot be in the other V_e(B)

* Let $m$ be the point where $|A-s_m| < e$ and $|B-s_m| < e$ for $e = \dfrac{|B-A|}{2}$
* $ |B-A| = |B-s_m+s_m-A| \leq |B-s_m| + |A-s_m| < \dfrac{|B-A|}{2} + \dfrac{|B-A|}{2} = |B-A| $

## 3.1.5 Explanation of Convergence of Limits in terms of Neighborhoods

## 3.1.8 DEF Tail of a Sequence
* Given a sequence, $X = (x_1, x_2,...)$, the m-tail of X is a sequence, $(x_m, x_{m+1}, ...)$
* We denote this as $X_m$

## 3.1.9 THM Tail of a Sequence has same limit as sequence
* for all epsilon, the tail or the original sequence will give an value that will guarantee $|L-x_i|<e$

## 3.1.10 THM
* Let $x_n$ be a sequence. If $(a_n)$ converges to $0$ and $|x_n -x| \leq a_n$ then $(x_n)$ converges to $x$
* Not a big fan of theorem. (using a another sequence to show a sequences converges)
* I think one can build a more constructive approach with smaller theorems (see below)
  * With application of Squeeze Theorem
    * Lim(|x_n-x|)=0
  * $Lim(|x_n-x|) = 0 \rightarrow Lim(x_n-x)=0 \rightarrow Lim(x_n)=x$
    * This shows $Lim(x_n)=x$

# 3.2 Limit Theorems

## 3.2.0 Introduction
* Develop techniques to expand the collection of convergent sequences
* Find more examples

## 3.2.1 DEF Bounded sequence
## 3.2.2 THM Convergent sequence implies bounded

* Suppose $Lim(s_n) = s$
* $(s_n)$ is bound in $V_e(s)$ for $i > K(e)$ 
* Clearly we can find a bound for elements $\{ s_1, s_2, ... , s_{K(e)} \}$
* Merge these two bounds for a bound for all of $(s_n)$.
  * Let $B1$ be bound for set $A$. Let $B2$ be bound for set $B$.
  * Merge of $B1$ and $B2$ gives bound for $A \cup B$

## 3.2.3 THM Real number operation on sequences and limit
* __TODO__: sum, diff, constant mult
* mult: if $(x_n)$ and $(y_n)$ are convergent then $(x_n * y_n)$ converges to $x*y$
  * $|xy-(x_n)(y_n)| = |xy -(x_n)y + (x_n)y -(x_n)(y_n)| \leq |xy -(x_n)y| + |(x_n)y -(x_n)(y_n)| \leq |y||x - (x_n)| + |x_n||y - (y_n)|$
  * $|y||x - (x_n)| \leq \dfrac{e |y|}{2}$
  * $|x_n||y - (y_n)| \leq \dfrac{e (e+|x|)}{2}$
    * $|x_n| - |x| < |x_n - x|< e$
    * $|x_n| <  e + |x|$
  * $|y||x - (x_n)| + |x_n||y - (y_n)| \leq e/2+e/2 = e$
* div

## 3.2.4 THM order on sequence corresponds to order on limit
* if $(x_n) \geq 0$ then $Lim(x_n) \geq 0$

## 3.2.5 THM Inequality is preserved for sequences and their limits
* $(x_n) \leq (y_n) \rightarrow Lim(x_n) \leq Lim(y_n)$
* Can show $(x_n) > (y_n)$ is not true if $Lim(x_n) > Lim(y_n)$ because we can select neighborhoods of $x$ and $y$ s.t all elements of the neighborhood will $V_e(x) > V_e(y)$

## 3.2.6 LEMMA 
* $ (z_n) \leq (x_n) \leq (y_n) \rightarrow Lim(x_n) \leq Lim(x_n) \leq Lim(y_n)$
 

## 3.2.7 THM Squeeze Theorem
* If $(z_n) \leq (x_n) \leq (y_n)$ and $L = Lim(z_n) = Lim(y_n)$ then $Lim(x_n)$ exists and is equal to $L$
* If $z_n$ and $y_n$ are found within $V_e(L)$ then $x_n$ is also in this neighborhood
* This means that for $i > min( Ky(e), Kz(e) )$,  $x_i$ will be in the $V_e(L)$

## 3.2.8 Examples of non convergent sequences
* Not bounded
pg75

## 3.2.9 Convergence and abs
* If $Lim(x_n) = x \rightarrow Lim(|x_n|) = |x|$

>! * $ | x_i - x|<e $
>! * $ | |x_i| - |x| |<e $
>! * $(\dag)$ Can we show $ | |x_i| - |x| | < | x_i - x|$?
>! * ---------------------
>! * I got quite dissatistfied  after looking at this proof and demotivated
>! * I think the reason is it doesn't really explain why or arrive at the solution in a natural/discoverable way
>! * I think when I am not satisfied with a proof or an explanation, I should really dig deeper and analayze it closer
>! * But at the same time not let it get the best of me.
>! * Don't be results driven
>! * --------------------------
>! * Below is the aforementioned neat proof from a book
>! * $|b| = | b - a + a | < |b-a| + |a|$
>! * $|b| - |a| < |b-a|$
>! * $|a| = | a - b + b | < |b-a| + |b|$
>! * $|a| - |b| < |b-a|$
>! * $|b| - |a| > -|b-a|$
>! * --------------------------
>! * Useful Lemmas
>! * Keep in mind these two properties of absolute value. $|-x| = |x|$ and if $b<0 -b = |b|$
>! * How to show $a>|b|$ iif $a>b$ and $a>-b$
>! * --------------------------
>! * Continuing from $(\dag)$
>! * 1 Consider $|a-b|$ if $a$, $b$ have same sign. Then it is clear $|a-b| = | |a|-|b| |$
>! * 2 Suppose they do not have the same sign and let $b<0$ then $|a-b| = | a+|b| | = |a|+|b|$
>! * $|a|+|b| >= |b|-|a|$ and $|a|+|b| >= |a|-|b|$ so $|a-b| = |a|+|b| > ||a|-|b||$

## 3.2.10 Convergence and sqrt
* If $(x_n)$ converges to $x$ then $(\sqrt{x_n})$ converges to $\sqrt{x}$
  * $x_n$ is a positive sequence
* $e \geq x-x_n = (\sqrt(x)-\sqrt(x_n))(\sqrt(x)+\sqrt(x_n)) \geq (\sqrt(x)-\sqrt(x_n))$

## 3.2.11 Convergence and ratio

* if $Lim(\dfrac{x_{n+1}}{x_n}) = r < 1$ and $x_n > 0$ then $Lim(x_n)=0$
  * $\dfrac{x_{n+1}}{x_n}-r <  + e$
    * choose $e,$ st $r+e < 1$
  * $\dfrac{x_{n+1}}{x_n} < r < r + e < K < 1$
  * $y_1 = x_{n+1} < K * x_n$
  * $y_i = x_{n+i} < K^i * x_n$
  * if we can show Lim(K^n) = 0
    * $Lim(a*K^n) = a*0 = 0$

>! * if a=b x<y then a+x<b+y 
>! * Show for K<1 Lim(K^n)=0
>! * We note that if $K<1$ then there is $a,b$ s.t $K<\dfrac{a}{b}<1$
>! * Let use try to show $Lim( (a/b)^n ) = 0$
>! * -
>! * pick $0 < 1/r < t/r < e$
>! * $1/r < a/b$
>! * lets forget about a 
>! * why is proving something about the smallest element often involve inspecting the largest element
>! * its basically showing b^x is unbounded for any integer b>0
>! * consider the set of all multiples of b less than M
>! * produce the largest or smallest element, the boundary case right before
>! * -
>! * Lemma: $(\dfrac{1}{b}^{n})$ for $ n \in \mathb{N}$ converges to 0
>! * We will show for all $E>0$ there is $m$ s.t. $\dfrac{1}{b}^{m} < \dfrac{1}{r} < E$
>! * 1 Suppose this is not the case and there is a lower bound for all elements of $\{\dfrac{1}{b}^{n}\}$ this is equivalent to the following 2
>! * 2 Suppose there is an upper bound for $\{b^n\}$. Then, it has supremum call it $S$
>! * then there is $S-e = S/\sqrt{b} < b^x <=S$
>! * This means $b^{x+1} > b*S/\sqrt{b} = \sqrt{b}*S > S$ which is a contradiction



## EX 3.2.21 
* if $|x_n - y_n| <e$
* transitivity property
* $a-b<e$, $b-c<e$, $a-c<2e$
* $R(a,b) = |a-b| < e$
  * What properties does this relation have?
  * reflexive, transitive, identity, 
  * $R(a,b) = R(a-b,0)$
  * $R(a,b) + R(0,c) = R(a,b+c) = R(a+c,b)$

# 3.3 Monotone Sequences

## 3.3.0 Introduction
* Develop techniques to show sequence is convergent even if the value is not known
* Evaluate the limit by other methods once it is known

## 3.3.1 DEF monotone sequence
* Let $(x_n)$ be a sequence
  * If $i>j$ then $x_i \geq x_j$, we say $(x_n)$ is increasing
  * If $i>j$ then $x_i \leq x_j$, we say $(x_n)$ is decreasing
  * $x_n$ is monotone if it is increasing or decreasing

## 3.3.2 THM Monotone sequence is convergent 
* increasing sequence is convergent
  * Converges to the supremum
* decreasing sequence is convergent
  * Converges to the infimum

## 3.3.5 Sequence that converges to sqrt 2
* $x_1=1$ $x_{n+1} = 2/x_{n}$
* Then limit of $x_n$ is equal to limit of $x_{n+1}$ (lim of tail of sequence is equal to lim of sequence)
* $x = 2/x \rightarrow x^2 = 2$
* The issue is that this sequence is not monotone nor we know it converges
  * Can you find a monotone bounded sequence, that when limit is taken between the tail and 

## 3.3.6
* Euler's number
* $e_n = (1+1/n)^n$
* __TODO__: Look into more detail

# 3.4 Subsequences and Boltzano Weistrauss

## 3.4.1 DEF Subsequence
* Let $(x_n)$ be a sequence
* Given $n_1 < n_2 < n_3$ ..., $(x_{n_1} , x_{n_2}, x_{n_3},...)$ is a subsequence of $(x_n)$

## 3.4.2 THM Sequence convergence and subsequence convergence
* If a sequence $(x_n)$ converges to $x$, then any subsequence converges to $x$

## 3.4.4 THM TFAE
* $(x_n)$ does not converge to $x$
* There is a $e$ where there always is unending $x_n \not\in V_e(x)$
  * For all $M$, there is $n>M$ and $P$ is false
* There is $e$ and a subsequence that lies outside of $V_e(x)$

## 3.4.5 Divergence Criteria
* $(x_n)$ has two subsequences whose limits are not equal. Then $(x_n)$ is divergent
  * All subsequences of convergent sequence must converge to same limit
* $(x_n)$ is not bounded

## 3.4.6 THM Monotone Subsequence
* A $(x_n)$ sequence has a monotone subsequence
* Let $x_a$ be the first element where for all $x_a > x_i$ for $a<i$
  * And let them be $\{ x_a, x_b, ... \} = S$
  * If there are no such elements of $S$, we can construct an increasing sequence since for any x_a there is some x_a<x_i
  * If there are finite elements of $S$, we can work with subsequence which starts with last element of S
  * If there are infinite elements of $S$, the elements of $S$ a form a decreasing sequence

## 3.4.7 THM Bounded sequences has convergent subsequence
* Every sequence has a monotone subsequence
* PF1: This monotone subsequence is bounded because the sequence is bounded
  * Bounded monotone sub sequence is convergent
* PF2: Nested Intervals based Theorem? _TODO_
  * let sequence be bound from 0 .. M (Since x_n is bounded can easily add a constant to sequence to adjust)
 
## 3.4.9 THM  Boltazno Weistrauss
* Let $(x_n)$ be a bounded sequence. If every convergent subsequence of $(x_n)$ converges to $x$, then $(x_n)$ converges to $x$
* Suppose $(x_n)$$ doesn't converge to $x$ then there is $e$ where for all $N$ there is some $x_i \not\in V_e(x)$
  * These elements has a convergent subsequence and it must converge to x. But all the elements lie outside $V_e(x)$

# 3.5 Cauchy Criterion
