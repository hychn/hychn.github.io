# TODO: dont use rotation base, keep the base as the main obj and the quad as the side object
# TODO: This means re evaluating the statesystem of spr2d

from random import random

if (self.position - self.loci).distance() > roam.radius:
    d = (a.position-self.loci)
    d = Vec3( d[0]*random(),0,d[2]*random() )

# rearrange fball to include start_cast?

# what if we want the action to continue for some time, put a cd on changing the action

#def try_until( ):
    #pass

def update():
    self.action(actionparams)
    if mode1:
        change action/params based on conditions
    if mode2:

# tab system
