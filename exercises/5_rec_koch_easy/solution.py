from turtle import *



# speed(0)
tracer(0, 0)

""" The Koch Snowflake
  This fractal, also known as the Koch island or Koch Snowflake , was first
  described by Helge von Koch in 1904. It is built by starting with an
  equilateral triangle , removing the inner third of each side , building
  another equilateral triangle at the location where the side was removed ,
  and then repeating the process indefinitely .
        Level 0                Level 1             Level 2
          /\                    /\          (I can 't ascii this )
         /  \                  /  \
        /    \          ------/    \-----
       /      \         \               /
      /        \         \             /
     /          \         \           /
    /            \        /           \
   /              \      /             \
  /----------------\    /-----      ----\
                              \    /
                               \  /
                                \/

  Oneway to express this is the Lindenmayer rewrite system.
    Symbol    Meaning
    F         forward
    +         turn right 60 degrees
    -         turn left 60 degrees

  Koch Lindenmayer Algorithm
      K(N) = K' ++ K' ++ K'
      K'(0) = F
      K'(N) = K' - K' ++ K' - K'
  Implicit in each K' call is K '(N -1, length /3)
  http :// en. wikipedia .org / wiki / Koch_snowflake

  How does this pattern work ?
      Function K handles there being 3 original sides of an equilateral triangle .
      Function K' handles what happens on a side ( draw it , or recurse into pieces )

      There are 3 original sides so 3 calls to draw them (K' K' K ')
      Assume we start pointed to draw the first line .
      Its a 120 degree right turn to get from one line to the next .
      Thats how we get the "K' ++ K' ++ K '"

      When N is 0 ( the base case ), we just want to draw the line , not
      divide it up into pieces so "F"

      For a recursive case , we need to draw 4 pieces (K' K' K' K ').
            /
           /
    _____ /
    \
     \
      \
      /
     /
    /
      The turns between the pieces are: left 60, right 120 , and left 60 (- ++ -) so
      the pattern is "K' - K' ++ K' - K '".
"""

""" Koch Snowflake """
def koch (level , length ):
    # K(N) = K' ++ K' ++ K'
    kochH(level, length)
    right(120)
    kochH(level, length)
    right(120)
    kochH(level, length)

""" Helper function for the Koch Snowflake """
def kochH (level , length ):
    # Base case
    if level == 0:
        # K'(0) = F
        forward(length)

    # Recursive case
    else :
        # K'(N) = K' - K' ++ K' - K'
        kochH(level - 1, length/3)
        left(60)
        kochH(level - 1, length/3)
        right(120)
        kochH(level - 1, length/3)
        left(60)
        kochH(level - 1, length/3)

""" Try different levels of the snowflake."""
koch(5,300)

update()
input()
