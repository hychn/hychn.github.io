RAPID UNDERSTANDING AND BOND NEUROPLASCITY FORMING
  * repeadtly look at it, re look at it (multiple things at once)
* When I look at different things I feel more motivated. why is this?
Follow the guide of openai, dont fall down too many rabbit hole
Why does model only seek to optimize it's ability to win and not defend?


# Introduction

* PART 1: a short introduction to RL terminology, kinds of algorithms, and basic theory,
* [Key Papers in DeepRL](https://spinningup.openai.com/en/latest/spinningup/keypapers.html)
* [Code repo of key algo](https://github.com/openai/spinningup)
* [Excercises](https://spinningup.openai.com/en/latest/spinningup/exercises.html)


## ESSAY: Spinning Up as a Deep RL Researcher: https://spinningup.openai.com/en/latest/spinningup/spinningup.html
>! ### The Right Background
>!  * Mathematical background 
>!    * __random variables, Bayes theorem, chain rule prob, expected value, standard dev, importance sampling__
>!  * RL main concepts and terminology
>!    * __states, actions, trajectories, policies, reward, value functions, action-value functions__
>!    * [RL Intro] (https://github.com/jachiam/rl-intro/blob/master/Presentation/rl_intro.pdf)
>!    * [Overview] https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html
>!    * [Classical RL algorithms](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf)
>!  * Learn by Doing
>!    * core deep RL algos Simplicity
>!  * simplest/smallest implementation first
>!    * [Vanilla policy gradient REINFORCE](https://arxiv.org/abs/1604.06778)
>!    * [DQN](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)
>!    * [A2C](https://blog.openai.com/baselines-acktr-a2c/)
>!    * [PPO](https://arxiv.org/abs/1707.06347)
>!    * [DDPG](https://arxiv.org/abs/1509.02971)
>!    * Focus on understanding: 
>!      * writing working RL code requires clear, detail-oriented understanding of the algorithms.
>!      * This is because broken RL code almost always fails silently.
>!    * ablations, intuition for parameters or subroutines have the biggest impact
>!    * Don't overfit
>!    * Iterate fast in simple environments: CartPole-v0, InvertedPendulum-v0, FrozenLake-v0, HalfCheetah-v2 (100-250 steps) OpenAI Gym
>!      * Simplest possible toy task
>!    * If it doesn't work, assume there is a bug 
>!    * Measure everything, replay of agent's performance now and then
>!    * Scale experiments when things work
>!  ### Developing a Research Project
>!    * Avoid reinventing the wheel
>!  ### Doing Rigorous Research in RL
>!  ### Closing Thoughts
>!  ### PS: Other Resources

## Installation
* OpenMPI?
* Spinning Up?

## Algorithms
* Vanilla Policy Gradient (VPG)
* Trust Region Policy Optimization (TRPO)
* Deep Deterministic Policy Gradient (DDPG)
* Twin Delayed DDPG (TD3)
* Proximal Policy Optimization (PPO)
* Soft Actor-Critic (SAC)

### On-Policy Algorithms
* VPG -> TRPO -> PPO
* on-policy: 
  * don't use old data, weaker on sample efficiency
  * directly optimize on bjective, policy performance
  * trades stability  for sample efficiency

### Off-Policy Algorithms
* Qlearning -> DDPG -> TD3 -> SAC
  * Bellman's equation for optimality (Q-function) can be trained to satisfy using any environment iteraction data, as long as there is enough experience from high-reward areas in environment)
* sample efficient if it can get the most out of every sample. Humans are very sample efficient. mcst0 is not it needs many examples to learn2play
* Importance sampling is a technique to filter these samples

### Code Format
* algorithm: 
  * class definition for experience buffer object, used to store information from agent-environment interactions
  * Logger
  * Random seed setting
  * Constructing actor-critic Pytorch module via the actor_critic function passed to algorithm function
  * Instantiate enviroment/experience buffer
  * set up loss function/ diagnostic
  * main loop
    * run agent in environment
    * update parameters of agent
    * log key performance metrics and save


## Part 1: Key Concepts in RL (notations)

* state:$s$
* observations:$o$
* action space: discrete/continuous
* policy deterministic $a_t = \mu_\theta(s_t)$ stochastic $a_t ~ \pi_\theta(.|s_t)$
  * Deterministic Policies: 
    * like NN model
  * Stochastic Policies:
    * Categorical policy (discrete action space) , similar to Categorical NN model
    * Diagonal Guassian policy (continuous action space)
      * __multivariate diagonal distribution__
      * where the __cross variance__ is a diagonal matrix
      * described by mean vector $\mu$ and convariance matrix $\sigma$
    
* sampling actions from policy
* computing log likelihoods of particular actions $log \pi_\theta (a|s)$


* Trajectories
* Reward 
  * finite horizon, infinite horizon discounted return

* Goal in RL is to select a policy which maximizes expected return when the agent acts according to it
* $P(traj|\pi) = \prod_{t=0}^{T-1} p(s_0) p(s_{t+1}| s_t, a_t) \pi(a_t | s_t) $

* Value Functions

* On-Policy Value Function
* On-Policy Action-Value Function
* Optimal Value Function
* Optimal Action-Value Function

Link between and Action-Value functions: Taking an action,  why do we need this?


* Bellman Equations
* https://en.wikipedia.org/wiki/Bellman_equation






# Opportunities
* Open AI Scholars https://openai.com/blog/openai-scholars/ scholars@openai.com
* Nuts and Bolts of deep rl research: http://joschu.net/docs/nuts-and-bolts.pdf
# Future (Notable sights)
* monotonic improvement theory (basis of advanced policy gradient algorithms)? http://joschu.net/docs/thesis.pdf
