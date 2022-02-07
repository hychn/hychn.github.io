$ \def\lim#1#2{ \underset{#1 \rightarrow #2}{lim} }$

# 1 Preliminaries

# 1.1 Sets and Functions
* DEF: Function
* DEF: Injective
* DEF: Surjective

# 1.2 Boolean Logic
* DEF: Negation
* DEF: And
* DEF: Or
* DEF: _Implication_ a
>! * aVb = V(a,b) = T means a,b can take on the values of V^{-1}(T)
>! * Two functions are equal if 
>! * a statement/function is equal to another statement with same domain when all variation of inputs gives same output
>!  * Can two statements that do not have the same input be equal to another?
>! * Truth table a b a->b
>! * Intersection of rows of truth table?
>! * a->b and !b->!a
>!   *   (a,b) (F,T) (F,F) (T,T)
>!   * (!a,!b) (T,F) (T,T) (F,F) Almost same except for reversal of (T,F)

# 1.3

# 2 The Real Number

# 2.1 Algebraic and Order Properties of R
* DEF: Operator $+ *$ binary function from, to $\mathbb{R}$
* PRP: $a+b = b+a$
* PRP: $(a+b)+c = a+(b+c)$
* PRP: $a*(b+c) = a*b + a*c$
* DEF: special elements 0,1 wrt binary functions
  * $a+0=a$, $a*1=a$
  * $a+-a=0$, $a*\dfrac{1}{a}=1$
* PRP: uniquness of 0,1
* DEF: Order $a \leq b :=$ b-a is positive or zero 
* PRP: Reflexive $a \leq a$
* PRP: Transitive $a \leq b$ $b \leq c$ $\rightarrow a \leq c$
* REM: Negation $b \leq a$
>! * TFAE
>! * $b \leq a$
>! * a-b is positibe or zero
>! * b-a is negative or zero

# 2.2 ABS and Real-Line
* DEF: $|a| = \begin{cases} a>0: a \\ a=0: 0 \\ a<0 : -a  \end{cases}$

# 2.3 Completeness Property of R
* AXM: upper bounded subset of $\mathbb{R}$ has a least upper bound

# 2.4 Applications of Supremum

# 2.5 Intervals

# 3 Sequences

# 3.1 Sequences and Their Limits
* DEF: Sequence
* DEF: Limit
>! * The limit of sequence $(x_n)$ is $L$ if: for any $e>0$,$\exists k$ s.t. $i>k \rightarrow |x_i-L|<e$
* PRP: convergent sequence implies bounded
* DEF: Negation of convergence to L
>! $\exists e>0$ s.t. $\forall k \neg (i>k \rightarrow |x_i-L|<e)$
>! $\exists e>0$ s.t. $\forall k ( \exists i>k) \land |x_i-L|>=e )$
>! There is an episilon, that no matter how far you go down in the sequence, there is an element in the sequence that lies outside the e neighborhood of L

# 3.2 Limit Theorems
* DEF: Operators on sequences 
* PRP: Operator on sequences and their limits
* DEF: Order of sequences
* PRP: Order of sequences and their limits

# 3.3 Monotone Sequences
* PRP: Monotone Bounded Sequences have a limit, the supremum

# 3.4 Subsequences and Bolzano Weierstrass Theorm
* DEF: Subsequence
* PRP: For a convergent sequence, every subsequence is convergent
* PRP: Sequence has a monotone subsequence

# 3.5 Cauchy Criterion
* PRP: sequence is cauchy <-> it is convergent
* PRP: sequence is contractive -> it cauchy

# 3.6 Properly Divergent Sequences
* PRP: sequence convergent -> bounded
* PRP: sequence not bounded -> not convergent

# 3.7 Introduction to Series
* DEF: Series of $(x_n)$ is a sequence $s_n = x_1 + .. + x_n$
>! * Sum within the sequence, product?
* PRP: $\sum{x_n}$ convergent $\rightarrow$ $Lim(x_n)=0$
* PRP: Series is convergent <-> series is bounded (if $(x_n)$ is positive)
>! * Series is convergent -> series is bounded
>! * Series is bounded. Series is monotone -> Series is convergent
* PRP: Series, order and convergence
>! * Suppose $0 =< x_n < y_n$. Then the following is true
>! * $\sum{y_n}$ convergent $->$ $\sum{x_n}$ convergent
>! * $\sum{x_n}$ divergent $->$ $\sum{y_n}$ divergent
* PRP: Series, ratio and convergence

# 4 Limits on Functions

# 4.1 Limits of Functions
* DEF: Limit of a function
>! * PRP: TODO $(a_n)$, $(b_n)$ cov to $x$ then $Lim(f(a_n)) = Lim(f(b_n))$ given this we can define uniqueness for anyseq
>! * DEF: $Lim_{x \rightarrow a}(f(x)) = Lim( f(x_n) )$ where $x_n$ is any sequence that conv to x
# 4.2 Limit  Theorems
* DEF: Operator on functions
* PRP: Operator on functions and their limits
# 4.3 Some  Extensions of  the  Limit  Concept
* Different types of sequences from left,right
* Is there some property regarding the various limits of our function
* $ \lim{x}{a} f(x) = lim f(a) $
