# 1. GROUPS
# 1.6 Symmetric, Alternating, and Dihedral Groups
* DEF Even/Odd permutation is written in even/odd number of transpositions
* THM A permutation can be just 1 of even or odd
* DEF $A_n$ set of all even permutations of $S_n$ where $n>2$
* PRP interesting property of transpositions
  * (bx)(ab) = (ab)(ax) [flipping]
  * (bx)(ab)(bx) = (ab)(ax)(bx) = (ab)(xab) = (ab)(abx) = (ax) [replacing a number in transposition form xtx]
  * (cb) (ab)(ac)(ab)(ac) (cb) = (ab)(ac)(ac)(ab)(ab)(ac) = (ab)(ac)
  * (ab) (ab)(ac)(ab)(ac) (ab) = (ac)(bc) = (cab)
* THM a 2-cycle in normal subgroup generates all 2-cycles
  * Let (ab) our 2 cycle, then multi by
  * (bx)(ab)(bx) = (ax)
* THM a 3-cycle in normal subgroup generates all 3-cycles
  * Let (abc) be our 3 cycle (ab)(ac)
  * (cx)(abc)(cx) = (cx)(ab)(ac)(cx) = (ab)(cx)(ac)(cx) = (ab)(ac)(ax)(cx) = (abc)(xac) is in N
  * $(abc)^{-1} \in N$ so $(abc)^{-1} (abc)(xac) = (xac) \in N$
* Carefully consider ALL the possibilties of the objects/properties of the objects you are working with. 
  * Once you have exhausted, you can explore including additional property/structure/restriction
* THM $A_n$ is normal subgroup of $S_n$ of index 2 with order $|S_n|/2$. $A_n$ is the only subgroup of $S_n$ of index 2.
  * normal is clear
  * index 2? is there some way to characterize even vs odd permuation? how about start with small case were we can definitely know n=2
    * we have I and (1,2). Now, lets extend this to n=3. How do we for all permutations of $S_3$ from $S_2$?
    * $|S_2|=2$ $|S_3|=3*2$
    * Alternate notation for $S_2$: [1,2] [2,1]


