# Multi-hop networks
* Traffic engineering (TE) enables optimal forwarding and routing rules to meet quality of service (QoS) requirements for a large volume of traffic flows
* Learna stochastic routing policy for each router so that each router can send a packet to the next-hop router according to the learned  optimal prob
* Naturally leads to multi-path TE strategies, to minimize E2E delay
  * heuristic approach
  * model-based optimization
  * model-free optimiation
* Model-based optimization based on network utility maximization (NUM framework) where TE problem is formulated as a constrained maximization problems of the utility function
* Limitations of model-based approachhes, Multi-agent reinforcement learning (MARL) developement of model-free distributed TE optimization schemes [7-10] where each router, acting as an agent learns the optimal local TE policy in such a way that the colective TE policy of all routers can achieve the optimal E2E TE performance
* Mainly focuses on applying action-value methods such as Q-learning and its variants [11-15 which maximizes TE objective the E2E delay
* The paper proposes a stochastic policy gradient RL
  * Formulate the problem as a multi-path TE problem as a multi-agent Markov decision process (MA-MDP)
  * MA-MDP problem, emply the multi-agent actor-critic algorithm where each router has its own actor and critic


# Network Planning with Deep Reinforcement Learning
* Networking planning, formulated as Integer Linear Programming problem (ILP)
* Uses GNN
* Use RL to prune search space and the use ILP solver to find optimal solution

* Netowkring planning is a hard combinatorial optimzation problem
* Cross-layer decisions taht involve both the IP layer and optical layer needs to be made.
* Planned network must satisfy certain service expectations specified by the operator
* Converging optimal solution is hard with RL

