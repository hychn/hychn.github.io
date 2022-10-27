$\def\<-{ \leftarrow }$
$\def\->{ \rightarrow}$
$\def\>={ \geq }$
$\def\<={ \leq }$

# Intoduction
* Title: I have read the instructions on your website

I have read the instructions on your website

* Hello Professor,

* My name is Yechan Hong. 
* I did my B.A. focused in Computer Science.
* Later, I completed M.S. in Applied Mathematics because of my strong interest for the mathemathics of AI.
* I am working in the industry for the past 3 years for my mandatory military service and am planning to return for a doctoral degree in Fall 2023.

* ML projects:
  * Computer Vision: Satellite image prediction, robotic pose tracking 
  * Protein contact/structure prediction
  * RL gomoku

* Undergraduate:
  * Statistical Model Analysis: A-
  * Operations Research 1,2: A,A
* Graduate math courses:
  * Advanced Calculus Single Variable: A-
  * Advanced Calculus Multi Variable: A-
  * Real Analysis 1, 2: A,A-
  * Intro to Abstract Linear Algebra: A-
  * Abstract Algebra Intro, 1, 2: A-,B+,B-
  * Intro to Complex Variables: A-
  * General Topology 1: A
  * Adv Ordinary Diff Equations: A+


* I am very interested in your research sample efficiency
# Paper
* [A Few Expert Queries Suffices for Sample-Efficient RL with Resets and Linear Value Approximation](https://arxiv.org/pdf/2207.08342.pdf)
* A basic starting point which still lacks comprehensive understanding is the case of linear value function approximation, which models value functions as lying in the span of a known d-dimensional feature mapping and asks for methods which have sample complexities that are polynomial only in d, H, and possibly |A|
* optimal value function (or optimal action-value function) is assumed to be linear
* In recent years much has been said about linear value approximation under stronger assumptions
  * under determinism
  * linear/low-rank MDPs
    * 
  * Bellman-closedness
    * Small bellman error?
    * Bellman error $|| V(x) - (R+E[V(x')]) ||$
      * Bellman backup $V(x) \<- r (R+E[V(x')])+(1-r)V(x)$
  * existence of core states
    * Efficient Planning in Large MDPs with Weak Linear Function Approximation
      * Core States: There is a set of core states $S_* \subset S$ (with $|S_*|=m$) that are available to the algorithm, and the feature vector of every other state can be written as a positive linear combination of the core state features.

* In this work, we consider an alternative possibility for recovering polynomial sample complexities which do not further restrict the class of MDPs under consideration. That is, we assist the learner with some additional side information about the problem.
* Under linear-realizability, what is the minimal amount of expert data required for sample/computational-efficient learning, and which algorithm achieves this
  
## RESULTS
* Under these conditions, our method uses surprisingly few expert queries combined with some modest (polynomial) amount of exploration to recover the expert policy.
  * Delphi recovers a policy matching which is e-optimal,(with respect to the expert policy)
    * 1. $O(d log(B/e) )$ oracle calls 
    * 2. $\tilde{O}(\dfrac{d^2 H^5 |A| B^4} {e^4})$
      * B is bound on $l_2$-norm of unknown linear paramter
* Assumtpion 2.1 interactive expert
* Assumption 2.2 expert v is linear with bounded features
* Assumption 2.3 after experiencing transition (s,a,r,s') in MDP, agent can return to state s
* Definitions
  * H horizion
  * S - state space, A action set, 
  * R : SxA -> [0,1]     reward distribution
  * P : SxA -> [0,1]^|S| transition distribution
  * Many potential applications of reinforcement learning (RL) have intractably-large state-spaces.
  * sample complexity
    * number of training-samples that it needs in order to successfully learn a target function
## Delphi algorithm
* Guess and check
* Pick optimistic linear parameter, $\theta_t$, which is consistent on past expert data we have seen at iteration t
* Check if this parameter is globally consistent by playing $n_rollouts$ of length H with policy derived from $\theta_t$
* After some rollouts
  * Encounters a state that has no consistent action
    * In the first case, we are also inconsistent for the expert action at that state (since all actions are inconsistent)
  * Only encounter states that have consistent action
  * In the second case, we derive (cf. Lemma 3.7) that if no inconsistencies are observed for several rollouts, then our “virtual value” vθ is equal to the true value under πθ (i.e., vπθ ). Using the optimistic property, this implies that we are optimal.

* the policy $\pi_{\theta_t}$ will play any action $a$ such that $v_{\theta_t}$ is consistent with Bellman update for that action, any action $a$ such that $v_{\theta_t} = r(s,a) + <P(s,a),v_{\theta_t}(.)>$
* Thus, the parameter θt which is chosen at time t is orthogonal to the previous t − 1 TD vectors which have been generated from interactions with the oracle. (I'm guess the old actions are consistent action, wrt to all θi)
  * We pick the optimistic linear parameter which is consistent on the past expert data 
    * How do you know it exists?
  * It follows that the iteration complexity is at most d + 1, since there are at most d + 1 linearly
  independent vectors in Rd+1.
  * Use Eluder diension to generalize argument where expectations are estimated
  * Establishes __COMPLEXITY__
## LEMMA'S

### Concentration Inequalities
* Lemma 3.2 Bounds on distance,  $\Delta_{s,a} - \hat{\Delta}_{s,a}$
* Lemma 3.3 Bounds on distance,  $\Delta_{s,a} - \tilde{\Delta}_{s,a}$
* Hoeffding's inequality :In probability theory, Hoeffding's inequality provides an upper bound on the probability that the sum of bounded independent random variables deviates from its expected value by more than a certain amount

### Optimism
* Lemma 3.4 $\theta^{\circ}$ not eliminated. With probability $>=  1-\delta$, $\theta^\circ \in \Theta_t$ for all iterations $t \in [E_d+1]$
  * New admissible parameters $\Theta_t$
  * "Let $\delta_t$ be the vector added to $\Theta_t$ at time t"
  * $\Theta_t \rightarrow \Theta_{t-1} \cap \{\theta | <\tilde{\Delta}, 1 \oplus \theta>  \}$
  * By the bounds we established on 3.2,3.3
    * $|<\tilde{\Delta}-\Delta_t, 1 \oplus \theta>| \leq \epsilon$
    * since $< \Delta_t , 1 \oplus \theta^o> = 0 $ 
      * we get $|<\tilde{\Delta}, 1 \oplus \theta^o>| \leq \epsilon$ 
      * which the means $\theta^o \in \Theta_t$

* Lemma 3.5 Under the event of 3.4, we have $v_t(s_0) \geq v^{\circ}(s_0)$ for  $\forall t \in [E_d]$
  * optimistic update rule?
  * "the update to $\theta_{t+1}$ will choose the argmax $\theta \in \Theta_t$ for $v_{\theta}(s_o)$
  * this means $v_{\theta_{t+1}} \geq v_{\theta^o}$ 

* Notes on Eluder dim:
  * The same sequence cannot be used to extend
    * Namely, the new point at the end
  * is eluder dim well defined?, yes by the term 'maximal'
  * How can you show that a sequence is maximal? (show that the Eluder dim is n)
  * Well Lemma A.2 gives us the upper bound for Eluder dimension given restrictions on $||\theta||$ and $||x||$
  * Lemma 3.6
    * The algorithm forms a Eluder sequence 
    * hence dimension of the sequence produced by algorithm is bounded by A.2
      * which means it can be solved within complexity given by the bound
      * The 2nd condition, that the sum of the difference in $f$ and $f^*$ be less than $e^2$ is met because we chose the contraints on new parameters to be less than $~ \dfrac{e}{sqrt{E_d}}$
      * and we have shown (3.4) optimal parameter must also obey this contrain since
  * $\hat{\delta}$ is estimated TD Vectors obtained with $n_{eval}$ samples
  * $\tilde{\delta}$ is refined data estimated with $4 E_d n_{eval}$

* OK so how do we contrain using E_d if we do not know what it is?

### Iteration Complexity
* 3.6 iteration bound
  * Bind the iteration complexity of the algorithm, Ulder dimension
    * maximum length of sequence of points $(x_i)$ such that there exists functions differing from the target function on $x_i$ but fit correctly on $x1,...,x_{i-1}$
  * Eluder dim for $f^*$, $e$
    * longest sequence possible $[(x_1,f_1), ...(x_n,f_n)]$ st
    * $ \forall i |f_i(x_i) - f^*(x_i)|>e $ and $\Sigma_{j<i} (f_j(x_j)-f^*(x_j))^2 <= e^2$
  * Eluder dimension bound for linear function class, $F = \{f_\theta(x)=\theta^T x\}$
    * $dim_E(F,e)$ <= O(d ln(B/e) )$
  * Finally, produce an e that satistfies the conditions.
  * Smaller epislon implies the dimension is smaller? so this will give us a bound on the dimension

* 3.7 Consistency =⇒ accurate prediction
  * if number of rollouts without observing a consistency break, then estimated value must be roughly equal to true value
* Theorem 3.1 combines all ingridients to conclude




# Other INFO
* I have been reading various resources, hugging face, bersaktas,...
  * good theoretical text?
    * or just need to go through the papers
    * with exercises?


