RAPID UNDERSTANDING AND BOND NEUROPLASCITY FORMING
  * repeadtly look at it, re look at it (multiple things at once)
Follow the guide of openai, dont fall down too many rabbit hole
Why does model only seek to optimize it's ability to win and not defend?


# Introduction


## ESSAY: Spinning Up as a Deep RL Researcher: https://spinningup.openai.com/en/latest/spinningup/spinningup.html
>! ### The Right Background
>!  * Mathematical background 
>!    * __random variables, Bayes theorem, chain rule prob, expected value, standard dev, importance sampling__
>!  * RL main concepts and terminology
>!    * __states, actions, trajectories, policies, reward, value functions, action-value functions__
>!    * [RL Intro] (https://github.com/jachiam/rl-intro/blob/master/Presentation/rl_intro.pdf)
>!    * [Overview] https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html
>!    * [Classical RL algorithms](https://sites.ualberta.ca/~szepesva/papers/RLAlgsInMDPs.pdf)
* Learn by Doing
  * core deep RL algos Simplicity
  * simplest/smallest implementation first
    * [Vanilla policy gradient REINFORCE](https://arxiv.org/abs/1604.06778), [DQN](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf), [A2C](https://blog.openai.com/baselines-acktr-a2c/), [PPO](https://arxiv.org/abs/1707.06347), [DDPG](https://arxiv.org/abs/1509.02971)
  * Focus on understanding: 
    * writing working RL code requires clear, detail-oriented understanding of the algorithms.
    * This is because broken RL code almost always fails silently.
  * ablations, intuition for parameters or subroutines have the biggest impact
  * Don't overfit
  * Iterate fast in simple environments: CartPole-v0, InvertedPendulum-v0, FrozenLake-v0, HalfCheetah-v2 (100-250 steps) OpenAI Gym
    * Simplest possible toy task
  * If it doesn't work, assume there is a bug 
  * Measure everything, replay of agent's performance now and then
  * Scale experiments when things work
### Developing a Research Project
  * Avoid reinventing the wheel
### Doing Rigorous Research in RL
### Closing Thoughts
### PS: Other Resources

* PART 1: a short introduction to RL terminology, kinds of algorithms, and basic theory,
* Key Papers in DeepRL: https://spinningup.openai.com/en/latest/spinningup/keypapers.html
* [Code repo of key algo](https://github.com/openai/spinningup)
* [Excercises](https://spinningup.openai.com/en/latest/spinningup/exercises.html)


















# Opportunities
* Open AI Scholars https://openai.com/blog/openai-scholars/ scholars@openai.com


      * Nuts and Bolts of deep rl research: http://joschu.net/docs/nuts-and-bolts.pdf
# Future (Notable sights)
  * monotonic improvement theory (basis of advanced policy gradient algorithms)? http://joschu.net/docs/thesis.pdf
