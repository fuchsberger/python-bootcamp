import turtle

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()

t.speed(0)

turtle.tracer(0, 0)


""" In the Plusses fractal , each plus arm has another plus on it. This means
that all 4 arms of the first plus have sub plusses but the remaining
plusses only grow new ones on the outer 3 arms .
          Level 0                Level 1
            |                      |
            |                  ----|----
            |                      |
            |                 |    |    |
    --------|--------     ----|----|----|----
            |                 |    |    |
            |                      |
            |                  ----|----
            |                      |

                        Level 2
                          |
                      ----|----
                          |
                     |    |    |
                 ----|----|----|----
                     |    |    |
               |          |            |
           ----|----      |        ----|----
        |      |          |            |      |
    ----|------|----------|------------|------|----
        |      |          |            |      |
           ----|----      |        ----|----
               |          |            |
               |          |            |
                 ----|----|----|----
                     |    |    |
                          |
                      ----|----
                          |
The new arms need to be drawn a bit less than the actual length so they
do not touch at the tips . The inner plusses do not completely redraw the
outer ones so we 'll have to draw all of them .

Notice that the recursion only happens in 3 directions except for the highest
level when it happens in 4 directions: "left", "right", "up", "down"

Each recursive call uses level -1, length /2, and a direction.
The first call to plusses doesn't need a direction since it draws all 4 arms.
"""

def plusses (level , length):
    # your code goes here
    # Any cool fractal full of plusses is a good fractal.
    # It does not need to look exactly like the description above.
    plussesH (level , length)
    t.right(90)
    plussesH (level , length)
    t.right(90)
    plussesH (level , length)
    t.right(90)
    plussesH (level , length)
    t.right(90)

def plussesH(level, length):
  if level == 0:
    t.forward(length)
    t.forward(-length)
  else:
    t.forward(length*2/3)
    t.left(90)
    # instead of

    # t.forward(length*1/3)
    # t.forward(-length*1/3)
    # do this
    plussesH(level-1, length/3)

    t.right(90)
    # t.forward(length*1/3)
    # t.forward(-length*1/3)
    plussesH(level-1, length/3)
    t.right(90)
    # t.forward(length*1/3)
    # t.forward(-length*1/3)
    plussesH(level-1, length/3)

    t.left(90)
    t.forward(-length*2/3)

plusses(2,300)

turtle.update()

screen.mainloop()
