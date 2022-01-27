# Probability
* $P(A) = u(A)$
* $P(A \cup B)$, when $A,B$ disjoint, is $u(A)+u(B)$
* $P(A|B) = \dfrac{P(A \cap B)}{P(B)}$

* $P(B|A) = \dfrac{P(A \cap B)}{P(A)} = \dfrac{P(A|B)*P(B)}{P(A)}$

# GOMO
* Expand sample size of higher up nodes?

# Instructions
* Implement 2.5DEntity
  * Extend Plane class with some new properties
  * Orientation:
    * look at angle btw camera point and obj point, this is the new zero. The obj's rotation must be same as this angle for it to be zero
    * So to compute orientation, calculate the obj's angle orient from the new zero
    from math import atan2, degrees
    def angle_y(A,B):
      pos = A.world_position - B.world_position
      rotation_y = degrees(atan2(pos[0], pos[2]))
  * Update
  * Look at anim class
  * How to treat it like a entity, create an mesh with invisible with size of sprite
  * Add debug flat panel on bottom
  
# [] Ray collision adjust z cam  & Clamp further restrction on Z
* clone https://github.com/pokepetter/ursina/blob/master/ursina/prefabs/first_person_controller.py
* in init add default
self.maxz = maxz
* in update
ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
  if ray.hit: camera.z = ray.world_point.z
  else: camera.z = -6
* in update
adjust clamp -90, 90 to -70,70

# Cast
* p.rotation = rotation of camera

# SMALL
## static/dynamic entity: gravity
## Test LOS

* Highworkflow
userinput -> plyr entity (decouple mvment and things from frstp controller) (move,turn,jump,fall,cast)
(change state of plyr can happen anywhere)
(server,client)
To keep things smooth, both should be able to run task indep, and (merge their results)
Only server should handle critical data
anim


# Mindful
def input
def update


# Netcode Outline

it's essential streaming
Ah ok so this means all essential dynamic objects need to be stored in a data only container
  * how do you handle physics? doesn't matter as long as you keep track of orientation and moves

60 ticks
turn based Cn = move(Sn), S_c = update(Cn)
if C_c is missing apply last C_c
Need synced clock
sync - get latency send time+latency to client:set client IDX and State
whenever clientidx and servidx difference is too large, sync

