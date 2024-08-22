from turtle import *

""" Sierpinski Gasket is a fractal which subdivides a triangle into inner
triangles recursively .
          Level 0                 Level 1                 Level 2
            /\                      /\                     /\
           /  \                    /  \                   /  \
          /    \                  /    \                 /----\
         /      \                /      \               / \  / \
        /        \              /--------\             /---\/---\
       /          \            / \      / \           / \      / \
      /            \          /   \    /   \         /---\    /---\
     /              \        /     \  /     \       /\  / \  / \  /\
    /----------------\      /-------\/-------\     /--\/---\/---\/--\
Draws a Sierpinski gasket to the given level of triangles . A triangle is
a set of points : (p1 , p2 , p3).

In the Sierpinski gasket , each triangle has another triangle in each of
its 3 corners . The 3 subtriangles and the unused space in the middle are
all the same size .

As a bonus , drawing the inner triangles will cover drawing the outer
triangle . Strategy : get to lower left corner of each recursive call
and recurse . When level is 0, draw the actual triangle .
"""

def sierpinski (level , length ):
    print ( level )
    if level == 0:
        left (60)
        forward ( length )
        right (120)
        forward ( length )
        right (120)
        forward ( length )
        right (180)
    else :
    # lower left recursion
        pencolor ("red")
        sierpinski (level -1, length /2)
        # upper recursion
        pencolor ("blue")
        penup ()
        left (60)
        forward ( length /2)
        right (60)
        pendown ()
        sierpinski (level -1, length /2)
        # lower right recursion
        pencolor ("black")
        penup ()
        right (60)
        forward ( length /2)
        left (60)
        pendown ()
        sierpinski (level -1, length /2)
        # back to the start
        penup ()
        backward ( length /2)
        pendown ()

#sierpinski(1,300)
sierpinski(4,300)
#sierpinski(4,300)
update()
