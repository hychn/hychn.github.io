# Stable baselines and how can we use this?
* https://github.com/DLR-RM/stable-baselines3

# PPO
The Proximal Policy Optimization (PPO) algorithm is a popular reinforcement learning algorithm used to train agents to perform tasks in complex environments. It is based on the policy gradient algorithm, which aims to optimize a policy function that maps observations to actions.
PPO introduces two key concepts: the clipped surrogate objective and the trust region constraint. The clipped surrogate objective is a modification to the standard policy gradient objective that limits the change in the policy update. This is done to prevent large changes to the policy that could lead to instability during training.
The trust region constraint ensures that the updated policy is close to the old policy, which also helps to prevent instability during training. The idea is to constrain the size of the policy update so that it does not deviate too far from the current policy.
PPO operates by iteratively collecting data from the environment using the current policy, and then using that data to update the policy. Each iteration involves the following steps:
Collect data: The agent interacts with the environment using the current policy to generate a batch of observations and actions.
Compute advantages: The advantages of each action are estimated using a value function or other method.
Compute surrogate objective: The clipped surrogate objective is computed using the current and updated policies and the advantages.
Update policy: The policy is updated using an optimization algorithm that minimizes the surrogate objective subject to the trust region constraint.
Repeat: The process is repeated for a fixed number of iterations or until convergence.
Overall, PPO is a powerful and effective algorithm for training agents to perform tasks in complex environments, and it has been used to achieve state-of-the-art performance in a variety of applications.


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
