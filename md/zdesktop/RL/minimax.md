* DEF maximin value: highest value that the player can be sure to get without knowing the actions of other players
* $\displaystyle \min{a_{-i}}$
* $\underset{ a_{-i} }{min}$

* The min max algorithm uses maxmin

* Which move you would make as a maximizing player considering that your opponent also plays optimally?

* Suppose I am max. when would i not want to branch?
  * when the branching option is less than (the max options from this node)

* suppose I am min. when would i not want to branch?
  * when the branching option is greater than (the min options from this node)


* how about expanding the min/max options from this node to above this node?
* because if there are better options availble above, we dont need to consider going down, even if the options are better in the current node


Ok then from the perspectiveof max, min, we keep track of the best options avaiable for each player
maxbest, minbest

# Condition A
* so, when the next option is not better than maxbest/minbest we dont need to go

# Condition B
* also there is another place we dont need to look, where we can drop entire tree
* suppose we find a value that is (better, lower) than maxbest
  * then, the max will never choose the node we are on
* suppose we find a value that is (better, higher) than minbest
  * then min will never choose the node we are on

# Does condition B imply condition A
* suppose next option is not better the maxbest but we go there
* then this value is lower then maxbest 
  * then, max will never choose this node so it is doing the same thing


* if the next value is less than maxbest, (drop what do you mean drop?)
* if the next value is greater than minbest, (drop what do you mean drop?)

* What is relationship btw maxbest minbest?
* maxbest of current node comes from the collection of minbests in the next nodes
* minbest of current node comes from the collection of maxbests in the next nodes


* Pass the torch
* Lets go through it once more and think about how to optimizeit

* if we get a better maxbest then replace it as we go down
* Can we propagate this maxbest back up? yes as we return the values

* way to use different agents 
  * some agents require a tree, how to handle this?

* forced move
* minmax/BestMax, BestMin pruning
* transposition, not towards depth of tree
  * hashing for larger keys
  * Transposition doesn't work for MCST?
* is there a way to combine MCST with 

* Alof of these topics are related to how can we reduce the search tree

* mainly, because we don't have alot of time to spend iterating over

* What does AB-pruning do for tic tac, what are it's disadvantages
* Transpositions do work for MCST, you just can't  preserve 


