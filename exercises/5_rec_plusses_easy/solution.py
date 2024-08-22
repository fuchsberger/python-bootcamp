from turtle import *

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

def plusses (level , length , direction=None):
    # your code goes here
    # Any cool fractal full of plusses is a good fractal.
    # It does not need to look exactly like the description above.

    # you are at the midpoint of a plus facing -->
    # draw the plus with 4arms
    # forward ( length /2 - 5)
    # backward ( length - 10)
    # forward ( length /2 - 5)
    # right (90)
    # forward ( length /2 - 5)
    # backward ( length - 10)
    # forward ( length /2 - 5)
    # left (90)
    # # end at the midpoint, also pointing -->
    # return
    if level > 0:
        if direction != " right ":
            # to the left
            backward ( length /2)
            plusses (level -1, length /2, " left ")
            forward ( length /2)
        if direction != " left ":
            # to the right
            forward ( length /2)
            plusses (level -1, length /2, " right ")
            backward ( length /2)
        if direction != " down ":
            # upwards
            left (90)
            forward ( length /2)
            right (90)
            plusses (level -1, length /2, "up")
            right (90)
            forward ( length /2)
            left (90)
        if direction != "up":
            # downwards
            right (90)
            forward ( length /2)
            left (90)
            plusses (level -1, length /2, " down ")
            left (90)
            forward ( length /2)
            right (90)

plusses(4,300)

update()
