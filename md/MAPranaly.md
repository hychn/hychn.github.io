# 1 Preliminaries

# 1.1 Sets and Functions
* DEF Function
* DEF Injective
* DEF Surjective

# 1.2 Boolean Logic
* DEF Negation
* DEF And
* DEF Or
* DEF _Implication_ a
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
* DEF Operator $+ *$ binary function from, to $\mathbb{R}$
* PROP $a+b = b+a$
* PROP $(a+b)+c = a+(b+c)$
* PROP $a*(b+c) = a*b + a*c$
* DEF special elements 0,1 wrt binary functions
  * $a+0=a$, $a*1=a$
  * $a+-a=0$, $a*\dfrac{1}{a}=1$
* PROP uniquness of 0,1
* ---
* DEF Order $a \leq b :=$ b-a is positive or zero 
* PROP Reflexive $a \leq a$
* PROP Transitive $a \leq b$ $b \leq c$ $\rightarrow a \leq c$
* REM Negation $b \leq a$
>! * TFAE
>! * $b \leq a$
>! * a-b is positibe or zero
>! * b-a is negative or zero

# 2.2 ABS and Real-Line
* DEF $|a| = \begin{cases} a>0: a \\ a=0: 0 \\ a<0 : -a  \end{cases}$

# 2.3 Completeness Property of R
* AXI upper bounded subset of $\mathbb{R}$ has a least upper bound

# 2.4 Applications of Supremum

# 2.5 Intervals

# 3 Sequences

# 3.1 Sequences and Their Limits
* DEF Sequence. naturally ordered sequence of elements in $\mathbb{R}$
* DEF Limit. The limit of sequence $(x_n)$ is $L$ if: for any $e>0$,$\exists k$ s.t. $i>k \rightarrow |x_i-L|<e$
* PROP Convergent Sequence are Bounded
* DEF Negation of convergence to L
>! $\exists e>0$ s.t. $\forall k \neg (i>k \rightarrow |x_i-L|<e)$
>! $\exists e>0$ s.t. $\forall k ( \exists i>k) \land |x_i-L|>=e )$
>! There is an episilon, that no matter how far you go down in the sequence, there is an element in the sequence that lies outside the e neighborhood of L

# 3.2 Limit Theorems
* Operators on sequences and limits

# 3.3 Monotone Sequences
* PROP Monotone Bounded Sequences have a limit, the supremum

# 3.4 Subsequences and Bolzano Weierstrass Theorm
* DEF Subsequence
* PROP Every sequence has a monotone subsequence

# 3.5 Cauchy Criterion
* PROP If a sequence is cauchy iff it is convergent
* PROP If a sequence is contractive, it cauchy

# 3.6 Properly Divergent Sequences
* PROP Sequence convergent $\rightarrow$ bounded
* PROP Sequence not bounded $\rightarrow$ not convergent

# 3.7 Introduction to Series
* DEF Series of $(x_n)$ is a sequence $s_n=x_1+..+x_n$
>! * Sum within the sequence, product?
* PROP $\sum{x_n}$ convergent $\rightarrow$ $Lim(x_n)=0$
>! * It is easy to see this if $x_n$ were all positive because the sum wil be infinite otherwise
>! * If a sequence is convergent, the distance between the sequences will converge to zero
>!  * This is definition of Cauchy 
>! * The book proves it by using $s_{n+1} - s_{n} = x_{n+1}$ = $Lim(s_{n+1} - s_{n}) = Lim(x_{n+1}) = Lim(x_n)$
>!  * I think this is a valuable perspective as well
* PROP Series is convergent $\iff$ series is bounded (if $(x_n)$ is positive)
>! * Series is convergent -> series is bounded
>! * Series is bounded. Series is monotone -> Series is convergent
* PROP Series, order and convergence
>! * Suppose $0 =< x_n < y_n$. Then the following is true
>!  * $\sum{y_n}$ convergent $->$ $\sum{x_n}$ convergent
>!  * bounded, monotone
>!  * Book proof: use cauchy 
>! * $\sum{x_n}$ divergent $->$ $\sum{y_n}$ divergent
>!  * $\sum{x_n}$ divergent -> not monotone or not bounded -> not bounded -> $\sum{y_n}$ is also not bounded -> not convergent
>!  * Another proof: Is also contrapositive of prior statement
* PROP Series, ratio and convergence
>! a
