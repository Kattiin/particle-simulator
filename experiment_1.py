

from view import *
from model import *

# Experiment: Constant gravitational field
# We investigate how particles with different masses
# behave under gravity.
# We expect all particles to accelerate downwards
# at the same rate, regardless of their mass.

# Observation:
# All three particles fall downwards at the same rate,
# even though they have different masses.
#
# This is what we expected because gravitational
# acceleration does not depend on mass.
# According to Newton's second law, F = m*a.
# Since gravity is F = m*g, we get a = g.

# Timestep experiment:
# We tested timestep = 0.01 and timestep = 0.1.
#
# When we increased the timestep to 0.1, the particles
# appeared to fall faster on the screen.
#
# This happens because the simulation advances more
# time during each iteration.
#
# The gravitational acceleration remains the same,
# but a larger timestep can reduce the accuracy
# of the simulation.
#
# A smaller timestep generally gives more accurate
# results, but requires more iterations to simulate
# the same amount of time.



particles = [
    Particle(1, Vec(-5, 5), Vec(0, 0), 0.2),


    Particle(2, Vec(0, 5), Vec(0, 0), 0.2),
    Particle(3, Vec(5, 5), Vec(0, 0), 0.2)
]

timestep = 0.1

simulation_loop(
    constant_gravitational_field,
    timestep,
    particles
)
