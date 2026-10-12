
# This file showcases the feature "circular arena" - walls.
# It uses the particle movement from experiment.inertial.py to showcase the walls function

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
