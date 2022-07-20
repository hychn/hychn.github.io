




# People
https://tlacombe.github.io/
if you intend studying TDA, you should really look at what the research team is actually doing. No one is an expert on all the aspects of TDA (the field goes from algebraic topology to Machine Learning, including statistics, algorithmic, etc.), so make sure that the research team current focus matches your interests.

# What do data scientist algorithm learner do?
Not really. Most data scientists and machine learning engineers implement pipelines of algorithms that already exist. Ive spent my career in research and development in a fairly mathematical field (geometry). While I have invented a couple new algorithms, at least 95% of my work over the past 10+ has involved implementing things that exist to solve new problems. Its a lot more value for your dollar if the data scientist finds a good solution that works for that problem rather than invents a new one.


# What do I need to know before going into a TDA 
It depends on the algorithm, and there are many these days. In general, a strong foundation in abstract algebra, linear algebra, topology, and algebraic topology are helpful for persistent homology. Morse functions are used in Mapper and Morse-Smale regression, and its helpful to know some differential topology and dynamic systems before delving into those algorithms.


# What are some applications where topological data analysis has an edge over other ML approaches?
Small data is one, particularly with a lot of observations. Complex survey data is another case in which statistical methods and many machine learning methods won't define and validate subscales for small data or unstructured surveys (see here: https://www.slideshare.net/ColleenFarrelly/hierarchical-clustering-for-psychometric-validation-76735689). Will have a paper out soon detailing this in gifted education research. Topology is particularly useful in extending extant statistical methods and tests.

Another is when extensive visualization of results is needed. Sometimes, a plot of Morse-Smale clusters from msr package in R is better than an MDS plot or overall random forest importance graph. This is particularly important within risk modeling, when a visual exploration may help an actuary understand different contributors to risk (see my Google Scholar profile for a paper on actuarial examples). With this function, it's probably useful in most data exploration problems.
