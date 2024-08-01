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
    # This is the base case
    if level == 0:
        """
        Begins pointing like this -->
        Each angle of the triangle is 60 degrees.

        line #1   /\  line #2
          ^      /  \    |
          |     /    \   v
                -------
                line #3
                <-----

        Between each line turn left or right in increments of 60 for the next line.
        After the last line it points like this <---
        Turn it so it points like this ---> the same as when it started this base case.
        """
        left (60)
        forward ( length )
        right (120)
        forward ( length )
        right (120)
        forward ( length )
        right (180)
    else :
        """
        Begins pointing like this --> in the lower left corner of the triangle you are about to draw.
        Draws a lower left triangle, an upper triangle, and a lower right triangle
        The triangle drawing is done by making a recursive call for each one
                             /\     recursive
                            /--\    call #2
                recursive  /\   /\
                  call #1 /--\ /--\   recursive
                                      call #3

        Inbetween each recursive call, you need to move the turtle to the lower left corner of the next recursive triangle to be drawn. If you do not want to draw lines when you move the turtle, you
        can use these functions:
            penup()
            pendown()

        For extra coolness, set the color at the start of each of these 3 triangles
            pencolor(c) # color can be "red", "green", "blue", "black"
        """
        # lower left triangle. recursive call #1 goes here


        """
        Between the lower left triangle and the upper triangle, you are on the
        bottom left corner of the lower left triangle and pointing -->.
        You need to get to the bottom left corner of the upper triangle and again pointing -->.
        1) Turn left 60 degrees            /--> (step 3)
        2) go forwards length/2           /     (step 2)
        3) turn right 60 degrees      -->/      (step 1)
        Note: the steps are done in order 1, 2, 3. They happen to move the turtle upwards.
        """"
        # code to move from the lower left triangle to the upper triangle goes here

        # upper triangle. recursion call #2 goes here

        """
        Between the upper triangle and the lower right triangle, you are on the
        bottom left corner of the upper triangle and pointing -->.
        You need to get to the bottom left corner of the lower right triangle and again pointing -->.
        1) Turn right 60 degrees      -->\      (step 1)
        2) go forwards length/2           \     (step 2)
        3) turn left 60 degrees            \--> (step 3)
        This time the steps move the turtle downwards.
        """"
        # code to move from the upper triangle to the lower right triangle goes here

        # lower right triangle. recursive call #3 goes here

        """
        After the last triangle, you need to move the turtle back to where this function started.
        1) go backwards length/2                finishes -->--------------> starts
        The function to move backwards is
            backward(a distance)
        """
        # code to move the turtle back to the bottom left corner of the bottom left triangle goes here


#sierpinski(1,300)
sierpinski(2,300)
#sierpinski(4,300)
