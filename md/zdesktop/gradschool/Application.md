* Go through all
  * check missing/duo lingo, Arizona
  * submit application 

# TODO
* https://mila.quebec/en/research-programs/
  * McGill university Dec15
* Dec 1: prince, arizona state, ohio state
  * Read the abstracts/papers
* Contact professors for PhD position, cv simple
* End of next week-11/18 We should be done with all

* Take time and study well the papers and the topics, Finish by next week
  * Princeton SOP
  * Washington SOP
    * Study bayesian inference for Wash U
* Washington Fellowship

* Check missing stuff on all applications
  * Duolingo, Colorado Boulder
  * UTA MyStatus upload transcript



# Other

* What information do you need? capture and store?

$\def\<={ \leq }$
$\def\>={ \geq }$
$\def\->{ \rightarrow}$
$\def\R{ \mathbb{R}}$

* [ML News](https://groups.google.com/g/ml-news)

* Proofs from THE BOOK


# TODO
* PASSPORT
* Apply to 2-3 phD applied math programs with math letter of recommendations
* Proof of Funding

# Birth
* City of Birth: Pocheon/Seoul, Gyeonggi

# Address Contact
* 20 Changseon-Ro 131BEON-Gil
* Changseon-Myeon, Namhae-Gun
* South Gyeongsang
* 52453
* +1 8201022591479

# EDU
* Depauw 8-2010, 5-2014
* Mizzou 8-2016, 5-2019

# Recommendation
* Jan Segert
  * Mathematics Department, University of Missouri
  * professor, retired
  * Master's Thesis Supervisor
  * segertj@gmail.com
* Jianlin Cheng
  * Department of Electrical Engineering and Computer Science
  * Thompson Missouri Distinguished Professor/Director of Bio-ML Lab
  * Master's Thesis Supervisor
  * chengji@missouri.edu
* Ilsang Yoon
  * BIORCHESTRA
  * Chief Alliance Officer 
  * Senior Vice President at PharmCADD
  * isyoon@biorchestra.com

# STEPS
* Finish apply, SOP
* Get supplementary stuff
  * GRE, DuoLingo
* Study the RL field more, read the papers of professors
* Email professors, that request
  * Asking for guidance on which topics to study
    * https://arxiv.org/pdf/2203.12139.pdf
    * Some terms familiar, some terms new
    * ELBO, KL divergence

# List of Schools/Deadline

* For all these schools, check research, and requirements, and write phd
* How about you contact these professors and then see if they have openings in their lab to decide wether to apply or not?


* [Washington University in St. Louis](https://gradadmit.wustl.edu/apply/?sr=4503835c-76a0-44d8-b086-00f19e2bb810)
  * Dec 15 $75
    * Letter Rec
    * SOP
    * Fellowship essay
    * Research Experience Contact
  * [Program Info](https://gradadmit.wustl.edu/apply/?sr=4503835c-76a0-44d8-b086-00f19e2bb810)
    * If you join the PhD program at Washington University, one of the courses you take in your first semester is Introduction to Graduate Study in CSE. As part of this course, you will do two one-month rotations in the research groups of faculty members who are recruiting graduate students. 
    * The rotation model does not preclude students from initiating discussions with faculty whose group they really want to join prior to joining WashU, but it offers the opportunity to be exposed to other research areas and approaches and to interact with potential research advisers before finalizing a commitment.
  * [Deadlines/info](https://engineering.wustl.edu/academics/graduate-admissions/application-checklist.html)
  * [Faculty](https://machinelearning.wustl.edu/faculty/)
    * [William Yeoh](https://sites.wustl.edu/wyeoh/research/)
      * Stochastic Goal Recognition Design Problems with Suboptimal Agents
        * Goal Recognition Design (GRD) problems identify the minimum number of environmental modifications aiming to force an interacting agent to reveal its goal as early as possible. 
          * Extending the stochastic goal recognition design framework by supporting suboptimal agents in cases where an observer has either full or partial observability
          * Presenting methods to evaluate the ambiguity of the model under these assumptions
    * [Brendan Juba](https://www.cse.wustl.edu/~bjuba/papers/index.html)
      * [Polynomial Time Reinforcement Learning in Factored State MDPs with Linear Value Functions](https://www.cse.wustl.edu/~bjuba/papers/fmdp-aistats.pdf)
        * Many reinforcement learning (RL) environments in practice feature enormous state spaces that may be described compactly by a “factored” structure, that may be modeled by Factored Markov Decision Processes
        * We present the first polynomial-time algorithm for RL in Factored State MDPs (generalizing FMDPs) that neither relies on an oracle planner nor requires a linear transition model; it only requires a linear value function with a suitable local basis with respect to the factorization, permitting efficient variable elimination
      * S,A,R,P: State, Action, Reward SxA->real, TransitionProb SxSxA->real P(s'|s,a)
      * t,p: time horizon, initial distribution over S
      * deterministic policy
      * value function of policy, expected sum of reward from initial to horizon following the policy
      * optimal policy for M: u^M
      * episode?
      * Ht history (s1,a1,r1,s2,a2,r2,...st-1,at-1,rt-1)
      * An RL algorithm outputs a sequence of functions ${\pi_k | k=1,2..}$, each mapping H_{t_k} to a probability distribution \pi_k(H_{t_k}) over policies which the agent will employ in episode k. (Selector of policies over depending on the input history)
      * M* latent in the environment
      * regret: 
        * Regret(T,\pi, M*) = sum( k=1,T/t, regretofepisodek)
        * regretofepisodek = E(s~p)[V(u*, s)-V(uk, s)]
        * where u* is optimal policy for M*
        * and uk ~ pi_k(H_{t_k})
        * 
      * Factored spaces
        * Transition from one factored state to another factored state only depends on the current scope
      * Factored rewards
        * the reward of a complete space is equal to the sum of the reward in the factored states
      * Factored linear value function class
        * I thought value depended on policy where is policy here? We are assuming this holds for all policies, specifically the optimal policy
        * Based on the factored linear value functions, the bellman operator can also be factored linearly
      * What is the big point of the paper?
        * Many important application domains of Reinforcement learning (RL) – such as resource allocation or complex games – feature large state spaces, for which existing theoretical guarantees are unsatisfactory. But, many of these domains are believed to be captured by a small dynamic Bayesian network (DBN) on factored state variables.
        * efficiently representing space with factored states
        * assumptions on factored reward functions and factored linear value functions


    * [Roman Garnett](https://www.cse.wustl.edu/~garnett/)
      * Bayesian optimization
      * Automated Model Selection with Bayesian Quadrature
        * We present a novel technique for tailoring Bayesian quadrature (BQ) to model selection. The state-of-the-art for comparing the evidence of multiple models relies on Monte Carlo methods, which converge slowly and are unreliable for com- putationally expensive models. Although previ- ous research has shown that BQ offers sample efficiency superior to Monte Carlo in computing the evidence of an individual model, applying BQ directly to model comparison may waste computa- tion producing an overly-accurate estimate for the evidence of a clearly poor model. 
    * [Course: CSE 515T – Bayesian Methods in Machine Learning](https://www.cse.wustl.edu/~garnett/cse515t/fall_2019/)
      * This is actually a pretty good learning resource
      * [What is Bayesian Methods?](https://www.sarem-seitz.com/when-is-bayesian-machine-learning-actually-useful/)
      * Maximum a-posteriori estimation, P(D|m) p(m)/P(D)
        * apparently this is equivalent to regularized MSE


* [Princeton](https://www.cs.princeton.edu/research/areas)
  * Seems like we dont really need to send out an email, just get accepted
  * [Introduction to Online Nonstochastic Control](https://sites.google.com/view/online-nonstochastic-control/home)
  * [Control Meets Learning Seminar by Elad Hazan](https://www.youtube.com/watch?v=dmWXHmjVxcI)
  * __QUESTIONS__
    * POMDP - partially observable markov decision processes
    * Bayesian inference I still dont get this, check Adji's paper
  * [Elad Hazan](https://www.ehazan.com/)
    * [Nonstochastic Control](https://sites.google.com/view/online-nonstochastic-control/home)
  * [Rayn P Adams](https://www.cs.princeton.edu/~rpa/)
    * [SUMO: UNBIASED ESTIMATION OF LOG MARGINAL PROBABILITY FOR LATENT VARIABLE MODELS](https://openreview.net/attachment?id=SylkYeHtwr&name=original_pdf)
  * [Tom Griffiths](https://cocosci.princeton.edu/index.php)
    * [Optimal nudging for cognitively bounded agents: A framework for modeling, predicting, and controlling the ects of choice architectures](https://psyarxiv.com/7ahdc/)
  * [Adji Bousso Dieng](https://scholar.google.com/citations?hl=en&user=ZCniP_MAAAAJ&view_op=list_works&sortby=pubdate)
    * [Markov Chain Score Ascent: A Unifying Framework of Variational Inference with Markovian Gradients](https://arxiv.org/pdf/2206.06295)
  * [Sanjeev Arora]
    * [Implicit Regularization in Deep Matrix Factorization](https://arxiv.org/pdf/1905.13655.pdf)
      * Task: matrix completition, a model referred to as deep matrix factorization
        * Leading to more accurate discovery
      * Our first finding, supported by theory and experiments, is that adding depth to a matrix factorization enhances an implicit tendency towards low-rank solutions, oftentimes leading to more accurate recovery
      * Secondly, we present theoretical and empirical arguments questioning a nascent view by which implicit regularization in matrix factorization can be captured using simple mathematical norms.
      * Task: Deep matrix factorization, matrix completion and sensing
      * regularization process that changes the result to be simpler
        * adding depth enhances an implicit tendency towards low-rank solutions
  * [Ellen Zhong](https://www.cs.princeton.edu/people/profile/zhonge)
    * [CryoDRGN2: Ab initio neural reconstruction of 3D protein structures from real cryo-EM images](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhong_CryoDRGN2_Ab_Initio_Neural_Reconstruction_of_3D_Protein_Structures_From_ICCV_2021_paper.pdf)
      * utilizing interpolation and smoothness of Fourier space to effectively sample poses and resolutions when evaluting the strcuture density model.
      * model evaluation ˆV(k)of coordinate k (which corresponds to a Fourier coefficient of an image’s pixel)
      * search over multi resolution grids on the space of rotations and in-plane translations
      * how is it searcing effectively? how is it doing the effective searching (interpolation, smoothness in fourier space)
      * learn a neural model of a distribution of 3D structures on real heterogeneous cryo-EM data
      * search algorithms from the traditional cryo-EM literature, and describe the optimizations and design choices required to make such a search procedure computationally tractable in the neural model setting
      * CryoDRGN parameterizes cryo-EM volumes using a coordinate-based MLP with parameters to directly approximate the continuous density function
      *  cryo-EM images (i.e. integral projections) are 2D central slices of the model whose orientation is determined from the image pose
      * GOAL: $V_{\theta}: \R^3 \rightarrow \R $ estimate a coordinate-based volume densitiy function
      * INPUTS: input pose $SO(3) x \R^2$
      * Model coordinates specified in Hartley Space
      * In heterogeneous reconstruction, the volume representation is augmented with a latent variable that is learned using amortized variational inference in the framework of variational autoencoder
      * 5D pose search
        * stimated using a hierarchical search procedure over multiresolution grids on the space of rotations and in-plane translations. 
          * begin with an exhaustive search in the 5-D space of rotations and in-plane translations at some base resolution
          * ollowed by an iterative refinement of the K most likely candidate poses by binary search at successively higher resolution grids
          * interpolation accurate on smooth, smooth functions in fourier space statisfied if model output is centered and contained in the box
          * Computed without additional model evaluations
          * translations in real space map to multiplication by an exponential function in Fourier spac
      * Algorithm and background
        * generative process for image in fourier domain 
          * image(x,y) = f(V,x,y)
        * from this generative process we can form P(X|R,t,V) (pose R,t) and the goal is to optimize this statistical model
      * I think the use of properties of Fourier Space are nice.
        * Speeding up exhaustive search by interpolation
        * Interpolation is only accurate if the underlying function is smooth.
        * Smoothness in Fourier space corresponds to the function being flat at large r in real space, which is satisfied as long as the model output is centered and smaller than the box size
    * Online Nonstochastic Control by Professor Elad Hazan
      * Need for a new theory to get the best of both worlds
      * Optimal control theory, which exactly assumes this zero-mean noise, is therefore overly optimistic and inaccurate for our problem.
      * The designer might resort to robust control theory to account for all possible wind conditions, but this is overly pessimistic. What if we encounter a bright sunny day after all? Planning for the worst case would mean slow and fuel-inefficient flight. 
      * We would like an adaptive control theory which allows us to attain the best of both worlds: an efficient and fast flight when the weather permits, and a careful drone maneuver when this is required by the conditions. Can we design a control theory that will allow us to take into account the spe- cific instance perturbations and miss-specifications, and give us finite time provable guarantees? This is the subject of online non-stochastic control!
    * General examination, year 2
      * Research seminar 
      * in-depth oral examination on contents of seminar and associated general area of research
      * original research results do not have to be presented, but problems whose solution may lead to a thesis should be discussed
      * In many cases the student's thesis is in the same area as the reserach semianr, but this is not reuqired
      * What do you like about this?
        * Fanatasy opportunity and goal to prepare
        * Scope is not to specific but also just right, careful balance
        * Specialization and expansion





# DONE  =================================================================

* [Georgia Institute of Technology](https://grad.gatech.edu/preparing-your-application) Dec 15
  * TODO: Computing - PhD section
  * [Requirements](https://www.cc.gatech.edu/phd-cs-admissions-requirements)
  * [Faculty](https://cse.gatech.edu/content/artificial-intelligence-and-machine-learning)
    * https://ml.gatech.edu/people/faculty/phdprogramfaculty
    * [Florian Schfer](https://f-t-s.github.io/) CONTACT
      * Robust Reinforcement Learning: A Constrained Game-theoretic Approach
    * [Yongxin Chen](https://yongxin.ae.gatech.edu/) CONTACT, DONE
      * [Improved analysis for a proximal algorithm for sampling](https://arxiv.org/pdf/2202.06386.pdf)
      * [A Proximal Algorithm for Sampling from Non-convex Potentials](https://arxiv.org/pdf/2205.10188.pdf)
        * Alternating Sampling Framework (ASF)
        * develop an efficient sampling scheme of Restricted Gaussian Oracle (RGO) for non-convex semi-smooth potentials and
         bound its complexity with a novel technique.
        * to develop a sampling algorithm that can sample from non-convex and semi-smooth potentials.
        * challenging task of sampling from potentials that are neither convex nor smooth
    * [Panagiotis Tsiotras](https://dcsl.gatech.edu/research/autonomous-vehicle-learning.html)
    * [Yunan Luo](https://faculty.cc.gatech.edu/~yunan/)
      * [ECNet is an evolutionary context-integrated deep learning framework for protein engineering](https://www.nature.com/articles/s41467-021-25976-8.pdf)
        * Protein language model, Multiple Sequence Alignment
        * ECNet, evolutionary context to prediction functional fitness,  sequence - function relationship 
  * Program:
    * [Info](https://www.cc.gatech.edu/sites/default/files/documents/2022/202205%20Computer%20Science%20PhD%20Handbook.pdf)
    * Qualifying exam, 
      * knowledge : depth of knowledge in chosen area
      * creativity compoments: research deliverable evaluate creative and research ability
    * PhD Review
  * ECE 6254: Statistical Machine Learning - Mark A. Davenport
    * introduction to the theory of statistical learning and practical machine learning algorithm



* [Uni of Nebraska Lincoln](https://go.unl.edu/gradapp) Jan 15
  * SOP DONE
  * [Requirements](https://computing.unl.edu/graduate-admission-requirements/)
  * No gre, no english requirement
  * [LiuQuian](https://liuqiang12040913.github.io/research.html) CONTACT
    * [OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning](https://arxiv.org/pdf/2111.01616.pdf)
      * poor policy at early stage, require lots of compute resources
        * imitate baseline policy
        * baseline switching, estimate baseline policy cost and use baseline
  * [Vinodchandran Variyam](https://cse.unl.edu/~vinod/)
    * Sample Efficiency in Learning and Testing: Learning distributions from observation is a fundamental problem in machine learning. We investigate the necessity and sufficiency of number of observations  needed for learning distributions.
    * [Efficient interventional distribution learning in the PAC framework](https://proceedings.mlr.press/v151/bhattacharyya22a.html)
      * We consider the problem of efficiently inferring interventional distributions in a causal Bayesian network from a finite number of observations. 
      * PAC Probably Approximately Correct
      * ID aglorithm, identification algorithm
      * Results
        * Algorithm on Bayes net to learn a distribution with $d_{TV}(P,\hat{P}) \leq \epsilon$, total variation distance
          * with constant proability
        * What is bayesian network and how it is used in this paper?
        * algorithm uses m samples and O time 
    * [Near-optimal learning of tree-structured distributions by Chow-Liu](https://dl.acm.org/doi/10.1145/3406325.3451066)
    * [Learning and Sampling of Atomic Interventions from Observations](http://proceedings.mlr.press/v119/bhattacharyya20a.html)
>!  * Hau Chan, CONTACT
>!    * [ Learning Game-theoretic Models from Aggregate Behavioral Data with Applications to Vaccination Rates in Public Health ]
>!    * [Multi-Robot Task Allocation—Complexity and Approximation](https://arxiv.org/pdf/2103.12370.pdf)
>!    * [Monotone k-submodular secretary problems: Cardinality and knapsack constraints](https://www.sciencedirect.com/science/article/abs/pii/S0304397522002079?via%3Dihub)
>!    * [background reference](https://arxiv.org/pdf/1409.1399.pdf)
>!    * request pdf
>!    * DEF submodular $f(S)+f(T)\>= f(S\cap T) + F(S\cup T)$
>!      * U be a set, for $S,T \subseteq U$
>!      * $f : 2^U \-> \mathbb{R}$
>!    * [Adversarial Blocking Bandits](https://proceedings.neurips.cc/paper/2020/file/5cc3749a6e56ef6d656735dff9176074-Paper.pdf)
>!      * To complement our result, we show that a greedy algorithm
>!      that plays the best available arm at each round provides an approximation guarantee.
>!  * Leen-Kiat Soh
>!    * [Scalable Decision-Theoretic Planning in Open and Typed Multiagent Systems](https://ojs.aaai.org/index.php/AAAI/article/download/6200/6056)
>!      * Theoretical analyses establish the number of agents to model in order to achieve acceptable worst case bounds on extrapolation error, as well as regret bounds on the agents utility from modeling only some neighbors. 
>!  * [Mohmmad Hasan](https://engineering.unl.edu/hasan/publications/)
>!  * https://cse.unl.edu/~qyao/#opportunity


* [UNI Indiana](https://iugraduate2023.liaisoncas.com/applicant-ux/#/login) Dec 15
  * [requirements](https://bulletins.iu.edu/iu/gradschool/2020-2021/programs/bloomington/computer-science/index.shtml)
  * [faculty](https://luddy.indiana.edu/research/research-areas/ai-directory.html)
  * RL [Qin Zhang](https://homes.luddy.indiana.edu/qzhangcs) CONTACT
    * [Collaborative Learning with Limited Interaction: Tight Bounds for Distributed Exploration in Multi-Armed Bandits](https://homes.luddy.indiana.edu/qzhangcs/papers/dist-bandits-full.pdf)
      * Distributed system, improve sampling by using multiple agents 
      * making leanring scalable
      * Contributions
        * ??? It is very hard to understand these, let me read the paper
        * Almost tight round-speedup tradeoffs for fixed-time
  * RL [Roni Khardon](https://cgi.luddy.indiana.edu/~rkhardon/publications.php)
    * [Direct Loss Minimization for Sparse Gaussian Processes](https://cgi.luddy.indiana.edu/~rkhardon/PUB/aistats2021-DLMsGP.pdf)
      * Bayesian posterior $p(\theta |x) = \dfrac{p(x|\theta)}{p(x)} p(\theta)$ parameter given evidence
        * where $p(x) = \int p(x|\theta) p(\theta) d\theta$
      * [Variational inference](https://www.cs.princeton.edu/courses/archive/fall11/cos597C/lectures/variational-inference-i.pdf)
      * [Bayesian Network and Message Passing](http://mi.eng.cam.ac.uk/~mjfg/local/4F10.old/lect10.pdf)
        * Message Passing
          * Trees where each node has one parent
      * [Neuro-Dynamic Programming Bertsekas DP Tsitskilis
    * [Approximate Inference for Stochastic Planning in Factored Spaces](https://arxiv.org/pdf/2203.12139.pdf)
      * Belief Propagation
        * Motivation: Find marginal distributions $p_{X_i}(x_i)a = \sum$
  * RL Robots [Lantao Liu](https://vail.sice.indiana.edu/index.html)
    * [Decision-Making Among Bounded Rational Agents](https://arxiv.org/pdf/2210.08672.pdf)
      * Computational constraints during the modeling process
      * Naturally reason about sub-optimal behaviors



* [University of Texas at Austin](http://goapplytexas.org/) Dec 15
  * MyStatus
  * PW: same but without !
  *  Additionally, applicants are exempt from the requirement if they possess a bachelors degree from a U.S. institution or a qualifying country. 
  * Letters of Rec, Statement of Purpose
  * [Info](https://www.cs.utexas.edu/graduate/prospective-students/apply)
  * [Faculty](https://ml.utexas.edu/research-areas/faculty/reinforcement-learning)
  * Importance sampling: monte carlo method for evaluating properties of a particular distribution
  * [Qiang Liu](https://www.cs.utexas.edu/~lqiang/)
    * [Breaking the Curse of Horizon: Infinite-Horizon Off-Policy Estimation](https://arxiv.org/pdf/1810.12429.pdf)
    * [Diffusion-based Molecule Generation with Informative Prior Bridges](https://arxiv.org/pdf/2209.00865.pdf)
      * Applications of mathematics and AI to generate high-quality and realistic molecules that respect prior information.
  * [Peter Stone](https://www.cs.utexas.edu/~pstone/students.shtml)
    * [Lucid Dreaming for Experience Replay: Refreshing Past States with the Current Policy](https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/NCAA21-Du.pdf)
      * Experience replay (ER) improves the data efficiency of off-policy reinforcement learning (RL) algorithms by allowing an agent to store and reuse its past experiences in a replay buffer. While many techniques have been proposed to enhance ER by biasing how experiences are sampled from the buffer, thus far they have not considered strategies for refreshing experiences inside the buffer
      * LIiDER algorithm (we could try this for gomoku to make it less data hungry)
        * 1 Lider moves agent back to a past state
        * 2 Lider lets agent follow its current policy
        * 3 stores and reuses new experience if it turned out better
      * how to sample experiences
  * Program
    * Emphasis and encouragement focus on research
      * First semester Research Course
      * Find advisor during the first year
    * C S 364M. Principles of Machine Learning II.
    * C S 394R. Reinforcement Learning: Theory and Practice.
    * C S 383D. Numerical Analysis: Interpolation, Approximation, Quadrature, and Differential Equations.
    * C S 388J. Optimization.




* [Illinois Urbana Champaign](https://choose.illinois.edu/apply/) Dec 15
  * TODO: Copy of passport
  * [Nan Jian](https://nanjiang.cs.illinois.edu/) CONTACT
  * [Matus Telgarsky](http://mjt.cs.illinois.edu/)
  * [Katie Driggs-Campbell](https://cs.illinois.edu/about/people/faculty/krdc)
  * [Kris K Hauser](https://cs.illinois.edu/about/people/faculty/kkhauser)
  * [Jian Peng](https://cs.illinois.edu/about/people/faculty/jianpeng)


* [University of Kansas](https://gograd.ku.edu/apply/) Jan 5
  * TODO: Copy of passport
  * Math Phd Applied
  * stats, markov chain [Joonha Park](http://people.ku.edu/~j139p002/)
  * statistics [Zsolt Talata](https://talata.ku.edu/cv.html)
  * CS/AI RL control [Morteza Hashemi](https://hashemi.ku.edu/)

* [Arizona State](https://webapp4.asu.edu/dgsadmissions/logout) Dec 31
  * ID:yhong64
  * TODO: SOP
  * Faculty, SOP identify two or three ASU faculty with matching research interests. 
    * [Faculty list](https://scai.engineering.asu.edu/computer-science-and-engineering-faculty)
    * [Subbarao Kambhampati](https://search.asu.edu/profile/95646) [web2](https://yochan-lab.github.io/papers/)
      * Why Did You Do That? Generalizing Causal Link Explanations to Fully Observable Non-Deterministic Planning Problems
      * Large Language Models Still Can't Plan (A Benchmark for LLMs on Planning and Reasoning about Change)
    * [Siddharth Srivastava](https://www.public.asu.edu/~ssriva43/)
      * Learning Dynamic Abstract Representations for Sample-Efficient Reinforcement Learning.
    * [Dimitri Bertsekas](https://search.asu.edu/profile/3410924)
      * 'ExpertRNA: A new framework for RNA structure prediction'
    * bio informatics [Heewook Lee](https://search.asu.edu/profile/3505050)
    * bio informatics [Stephanie Forrest](https://search.asu.edu/profile/3182641)
  * Program
    * [ASU program](https://degrees.apps.asu.edu/masters-phd/major/ASU00/ESCOMSCPHD/computer-science-phd?init=false&nopassive=true)
    * [ASU handbook](https://scai.engineering.asu.edu/wp-content/uploads/2022/08/PHD-CS-Handbook-2022-2023Publish.pdf)
      * Comprehensive exam, show mastered the knowledge to conduct research in specialization
      * Proposal exam, mastered the research methods to identify, formulate, and plan research in specialization

* [Ohio State](https://delegated.osu.edu/psp/csosuda/EMPLOYEE/CAMP/c/OAD_GEA.OAD_GEA_NUR_APL.GBL?) Dec 1
  * id: yechanhong92
  * TODO: SOP, faculty names
  * [Faculty](https://cse.osu.edu/research/artificial-intelligence)
    * [Andrew Perrault](https://aperrault.github.io/publications/)
      * 'Normality-Guided Distributional Reinforcement Learning for Continuous Control'
        * We propose a different idea, leveraging the features of the learned distribution to estimate whether a state is sufficiently visited or not.
          * Sampling enough
    * [Ness B. Shroff](http://newslab.ece.ohio-state.edu/for%20students/index.html)
      * 'Optimal Sampling for Data Freshness: Unreliable Transmissions with Random Two-way Delay'
        *  optimal sampling strategy that minimizes the long-term average estimation error
  * Program
    * Direct PhD track
    * Coursework (competant and knowledgeable on fundamental principles of cs) 
    * and research
    * new qualifying process, take time to build the basics and faculty research assessment
  * Course
    * STAT 7620 Elements of Statistical Learning, interdisciplinary final project to apply the ideas

* [Uni Wisconsin Madison](https://apply.grad.wisc.edu/Account/Login?ReturnUrl=%2f) Dec 15
  * https://www.cs.wisc.edu/graduate/graduate-admissions-faq/
  * faculty
    * RL [Josiah Hanna](https://pages.cs.wisc.edu/~jphanna/publications.html)
      * 'Importance Sampling in Reinforcement Learning with an Estimated Behavior Policy'
        * By replacing behavior policy action probabilities with maximum likelihood estimates from observed data, reduce variance due to sampling error.
    * RL [Xiaojin Zhu](https://pages.cs.wisc.edu/~jerryzhu/research.html)
      * 'The Sample Complexity of Teaching-by-Reinforcement on Q-Learning'
        * characterize the sample complexity of teaching for different constraints in constructing teaching sequence
        * I raelly like this style of exploring consequences
    * statistics: [Miaoyan Wang](https://pages.stat.wisc.edu/~miaoyan/people.html)
    * bio [Vikas Singh](https://www.biostat.wisc.edu/~vsingh/)
    * [Ilias Diakonikolas](http://www.iliasdiakonikolas.org/)
    * statistics: [Garvesh Raskutti](https://pages.cs.wisc.edu/~raskutti/publication.html)
    * Daifeng Wang
    
  * TODO: add Robert Nowak
  * SOP why this school is for you
    * faculty research
    * courses
        * CS761 Mathematical Foundations of Machine Learning
          * foundations fo statistics, final project to make small contribution to jumpstart the research process.
    * program characteristic
      * Well balanced
      * breadth requirement, take courese, passing qualifying examination
        * Artificial Intelligence: 532, 534, 540, 545, 731, 760, 761, 766, 769
        * Bioinformatics: 576,776
      * depth requirement: preliminary examination



* [University of Colorado Boulder](https://grad.apply.colorado.edu/account/login) Dec 15
  * [Statement of Purpose](https://www.colorado.edu/cs/admissions/graduate-admissions/how-apply)
    * Colorado doesn't have a seperate section for indicating interest to program so you need to be really clear in this section.
    * Section headers

  * [recruiting](https://www.colorado.edu/cs/admissions/graduate-admissions/see-who-recruiting-fall-2023)
  * [requirements](https://www.colorado.edu/cs/academics/graduate-programs/doctor-philosophy/degree-requirements)
  * RL Control Systems [Majid Zamani](https://www.hyconsys.com/publications.html)
  * RL [Lijun Chen](https://spot.colorado.edu/~lich1539/)
  * RL [Ashutosh Trivedi](https://astrivedi.github.io/www/pubs.html)
  * SOP why this school is for you, just list of professors
    * Professor Lijun Chen's research, 'Incentivized Exploration for Multi-Armed Bandits under Reward Drift', provides ideas related to my key question of qualifying different types of sampling; the paper explores a compensation scheme for UCB, e-Greedy, and Thompson sampling algorithms and demonstrates it's effectiveness by show the regret is similar to the compensation. I really appreciated the style of the paper where the theory was backed up with numerical experiments.
    * Professor Majid Zamani's research, 'Compositional construction of finite MDPs for large-scale stochastic switched systems: A dissipativity approach', constructs an estimation and establishes an upper bound for the error. I am very interested in these types of techniques of simplifying a more complex system and qualifying the simplication.
    * I am also intrested in the statistical machine learning research from the mathematics department; professor Jem Corcoran's research on using importance sampling to manage rare event probabilities partially answers my key questions on how sampling and computational effectiveness.
    * I am looking forward to taking required coursework such as Probabilistic Models of Human and Machine Learning mathematical background and plenty of practical experience neccesary to start research.


