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

    # G(N) = G + G' ++ G' - G -- GG - G' +
    # Your recursive case goes here.

""" The helper function for the Gosper Curve """
def gosperH (level , length ):
    length = length / 2.6457
    # G'(0) = - F + F F ++ F + F -- F - F
    # Your base case goes here.

    # G'(N) = - G + G'G' ++ G' + G -- G - G'
    # Your recursive case goes here.

gosper(3,500)
#gosper(0,300).
