$ \def\finv#1{ f^{-1}(#1) }$

# 0 Prereq and Prelim

## 0.1 Logic
* $A \implies B$

## 0.2 Set and Classes
* 2 relation = and membership
* Properties within =
>!* $A=A$
>!* $A=B \implies B=A$
>!* $A=B \land B=C \implies A=C$
* Properties between =,membership
  * $A=B \land x \in A \implies x \in B $
* Equivalent condition membership,=
>!* $ (x \in A \iff x \in B) \implies A=B $
>!* What about other direction? Property btw =,membership with reflexivity
* DEF Set: class A is a set iff $A \in B$ for class B
* REM Set Paradox
* $M = \{ X | X \not\in X \}$
* $M \in M$ or $M \not\in M$
* How does the distinction of proper class and set avoid the paradox?
* We are essentially saying, M does not belong in this discussion because it cannot be a member of a set
  * M cannot be X
* What does that mean for $M \in M$ or $M \not\in M$?
  * It says both these are false and, more importantly as a result of $M \not\in M$, M cannot be in M?
>!* This seems alot more clearer than it did when I first read it
>!* Koldobsky, to learn it and forget it
>!* To approach the problem with a fresh mind, you have no idea how important this is.
>!* How to get better at forgetting. Don't take yourself too seriously
* Notice that this paradox is playing off of the \in to draw a contradiction
* The paradox is of the form, $A \iff \neg A$

* $ A \implies \neg A$ This statement is false. Because when hyp is true, the conclusion is false

* DEF Subclass
* Another relation between classes, built around implication and membership
* REL equality and issubclass
* Operation: union, intersection, relative complement
  * DEF A union B := $\{x | x \in A or x \in B\}$
  * DEF A inter B := $\{x | x \in A and x \in B\}$
  * DEF A minus B := $\{x | x \in A and not x \in B\}$
  * DEF not A     := G-A
* Instance: Null set, family of set, set of all subsets
* Adjective: Disjoint

* not(AUB) = G-(AUB) = {x | x in G and not in (AUB)}
* ?? x not in (AUB) = x in G-(AUB)


* Ok, we just introduced alot of new names and things
* What statements describe their relations and properties?
* Let us first look at what each operation/thing exactly is
* How would we go about listing all possible combinations?

* x@n
* x@!x
* !(x@y)
* (x@y)#z



## Sets
* Null        := S
* U,I,-       := SxS -> S
* P           := S -> S
* =           := SxS -> st

Not for sets?

## Binary
* AND,OR,->,= := bxb -> b
* NOT         := b -> b

Statements are algebras of binary variables

## Statements
* AND,OR,->,= := stxst -> st
* NOT         := st -> st


* Examine the relationship between these and set operation.
* Construction of Not relationship for sets


# How to organize findings at high level and the work that went in?
* Organize the findings at high level,
* Organize the work patterns at a high level
* And forget it, dont hold on to too much

# Organization of ideas, heuristic
* HEUR What am I looking at, at a very abstract level?
* HEUR Is there a clear way to define all the combinations of things? How big should the combinations be?
* HEUR Negation Consider the negation. a and !a
* HEUR Relations of a,b: a=b, a~b 
* NOTE HEALTH&MENTAL I am pretty sure my need to reboot my brain is due to chemical imbalance/reinforced by bad reward loop. Which is why I think the advice of not taking oneself seriously is super important.
  * What to do when you find yourself in a bad state? 
  * Create new state. Formed by the same mechanism that you arrived to the bad state.
  * Identify bad feedback loops and stop em in the future.
    * Result based reward vs Effort/instrinsic value based reward
* HEUR Examples
* HEUR Questions
  * What do questions and examples do?
    * Examples are a bit clear. It is an estimation or a phenomenum. It is a specific thing.
      * Focuses attention on specific things.
    * Questions It asks for an answer. directs attention. Can be more open ended.
      * Advance the current attention towards another goal.
* HEUR Consider alternate forms of the same object
  * Question-noun, question,ask-verb, questionable-adj
* HEUR Negation Example, Negation Question
* HEUR What is the most abstract whay to look at
* HEUR What do you want? Specific examples. A model which satistfies the different examples.


* What I as primarly dealing with was imagination/intuition/examining the properties and consequences
  * Examine the pros/cons
* HEUR Goal oriented thinking. 
  * Gives you adrenaline/drive proximity to your goal
  * Cannot overdo it. Needs rest.

* DEF 2 statements are equal. f1(x,y,z) f2(a,b,c)
  * f1=f2 := f1(x,y,z,a,b,c) = f2(x,y,z,a,b,c)
    * In this approach you added more variables
  * f1=f2 := f1(x,y,z) <-> f2(a,b,c)
    * if f1 true then f2 true
    * if f2 true then f1 true
    * Since !(f1 true) is (f1 false), and using the contrapositives, A<->B !A<->!B
    * Does this definition give us the desired properties of equality?
    * A=A, A=B->B=A, A=B&B=C->A=C

* Transitive(implication) (A->B,B->C) -> (A->C)
* Associative(equality) &,| (A&B)&C=A&(B&C) 
* A&B->A,B
  * A&B->A, A&B->B
* A = T&A,T|A
* Knock out
  * T&B = B
  * F&B = F
  * T|B = T
  * F|B = B
  * ??? Woah, why is &,| similar
  A B A&B A|B
  T T  T   T
  T F  F   T
  F T  F   T
  F F  F   F
  * Its beautiful, the way it just works...

* Substitution A=B->A@C=B@C

* F(A) and !A->!F(A). Then A
  * T=A|!A

* __HEUR__ Statement/Argument simple and general as possible
* DEF Implication Linking. A, as a consequence we get B
  * A->B
  * ??? How do we formally formulate this?
    * Suppose A, and you find B to be true. Then you can write A->B
    * What do you mean by find? 
      * (Go back to the LOGIC TABLE representation) 
        * Is there a simpler representation instead of a full table? 
        * (describes some general property of how the table is formed)
          * Table has rows, we are interested in values of 1 row, given certain values
          * values on each cell can be T or F
          * writing A->B could be describing the behavior of the whole table... 
            * namely that when A is T, B is T over all the rows in the table
      * (Another functional/mapping representation)
        * Do we really need this 'row' can we just work with the variables?
        * Well, fundamentally the different variables form a table...?
        * well defined: each domain has single output -> the inverse is well defined
          * is there a better word? unique
          * In your table analogy, the rows have this property
            * Good, we isolated this critical property

* SHOW A&(B|C) = X
  * ->
    * APPROACH S1 -> A,B -> S2
    * A&(B|C) -> A,(B|C)
    * A=T, B=T&B -> B=A&B
    * B=A&B, C=A&C -> (B|C) = (A&B)|(A&C) = X
  * <- (NOTE My guess is that this direction is bit more complex)
    * (A&B)|(A&C)
    * Suppose !A. Then our statement becomes (F&B)|(F&C) = F|F =F, which cannot be.
      * ??? Why cannot be and consequently A=T? (Explain this to me again, this is quite fundamental)
      * You must make a distinction on what stating A means, ??? Why is it done in this style? what are the consquences of doing it in this style?
      * F(A). Suppose !A -> !F(A) ??? so the question is what is the gap that takes us 
      * contrapositive gives F(A)->A. (Dang really? this -> is really powerful) (Descriptor of LOGIC TABLE?)
      * NOTE: there is an alternate argument interpreting F as a mapping. well-defined properties as well
        * ??? Does it mean these two ideas are related?
        * Why ofcourse. The well-defined is what we need to form A->B=!B->!A
    * This means A=T. Then our statement becomes (T&B)|(T&C) = B|C
    * So we have A,B|C = A&(B|C)



* If you dont follow through what you believe in, and give up when its hard, what trials can you overcome?
* You will fail many times in life, when working on a difficult thing. 
  * If you stay down and don't get up, you will never improve.

* Don't loose sight of the forest for the trees
* Don't take yourself too seriously
  * Do not compare yourself to others. Focus on What YOU need to do to get to the next level

* What pleasure do you take? out of thinking about thses things?
  * Wouldn't you like to understand the motivating thoughts behind Groendick?
  * Or what he meant by a house and tools and framework?
  * I can only really experience these things when I am able-minded huh...
    * It's more of an experience than a achievement...

* HEUR It might be worthwile to write some key motivating examples to guide the thought process
* OH, don't i have... the lin alg stuff or alg stuff on a paper somewhere...
* HEUR Organize/Summarize your findings
  * I must admit, this is a key area which I have neglected over the years

# Functions
* class A,B domain and range
* assignment from domain to range
* f:A->B a->f(a)

* These representations are binary in nature
* AA, a->a

* does x->y represent an object?
* f(a) does, but this is not binary
* f(f(a))
* ??? Consider the notational difference of a->b and f(a)
* x->y->z
* g(f(a))
* operation on functions
* commutativity in a restricted system

* x->y, x<-y
* Inverse $finv{S}$
* $A \subset B$


* HEUR I feel overwhelmed when so many new ideas come and I cannot think of them carefully
  * It's a familiar feeling, when there is too much to handle
  * I just end up rushing through the important stuff
  * Often times I have given up... or just had forgetten or repressed. Why does this happen?
  * How can I over come?
  * Its ok to be wrong or to miss things. 
    * Try again and again until satistfactory
    * Try in an earnest manner, your heart must be in it.
    * Try whole-heartedly, towards a good direction
  * Be comfortable with an incomplete understanding.
    * As a student, you'll run into many abstract definitions: topological spaces, metric spaces, manifolds, the various structures of abstract algebra, and so on. 
    * In math, a definition is what it is, no more and no less. While it's very good to develop an intuition about these various objects, there's a danger of looking for some deeper meaning that just isnt there.
    * John von Neumann once said, In mathematics you don't understand things. You just get used to them.
    * I don't advise taking this quote too literally, but I think it reinforces the point of not worrying about understanding everything right away.


* Time pressure
* Fall in love with the process
* Be mindful of your motivation

* Two Phase:
  * On-Hand Chaotic Work Phase
  * Relaxed Quiet Review Reminiscence Phase

* Produce the best work in a chaotic environment?
* Aural, visual, kinesis, read, writing, thinking
* visual, kinesis, aural
