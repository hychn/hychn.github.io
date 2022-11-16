from itertools import product
import math

def bin_nbhd( x,y,z, binL, R):
    bx,by,bz =  x//binL*binL, y//binL*binL, z//binL*binL

    N = math.ceil(R/binL)
    for i,j,k in product(range(N), range(N), range(N) ):
        print(i,j,k)


#bin_nbhd(0,0,0,2,10)
print( list(range(-1,1) )
