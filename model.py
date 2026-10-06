import math

# All code related to vectors and particles

# Task (2/12): Define a class Vec
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):  # defines how the vector is displayed
        s = f"({self.x}, {self.y})"
        return s

    def __rmul__(self, factor):  # multiplies the vector by a number
        return Vec(factor * self.x, factor * self.y)

    def __add__(self, other):  # adds 2 vectors
        return Vec(other.x + self.x, other.y + self.y)

    def __sub__(self, other):  # subtracts 2 vectors
        return Vec(self.x - other.x, self.y - other.y)

    def norm(self):  # returns a vectors length
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_coords(self):  # returns x and y as a tuple
        return (self.x, self.y)


# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
    return u.x * v.x + u.y * v.y  # returns the dot product of two vectors (a number)


# Task (4/12): Create a class Particle
class Particle:
    def __init__(self, m, x, v, r):
        self.mass = m       # mass
        self.position = x   # position
        self.velocity = v   # velocity
        self.radius = r     # radius

    # Task (5/12): In the Particle class, implement a method inertial_move(self, dt).
    def inertial_move(self, dt):  # updates position
        self.position = self.position + dt * self.velocity

    # Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)
    def apply_force(self, dt, f):  # updates velocity
        self.velocity = self.velocity + (dt / self.mass) * f  # acceleration = f / self.mass, because f = ma

    # Task (9/12): In the Particle class, add a method bounding_box(self)
    def bounding_box(self):
        top_left = Vec(
            self.position.x - self.radius,
            self.position.y + self.radius
        )  # coordinates top left

        bottom_right = Vec(
            self.position.x + self.radius,
            self.position.y - self.radius
        )  # coordinates bottom right

        return top_left, bottom_right  # returns vectors of top left and bottom right corner of bounding box


##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################










###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################