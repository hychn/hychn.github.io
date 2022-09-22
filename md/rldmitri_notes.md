$\def\lim#1#2{ \underset{#1 \rightarrow #2}{lim} }$
$\def\min#1{ \underset{#1}{min} }$

* http://www.mit.edu/~dimitrib/RLbook.html
* http://web.mit.edu/dimitrib/www/RL_CLASS_NOTES_2022.pdf
* https://web.mit.edu/dimitrib/www/RL_Frontmatter-SHORT-INTERNET-POSTED.pdf
# 1.2 Deterministic Dynamic Programming
* DEF Dynamic Programming: dynamic programming usually refers to simplifying a decision by breaking it down into a sequence of decision steps over time, and using bellman equation
* DEF Bellman EQ: V(a_0) = v(a_0) + b*V(a_1)


* For an auto travel analogy, suppose that the fastest route from Phoenix to Boston passes through St Louis. The principle of optimality translates to the obvious fact that the St Louis to Boston portion of the route is also the fastest route for a trip that starts from St Louis and ends in Boston. The principle of optimality suggests that the optimal cost function can be constructed in piecemeal fashion going backwards: first compute the optimal cost function for the tail subproblem involving the last stage, then solve the tail subproblem involving the last two stages, and continue in this manner until the optimal cost function for the entire problem is constructed.
* The DP algorithm is based on this idea: it proceeds sequentially, by solving all the tail subproblems of a given time length, using the solution of the tail subproblems of shorter time length. We illustrate the algorithm with the scheduling problem of Example 1.2.1. The calculations are simple but tedious, and may be skipped without loss of continuity. However, they may be worth going over by a reader that has no prior experience in the use of DP.

* We have noted earlier that discrete deterministic optimization problems, including challenging combinatorial problems, can be typically formulated as DP problems by breaking down each feasible solution into a sequence of decisions/controls, as illustrated with the scheduling Example 1.2.1. This formulation often leads to an intractable DP computation because of an exponential explosion of the number of states as time progresses. However, a DP formulation brings to bear approximate DP methods, such as rollout and others, to be discussed shortly, which can deal with the exponentially increasing size of the state space.

* NP complete

* Dynamic Programming: solve tail problem and then solve future problem
  * ABCD (find the values of 2 paths, 3paths, 4 paths) and
  * Suppose A-C is optimal path. Then for any point A<B<C,  A-B,B-C are optimal path from AB,BC
    * otherwise A-C would not be optimal
  * ?Why can't we pursue the optimal path from the head? You can. Compute all 2 paths the 3 paths would be considering ABx
    * It's no different to pursuing from tail

* Why do people rewrite the D.P problem in terms of Q?
* Multi-step lookahead vs one-step lookhead
# What is your proposal
* Potential Improvements
  * Mix policy methods, with model methods
  * Multi-step 
* Mathematic Courses
* Intuition/rigor-based experimentation (

# Rollout
* The major theoretical property of rollout is 'cost improvement' : the cost obtained by rollout using some base heuristic is less or equal to the corresponding cost of the base heuristic

* There is quite alot of notation in this book and the declaritive/important statements are just left as sentences
  * highlight these key points (key definitions)
  * There are also quite alot of notation (He does spend a bit of time in the beginning formulating the generic DP problem)
  * There are quite alot of equations
* rollout heuristic
* Let's write out the key definitions
* This weekend we will work on the purpose proposal and cv and send email to professors on Sun evening

# Definitions
* $0 \leq k \leq N$ time index
* state of system: $x_k$ $\in$ (state space at k)
* control/decision variable: $u_k \in U_k(x_k)$ (control space at k)
* state update: $f_k(x_k,u_k)=x_{k+1}$
* cost at time k $g_k(x_k,u_k)$ 
* total cost of control: $J(x_0;u_0, ..., u_{N-1}) = g_N(x_N) + \sum_{k=0}^{N-1}g_k(x_k,u_k)$ (why write g_N separate?)

# Points

* minimize $J$ over $\{u_0,u_1,...,u_{N-1} \}$
* $J^*(x_0) = \underset{ \underset{k=0,..,N-1}{u_k \in U_k(x_k)} }{min} J(x_0; u_0,...,u_{N-1})$
* (cost and state update depending on k)
## Discrete Optimal Control Problems
* deterministic finite-state finite-horizon optimal control problems
  * det: at state $x_k$, each control $u_k$ determines 1 next state $x_{k+1}$
  * finite-state: finite num of {x_k, }
  * finite-horizion N is finite
* graph, shortest path problem from stage 0 to terminal node
* See [Ber17], Section 2.1, and [Ber91], [Ber98] for extensive accounts of shortest path methods, which connect with our discussion here

## Dynamic Programming Algorithm
### Principle of Optimality
* A truncated optimal solution $\{*u_0,*u_1,...,*u_{N-1} \}$ is optimal for the sub problem, minimize cost to go from time k
* cost to go from time k: $J(x_k;...)$
* $J^*_k(x_k) = \underset{u_k}{min} g(x_k,uk)+J^*_{k+1}(x_k)$
* $J^*_k(x_k) = \min{u_k} g(x_k,uk)+J^*_{k+1}(x_k)$





# RL SPIN EXAMPLE Understanding

What is rollout, it is an estimation of J(u0,u1,...,uk-1,uk)? Are you sure. lets read it again.
What is diff between q-estimiation and optimal policy optimization


Ok so lets go back to the basics
G()

trajectory $(x_0,u_0,x_1,u_1...)$
$r(x_t,u_t)$ reward
$p(x_{t+1} | x_t,u_t)$

$V(traj) = E[ R(traj) ]$
Goal is to find maximal traj
which is given by maximal policy $max_{a_t}( r(x_t,a_t) + \gamma V^*(x_{t+1}) )$

$R(\tau) = \sum_{t=0}[\gamma^t r(s_t, a_t)]$
$V(s)   = E_{\tau ~ \pi}[ R(\tau) | s_0=s ]$
$Q(s,a) = E_{\tau ~ \pi}[ R(\tau) | s_0=s, a_0=a ]$

* There are two approaches to solving this problem
* 1 find a good estimate of $V^*$ to create this maximal policy
* 2 update the policy $\pi_\theta$ with gradients from $J$
  * $ J(\pi_\theta) = E_{\tau ~ \pi_\theta}[R(\tau)]$$
  * $ \Delta_\theta J(\pi_\theta) = E_{\tau ~ \pi_\theta}[\sum_{t=0} \Delta_\theta log(\pi_\theta(a_t|s_t))*R(\tau)]$
    * There is a proof considering the reward $R(\tau)$, afterward $t$
  * Baselines


* Model free - model based
* One of the most important branching points in an RL algorithm is the question of whether the agent has access to (or learns) a model of the environment. By a model of the environment, we mean a function which predicts state transitions and rewards.

In practice, $V^{\pi}(s_t)$ cannot be computed exactly, so it has to be approximated.  what is the reason?
what is Rhat? how can we get R if the model of the enviroment doesn't tell us? (Check the book by dmitri, it  only needs R for the end states)

