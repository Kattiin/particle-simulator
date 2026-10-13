

from view import *
from model import *

""" Experiment: Constant gravitational field.
This experiment will demostrate how particles with different 
masses behaves according to gravity.
All particles are expected to accelerate downwards
in the same speed and movement, disregarding their mass.

Observation:
Like expected, all three of the particles accelerated
and moved in the same pattern.
This corresponds to our prior statement, that gravitational
acceleration does not depend on mass.
According to Newton's second law, F = m*a.
Since gravity is F = m*g, we get a = g.

Timestep experiment:
We tested timestep = 0.01 and timestep = 0.1.
When we changed the timestep from 0.01 to 0.1, the 
speed of the particles increased.
This is a result of a larger timestep, which means
that more simulated time passes in each loop.
Consequently, the particles seem to move faster. 
The gravitational acceleration does not change,
but a larger timestep can reduce the accuracy
of the simulation.
A smaller timestep usually provides more accurate
results, although it requires more iterations to simulate
the same amount of time."""


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
