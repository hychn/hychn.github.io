$\def\<-{ \leftarrow }$
$\def\->{ \rightarrow}$


# Nan Jiang
* Title: I have read the instructions on your website

I have read the instructions on your website

* Hello Professor,

* Thank you for your time. I am really interested your research.

* ML projects:
  * Computer Vision: Satellite image prediction, robotic pose tracking 
  * Protein contact/structure prediction
  * RL gomoku

* I am very interested in your research sample efficiency
# [A Few Expert Queries Suffices for Sample-Efficient RL with Resets and Linear Value Approximation}(https://arxiv.org/pdf/2207.08342.pdf)
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
  
* Under these conditions, our method uses surprisingly few expert queries combined with some modest (polynomial) amount of exploration to recover the expert policy.
  * Delphi recovers a policy matching which is e-optimal,(with respect to the expert policy)
    * O(d log(B/e) ) oracle calls and $\tilde{O}(\dfrac{d^2 H^5 |A| B^4} {e^4})$
      * B is bound on $l_2$-norm of unknown linear paramter
* Assumtpion 2.1 interactive expert
* Assumption 2.2 expert v is linear with bounded features
* Assumption 2.3 after experiencing transition (s,a,r,s') in MDP, agent can return to state s


  * H horizion
  * S - state space, A action set, 
  * R : SxA -> [0,1]     reward distribution
  * P : SxA -> [0,1]^|S| transition distribution
  * Many potential applications of reinforcement learning (RL) have intractably-large state-spaces.
  * sample complexity
    * number of training-samples that it needs in order to successfully learn a target function

* I have been reading various resources, hugging face, bersaktas,...
  * good theoretical text?
    * or just need to go through the papers
    * with exercises?

* Undegraduate:
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
