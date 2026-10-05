import math

# All code related to vectors and particles

# Task (2/12): Define a class Vec
class Vec:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        s = f"({self.x}.{self.y})"
        return s

    def __rmul__(self, factor):
        return (factor * self.x, factor * self.y)

    def __add__(self, other):
        return (other + self.x, other + self.y)

    def __sub__(self, other):
        return (self.x - other, self.y - other)

    def norm(self):
        return math.sqrt((self.x ** 2 - self.y ** 2).norm())

    def get_coords(self):
        return (self.x, self.y)

# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
    pass

# Task (4/12): Create a class Particle
class Particle:
    def __init__ (self, m, x, v, r):
        self.m = m
        self.x = x
        self.v = v
        self.r = r

    def inertial_move(self, dt): # This method modifies the position attribute of a particle, over a small interval of time dt (t1 - t0).
        return dt * self.v + self.x

    def apply_force(self, dt, f): # This method modifies the velocity attribute of a particle, assuming a constant force f, over a small interval of time dt.
        return dt * self.x

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)

##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################