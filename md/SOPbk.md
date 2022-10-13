* SIMPLE AND TO THE POINT
  * Be sparingly with the words
  * 1000words~

# Purpose ===========================================================================================================
* General questions and simple, natural ideas that form the answer; these things fascinate and bring me great joy.
  * Here are two examples I encountered, while working in the industry for the past three years.
  * First, while classifying and segmenting satellite images, I explored the simple ideas: Image processing kernels that modifies images(blur,outline,dialate), nonlinear-activation functions, gradient descent to adjust parameters of kernels.
    * It was very satistfying seeing such simple ideas work together to classify large areas of terrain accurately and much faster than human annotation.
  * Second, when handling complex input data with instrinsic structure, I learned to encode the input data to a smaller latent space. 
    * Then, the input representation was transformed with respect to the structure. 
    * When working with 3D robotic-arm in images or 3D structure in 1D protein sequences, these ideas allowed the AI to handle the complex input much more efficiently and observe the 3D structure's properties.

* How do you optimize a parameter that has no derivative? Does a local optimum exist at all?
  * This is a key question that I encountered many times, while finding: 
    * an optimal model architecture for predicting satellite images, loss function for protein structure prediction, different estimations of cost-to-go function in reinforcement learning.
* Searching and estimation by sampling are good, natural ideas that could answer this question.
* However, I was not satisfied with the simple but impractical approach, exhaustive sampling. It took so long!
* With more specific questions, I wish to explore this key question in more details:
  * Does an optimal solution exist? What are it's characteristics?
  * What different types of sampling and estimation can we form? What are the consequence of using each? Are some better than others?
  * Can we measure the quality of the estimation?
  * What are the meaningful conditions/situations, where stronger conclusions can emerge?

# Why this program ===================================================================================================
* UIUC 
* The CS PhD program at UIUC has 3 key characteristics that make it the top choice for me.
  * First, I am very interested in the type theoretical RL research by Professor Nan Jiang.
  * His papers, 'Towards Hyperparameter-free Policy Selection for Offline Reinforcement Learning' and 'A Few Expert Queries Suffices for Sample-Efficient RL with Resets and Linear Value Approximation'
    * provides ideas related to the key questions of optimizing a hyperparameters without a derivative.
  * Second, the course, 'Statistical Reinforcement Learning', will give me a solid background knowledge and experience with novel theoretical research as part of the final project component.
  * Finally, I appreciate the guidance of the Artificial Intelligence Qualifying Exam Committee where I will present my research with a background material tutorial really fosters.
  * I am warm-heartedly encouraged by the committee's goals to promote learning, diagnostic, and qualification.


# Why you are qualified (1-3) paragraphs ==============================================================================
* I am know that the program will be a challenging and require me to grow beyond my comfort zone.
* My experiences of overcoming difficulties in academics, industry, and self-study makes me well-prepared for this.

* In academdia, 
* Applied Mathematics and Computer Science master's degree gives me a strong background for applying logical and theoretical concepts.
  * Courses such as Linear Algebra, Algebra, Analysis, Operations Research provide a solid background to understand ideas at a fundamental level.
  * In master's thesis, analyzing protein structure using CNNs and persistant homology, gave me valuable interdisciplinary insight on how math and CS can compliment each other.
  * Futhermore, I found myself enjoying the many hours thinking, meditating, and exploring theoretical concepts and questions.

* In the industry,
* Working in the industry gave me valuable experience overcoming difficult problems and producing consistant results.
  * Here are three examples.
  * First, working on segmentation of satellite images gave me opportunity to read, implement from scratch, and benchmarked papers such as U-Net and Deep Aggregate Net.
    * The prototype and analysis data was used to win a major government contract for our company.
  * Second, while developing a semiconductor-robot monitoring prototype for SK hynix, I combined Novel View Synthesis CNN algorithm with pose estimation to track and pose the robot arm.
    * The prototype was used to automatically extract to extract key details from a complex semiconductor monitoring video: the position of the robotic arm, the various nozzles attached to the arm, when the nozzle was spraying a solution or not
  * Finally, predicting 3D structure from 1D protein sequences gave me experience of managing and finishing a complex project.
    * Filter and preprocess large datasets of 25,000 proteins in various formats with missing information.
    * Combined various neural network architectures such as, LSTM, CNNs, and ESM language models embeddings.
    * Research and experiment with distance, dihedral angle, frame-aligned point error functions.
    * Much more stable, consistant, and quickly converging model from the starting baseline, Recurrent Geometric Networks.
  * In these three cases I learned gained common insights that helped me break through challenges:
    * have cautious optimism that a nice-simple solution exists, focus on key objectives, and work at a steady-consistant pace

* In my self-studies, pursuing challenging independent research interests taught me discipline, self motivation and drive.
  * Studying the AlphaGoZero paper, I implemented a Monte Carlo Search Tree model-based RL to play variations of tic-tac-toe on longer length-to-win and boards.
  * It was very challenging to get the initial prototypes to work on larger variations of the game; I carefully and patiently tried many different ideas.
  * Eventually, reasonable success was found using: multi-step lookahead using model value estimation, augmentation of board inputs using rigid transformations, adjustments on rollout sample size depending on game depth, and many minor changes.
  * Wanting to underestand the RL the much better, I am studying the fundamentals of studying markov decision process programming and optimal control.


# Closing narrative ====================================================================================================
* AI is undeniably becoming more prevalent and widely-used in the industry. 
* By asking intriguing questions and finding simple, natural answers, I hope to contribute towards a more goal-aware and meaningful AI.
* Doing this brings great joy and satisfaction in my heart.

* _ have a fascniating program
* My mind, body and heart are ready
* Ever preparing, vigilant, rested-prepared, relentless.
* What else would I do but pursue that brings great joy and satisfaction in my heart?








# Goals
* Study the questions and related ideas. (how?)
* Explore and combine simple, natural ideas to answer these questions in theory and practice.
* Discovery new questions and be able to answer them with training
* ------------------------------------------------------------------------------------------------------
* I hope to explore these questions, break them down into simpler questions, restrict them under meaningful conditions.
* I hope to study the ideas and their inter-relationship. related to similar questions.
* ------------------------------------------------------------------------------------------------------
* Explore, Reframe, break down/restrict these questions, understand, discovery ideas and the relationships between them.
* And suggest simple, natural ideas that can answer these questions in practice.
* Theory-Application



# SCHOOL ALIGNMENT
* SELF/GOALS and ALIGNMENT
# QUALIFICATIONS
  * Practice reading applying papers
  * Implementing
# RESTATE PURPOSE

# PURPOSE
* Provoking questions and simple, natural ideas that form the answers; these are the things that fascinate and bring me great joy.
* Some of the ideas that I am fond of.
  * Minimizing loss w.r.t to convolution kernels (which are typically used for bluring, outline in image processing) gave way to Convolution Neural Networks, an extremly important type of network.
  * Encoding inputs into a latent space representation to analyze their distributions and combine them to create new output.
  * Invertible neural networks and finding inputs that can create the similar ouputs.
* Some of questions that were difficult and are unanswered. (why?, do these tie into a common theme?)
  * How to optimize parameters that are not differentiable? (hyper parameter optimization (landcover, protein struct losses combined learning rate). Reinforcement Learning)
    * MCST model, what was I doing? adjustments of rollout (prediction of v, rollout using v)
      * iterated rollout
    * (Efficiently train) Sample Efficiency of reinforcement Learning/ML
  * Estimation of function and achieving guarantees optimal cost bound 
  * Auxillary cost and relationship to true cost?



# THIS PROGRAM
* How does this program support your goal?
* COURSES, Professor, Plan

# QUALIFICATIONS
* How to reflect your character through these examples?
* Personal 
* Courses I have taken
* Work experience: Landcover, Pose Detection, Protein Structure Prediction

# PURPOSE
 
# RESUME Ideally, some of these items should also be properly linked with the statement of purpose document.
# MOTTO: I just need to get in anywhere: The most important thing is how I spend my time preparing and how ready I am and how I study there

# List of SCHOOLS
* Illinois Urbana Champaign
* Arizona State
* UMICH https://micde.umich.edu/methodology/optimization/
* Northwestern
* UNIFL https://www.eng.ufl.edu/ai-university/projects/foundations-of-ai/
* UNI Indiana https://luddy.indiana.edu/research/research-areas/ai-directory.html
* UNI KANSAS
* UNI Wisconsin Madison
* Ohio
* Colorado
* Nebraska
* UNC
* Georgia
* Texas
* California 
* Washington
* UNI Washington Mizou?
