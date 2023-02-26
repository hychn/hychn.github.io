# Next step
* Refresh what PPO is
* See how it is implemented in the connect 4 example
* https://towardsdatascience.com/proximal-policy-optimization-ppo-explained-abed1952457b
* Apply it to your own mcst algo (can it be applied to mcst?)
  * Yes, it is possible to apply the Proximal Policy Optimization (PPO) algorithm to a Monte Carlo Tree Search (MCTS) model-based algorithm. However, it's important to note that MCTS is already a model-based algorithm that uses simulations to construct a tree of possible future states and actions, whereas PPO is a model-free reinforcement learning algorithm that learns a policy directly from experience.
  * In this hybrid approach, the MCTS algorithm is used to simulate the environment and estimate the value of each state, while PPO is used to learn a policy that optimizes the agent's actions in each state. The policy learned by PPO can be used to guide the MCTS search and improve its efficiency and effectiveness.
  * One approach to combining PPO with MCTS is to use PPO to train a neural network that takes as input the state of the game and outputs a probability distribution over actions. This network can then be used to guide the MCTS search by biasing the selection of actions towards those with higher probabilities. The MCTS algorithm can also be used to generate additional training data for the PPO algorithm by simulating the environment and collecting state-action pairs.
  * Overall, combining PPO with MCTS can be an effective way to leverage the strengths of both model-based and model-free reinforcement learning algorithms. However, the specific details of how to combine these algorithms will depend on the particular problem and environment being studied.


# Loss of example
* A = log(predp)*p
* B = torch.where(p>0, p*log(p),0)
* loss = B-A
* looks like normalization of entropy or something
* This is -plog(pred_p) for p≤0 and plog(p)-plog(pred_p)=plog(p/pred_p) for p>0. This sort of looks like one of the surrogates for PPO. Where is this from?


# What was the definition of entropy?
# What was the motivation behind KL divergence?
* encoding passing information in bits
  * say there are a set of events observed with different probabilities for A and B
  * A's probabilties are split by $p_n=1/2^n$
  * B's probabilities are $q_n$
  * A events are bit encoded to minimize the bits expressed probabilistically. $1/2^n = 11..(n-1)..1110$ 
    * this means a event with probability $1/2^n$ uses nbits to encode the event
  * Expected number of bits for B using A's encoding
    * $KL(A,B) = \sum log_2(p_n)*q_n$


# on policy vs off policy
* An off-policy learner learns the value of the optimal policy independently of the agent's actions. Q-learning is an off-policy learner. An on-policy learner learns the value of the policy being carried out by the agent including the exploration steps."
* The reason that Q-learning is off-policy is that it updates its Q-values using the Q-value of the next state s′s′ and the greedy action a′a′. In other words, it estimates the return (total discounted future reward) for state-action pairs assuming a greedy policy were followed despite the fact that it's not following a greedy policy.


# Stable baselines and how can we use this?
* https://github.com/laserany/snake-ai-model


* https://github.com/deepmind/open_spiel
* https://github.com/DLR-RM/stable-baselines3
* https://github.com/Farama-Foundation/Minigrid
* KL-divergence

* Advantage: represents how much better or worse an action is compared to the average action in a given state, taking into account the expected reward and the current policy.

# PPO
* The main idea behind ppo is 
  * Select the best parameter for expected advantage 
  * bound the advantange of new parameter to be epsilon close advantange of previous parameter

* https://spinningup.openai.com/en/latest/algorithms/ppo.html
* The Proximal Policy Optimization (PPO) algorithm is a popular reinforcement learning algorithm used to train agents to perform tasks in complex environments. It is based on the policy gradient algorithm, which aims to optimize a policy function that maps observations to actions.
* PPO introduces two key concepts: the clipped surrogate objective and the trust region constraint. The clipped surrogate objective is a modification to the standard policy gradient objective that limits the change in the policy update. This is done to prevent large changes to the policy that could lead to instability during training.
* The trust region constraint ensures that the updated policy is close to the old policy, which also helps to prevent instability during training. The idea is to constrain the size of the policy update so that it does not deviate too far from the current policy.
* PPO operates by iteratively collecting data from the environment using the current policy, and then using that data to update the policy. Each iteration involves the following steps:
* Collect data: The agent interacts with the environment using the current policy to generate a batch of observations and actions.
* Compute advantages: The advantages of each action are estimated using a value function or other method.
* Compute surrogate objective: The clipped surrogate objective is computed using the current and updated policies and the advantages.
* Update policy: The policy is updated using an optimization algorithm that minimizes the surrogate objective subject to the trust region constraint.
* Repeat: The process is repeated for a fixed number of iterations or until convergence.
* Overall, PPO is a powerful and effective algorithm for training agents to perform tasks in complex environments, and it has been used to achieve state-of-the-art performance in a variety of applications.


# Different types of RL algorithms 
* There are several popular reinforcement learning algorithms that differ in their approaches to solving the RL problem. Some of the key differences between these algorithms are:
* Q-Learning vs. Policy Gradient Methods: Q-learning is a model-free method that learns an optimal action-value function, while policy gradient methods learn a policy directly. Q-learning is often used in environments with discrete actions, while policy gradient methods are better suited to continuous action spaces.
* Deep Q-Networks (DQN) vs. Actor-Critic: DQN is a deep learning-based extension of Q-learning that uses a neural network to estimate the action-value function, while actor-critic methods learn a policy and a value function simultaneously. DQN is often used in environments with large state spaces, while actor-critic methods are better suited to continuous control tasks.
* Proximal Policy Optimization (PPO) vs. Trust Region Policy Optimization (TRPO): PPO and TRPO are both policy gradient methods that use a constraint on the policy update to improve stability during training. PPO uses a clipped surrogate objective to limit policy changes, while TRPO uses a trust region constraint to ensure that policy updates do not deviate too far from the current policy.
* Model-Based vs. Model-Free Methods: Model-based methods use a model of the environment to plan actions and estimate the state-action value function, while model-free methods learn the value function directly from experience. Model-based methods are often more sample-efficient but require accurate models of the environment, while model-free methods can be used in situations where a model is unavailable or difficult to estimate.
* Monte Carlo vs. Temporal Difference (TD) Methods: Monte Carlo methods estimate the value function by averaging the rewards obtained from a sequence of actions, while TD methods estimate the value function using a bootstrapped estimate of the future reward. TD methods are often more efficient than Monte Carlo methods because they can learn from incomplete sequences of experience.
* Overall, the choice of RL algorithm depends on the specific characteristics of the problem being solved, including the size of the state and action spaces, the structure of the reward function, and the availability of a model of the environment.


# Chat GPT RL
* https://openai.com/blog/chatgpt/
* Human in the loop RL
* We trained this model using Reinforcement Learning from Human Feedback (RLHF), using the same methods as InstructGPT, but with slight differences in the data collection setup. We trained an initial model using supervised fine-tuning: human AI trainers provided conversations in which they played both sides—the user and an AI assistant. We gave the trainers access to model-written suggestions to help them compose their responses. We mixed this new dialogue dataset with the InstructGPT dataset, which we transformed into a dialogue format.
* To create a reward model for reinforcement learning, we needed to collect comparison data, which consisted of two or more model responses ranked by quality. To collect this data, we took conversations that AI trainers had with the chatbot. We randomly selected a model-written message, sampled several alternative completions, and had AI trainers rank them. Using these reward models, we can fine-tune the model using Proximal Policy Optimization. We performed several iterations of this process.
