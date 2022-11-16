from itertools import product
import math

def bin_nbhd( x,y,z, binL, R):
    bx,by,bz =  x//binL*binL, y//binL*binL, z//binL*binL

    N = math.ceil(R/binL)
    N = range(-N,N+1)

    #return set( (binL*i, binL*j, binL*k) for i,j,k in product(N, N, N) )
    return [ (binL*i, binL*j, binL*k) for i,j,k in product(N, N, N) ]


x = bin_nbhd(0,0,0,5,10)
print(x)
#print( list(range(-1,1+1) ) )
