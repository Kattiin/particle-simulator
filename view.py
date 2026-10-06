# Task (7/12): Draw on canvas
from tkinter import *
from model import *     # importerar alla funktioner från model
import time

root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600) # canvas is the entire big block of white the particle simulation will be displayed on, som en stor duk :)
canvas.pack()

# Task (8/12): Define a new function to_canvas_coords(canvas, x)
def to_canvas_coords(canvas, u):
    width = canvas.winfo_reqwidth()     # canvas width
    height = canvas.winfo_reqheight()   # canvas height

    scale =  height / 20                # scales the simulation coordinates 
    x = width / 2 + u.x * scale         # moves x = 0 to canvas center
    y = height / 2 - u.y * scale        # moves y = 0 to center and flips y-axis (vi vill ha vanliga x och y axlar med korrekt nollpunkt)

    return Vec(x,y)                     # returns the canvas coordinates


#######################################
### NB. Task 9 is done in model.py. ###
#######################################

# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(canvas, o, u1, u2):    # this function moves the oval o to a specific bounding box, given by two vectors u1 and u2.
    
    u1 = to_canvas_coords(canvas, u1)
    u2 = to_canvas_coords(canvas, u2)

    canvas.coords(o, u1.x, u1.y, u2.x, u2.y)    # canvas.coords() is a Tkinter Canvas method used to read/changes coords of existing objects

# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):                   
    u1, u2 = particle.bounding_box()                  
    o = canvas.create_oval(0, 0, 0, 0, fill="pink") 
    move_oval_to(canvas, o, u1, u2)                  # move it to particle position
    return o                                         

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):
    ovals = []                                      

    for particle in particles:                          # one oval for each particle
        ovals.append(create_oval(canvas, particle))

    last_update = time.time()

    while True:
        f(timestep, particles)                           # apply forces

        for particle in particles:                       # update the particle positions
            particle.inertial_move(timestep)

        current_time = time.time()

        if current_time - last_update >= 1/30:           # updating the display only when necessary

            for particle, oval in zip(particles, ovals):
                u1, u2 = particle.bounding_box()
                move_oval_to(canvas, oval, u1, u2)

            canvas.update()
            last_update = current_time
