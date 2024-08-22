from turtle import *

""" Gosper curve
This produces a filled fractal rather than an outline. At level 2
and up, it produces a general shape like the Koch Snowflake.
Again, this algorithm uses the Lindenmayer rewrite system and has a
helper function. With each level, the length is divided by 2.6457.
  Symbol    Meaning
    F         forward
    +         turn right 60 degrees
    -         turn left 60 degrees
Forwards draws a line with length /2.6457.

Gosper Lindenmayer Algorithm
    G(0) = F + F ++ F - F -- FF - F +
    G(N) = G + G' ++ G' - G -- GG - G' +
    G'(0) = - F + F F ++ F + F -- F - F
    G'(N) = - G + G'G' ++ G' + G -- G - G'
http :// en. wikipedia .org / wiki / Flowsnake
"""

""" The Gosper Curve """
def gosper (level , length ):
    length = length / 2.6457
    # G(0) = F + F ++ F - F -- FF - F +
    # Your base case goes here.
    if level == 0:
        forward ( length )
        right (60)
        forward ( length )
        right (120)
        forward ( length )
        left (60)
        forward ( length )
        left (120)
        forward ( length )
        forward ( length )
        left (60)
        forward ( length )
        right (60)

    # G(N) = G + G' ++ G' - G -- GG - G' +
    # Your recursive case goes here.
    else:
        level = level - 1
        gosper (level , length )
        right (60)
        gosperH (level , length )
        right (120)
        gosperH (level , length )
        left (60)
        gosper (level , length )
        left (120)
        gosper (level , length )
        gosper (level , length )
        left (60)
        gosperH (level , length )
        right (60)

""" The helper function for the Gosper Curve """
def gosperH (level , length ):
    length = length / 2.6457
    # G'(0) = - F + F F ++ F + F -- F - F
    # Your base case goes here.
    if level == 0:
        left (60)
        forward ( length )
        right (60)
        forward ( length )
        forward ( length )
        right (120)
        forward ( length )
        right (60)
        forward ( length )
        left (120)
        forward ( length )
        left (60)
        forward ( length )

    # G'(N) = - G + G'G' ++ G' + G -- G - G'
    # Your recursive case goes here.
    else:
      level = level - 1
      left (60)
      gosper (level , length )
      right (60)
      gosperH (level , length )
      gosperH (level , length )
      right (120)
      gosperH (level , length )
      right (60)
      gosper (level , length )
      left (120)
      gosper (level , length )
      left (60)
      gosperH (level , length )

gosper(2,500)
#gosper(0,300).
