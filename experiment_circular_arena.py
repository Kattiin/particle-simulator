
# This file showcases the feature "circular arena" - walls.
# It uses the particle movement from experiment.inertial.py to showcase the walls function

"""Experiment: Circular arena (Walls)

This experiment demonstrates how particles behave inside a
circular arena. The particles start in a circle and move
towards the center.

The particles move freely inside the arena, but when they cross the 
boundary, a spring-like force pushes them back
towards the center.

Expected result:
The particles should pass through the center and continue outwards
until they reach the wall. The wall force should
then slow them down and eventually push them back.

The strength of this force depends on the spring constant k
and how far the particles move outside the arena.

When a particle moves beyond the wall, a force pushes it back towards 
the center. The further it moves outside the boundary, the stronger 
the force becomes.
"""

from view import *
import math

R = 8 # radius of arena (TEST VALUE)
k = 5 # "spring" value of wall (TEST VALUE)

##########################################
# code from experiment_inertial.py:

n = 20
particles = []

for i in range(n):
    theta = i * 2 * math.pi / n

    u = Vec(math.cos(theta), math.sin(theta))

    pos = 6 * u
    vel = -1 * u

    particles.append(Particle(1, pos, vel, 0.2))

# end of code from experiment_inertial.py
##########################################

def arena_forces(dt, particles):
    circular_arena(dt, particles, k, R) # defines the forces acting on particles

walls(canvas, R) # draws the circular wall

simulation_loop(arena_forces, 0.01, particles) # starts the simulation
