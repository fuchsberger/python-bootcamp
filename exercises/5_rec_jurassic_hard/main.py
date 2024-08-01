from turtle import *

"""
THIS CODE MAKES A WRONG TURN SOMEWHERE. RUN LEVEL 3 TO SEE IT. PERHAPS YOU CAN FIX IT?
SEE THE JURRASIC IMAGES IN THE DAY 3 LECTURE PROJECT FOR AN IDEA WHAT IT SHOULD LOOK LIKE.

The Jurassic fractal is the one found on the Jurassic Park book and movie .
Encoded with 90 degree turns to the left and right
Rules :
    J(0) = Draw a line downwards from the point
    J(N) = J(N -1) + Draw R + Draw the opposite of the mirror image of level n -1

level 1 is R
level 2 is R R L
level 3 is RRL R RLL
level 4 is RRLRRLL R RRLLRLL and so on ...
"""

def jurassic (level , length ):
    jurH (level , length /( level +1) , "red ")
    speed (" fastest ")

def jurH (level , length , color ):
    if level == 0:
        pencolor ( color )
        forward ( length )
        print ('0: ' + color )
        return ""
    else :
        # level N -1
        string = jurH (level -1, length , jurColor ( color ))
        # Draw R
        pencolor ( color )
        jurDraw ("R", length )
        # Draw opposite , mirror image
        reverse = string [ -1:: -1]
        # opposite = [ jurOpposite (c) for c in reverse ]
        opposite = list (map( jurOpposite , reverse ))
        for i in range (len( opposite )):
            jurDraw ( opposite [i], length )
        # concatenate
        string = string + "R" + "". join ( opposite )
        print (str( level ) + ': ' + color + ", " + string )
        return string

def jurDraw (c, length ):
    if c == "R":
        right (90)
    else :
        left (90)
        forward ( length )

def jurOpposite (c):
    if c == "R": return "L"
    else : return "R"

def jurColor (c):
    if c == "red ": return " green "
    if c == " green ": return " blue "
    else : return " red "

speed('fastest')
jurassic(3,300)
#jurassic(9,200)
