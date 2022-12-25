# Dimension
* THM the maximal LI elements generate a vector space
* THM for a finte vector space number of maximal LI elements is unique. We call this the dimension of the vector space
* EX A vector subspace may not share the same basis as the containing set. Consider $\mathbb{R}^2$ whose basis is $(1,0), and (0,1)$ and subspace $k(1,1)$

# Linear map
* $dim(V) = dim(Kerf) + dim(Imf)$
* For every linear map there is a matrix which represents it
* if $kerf={0}$ then the basis of domain coincides with basis of image due to the LI being linked across f
  * $0 = k_1*f(b_1) + ... + k_n*f(b_n) = f(k_1*b_1 + ... + k_n*b_n) \leftrightarrow k_1*b_1 + ... + k_n*b_n=0 $
* So the objective is to take f and construct a quotient space where the the $kerf={0}$
* $V/W$ Quotient Vector Spaces is indeed a vector space

* LI in $V$ and not in $W$ means LI in $V/W$
  * suppose it was not LI then $k*b_1+k$
* LI in $V/W$ means LI in $V$

* claim: $dim(V) = dim(V/W) + dim(W)$
  * let $dim(V)=n$
  * let $w_1 ... w_m$ be the basis of $W$
  * since the basis of $W$ is also LI we can extend it to n elements $w_1 ... w_m, b_{m+1}, ..., b_n$
  * now we will show that $b_{m+1}, ..., b_n$ is the basis of $V/W$
    * first $b_{m+1}, ..., b_n$ is LI in $V/W$ because it is LI with the basis of W 
      * Proof:
      * suppose for contradiction that LD, then $k_1*b_{m+1}+ ...+ k_n*b_n \in W$ where some $k_i$ nonzero
      * $b_{m+1}, ..., b_n$ LI so $k_1*b_{m+1}+ ...+ k_n*b_n != 0$
      * since the basis of W generates  $k_1*b_{m+1}+ ...+ k_n*b_n = c_1*w_1+...+c_m*w_m$ where some $c_i$ nonzero 
      * then we have the linear dependence of the terms $k_1*b_{m+1}+ ...+ k_n*b_n + c_1*w_1+...+c_m*w_m = 0$ which is contradiction
    * this means the basis of $V/W$ must be greater or equal to $b_{m+1}, ..., b_n$ 
    * second suppose for contradiction that basis it is greater than $b_{m+1}, ..., b_n$, then we extend our original basis by 1 $b_{m+1}, ..., b_n, x$
      * Proof:
      * $b_{m+1}, ..., b_n, x$ is LI in $V/W$
      * $w_1,...w_m, b_{m+1}, ..., b_n, x$ is LD in $V$
      * $c_1*w_1 +... + c_m*w_m  + k_1*b_{m+1} + ... + k_n*b_n + k*x = 0$ where some coefficients are nonzero
        * k cannot be zero ( otherwise LD of remaining terms)
        * some k_i must be nonzero (otherwise if only c_i nonzero then x can be written in terms of w_1. This would implie x is in W and $b_{m+1}, ..., b_n, x$ is not LI in $V/W$)
        * if some k_i nonzero then we have contradiction since $k_i*b_{m+i} + k*x$ is in W, which means $b_{m+i}, x$ are LD in $V/W$
        * so this cannot be
    * This means length of basis for $V/W$ must be equal to $b_{m+1}, ..., b_n$, giving us $dim(V) = dim(V/W) + dim(W)$

>! * Key ideas from above: Basis of subspace is LI in superspace
>! * Extension of existing LI elements to new basis allows us to draw powerful conclusions because we can infer additional properties 
>! * ??? Is there some general way to capture the relationship between, LI, LD elements instead of doing this case-by-case check?


# Matrices and Linear maps
* Change of Basis
* linear map as matrix 1-1 relationship?

# !!! let G generate V, then $|G|>=dim(V)$
* Interesting way to prove by contradiction of $|G|<dim(V)$
  * $G={g_1}$ with $V={v_1, v_2}$
    * $v1=a_1*g1$
    * $v2=a_2*g1$
    * then $k*v1+k*v2=0$
  * $G={g_1, g_2}$ with $V={v_1, v_2, v_3}$
    * $v_1=a_1*g_1 + b_1*g_2$
    * $v_2=a_2*g_1 + b_2*g_2$
    * $v_3=a_3*g_1 + b_3*g_2$
    * do Guassian elimination and we get
    * $a*v_1-a*v_2 = g_2$
    * $b*v_2-b*v_3 = g_2$
    * from here we get LD
  * the Gaussian elim idea is also kinda used in determinants

# Determinant
* Determinants? A nice way to compare and see the linear dependence/independence of vectors
  * Build it from smaller cases
