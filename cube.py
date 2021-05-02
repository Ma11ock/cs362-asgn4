#!/usr/bin/env python

# Calculate the volume of a cube.

# Get user's input on dimension of the cube.
# Intentional bug: it does not perform type checking.
def getUserInput():
    return int(input("What is the length/depth/width of the cube? "))

# Calculate the volume of the cube.
# Throw valueError if value is negative.
def calc(dimension):
    if dimension < 0:
        raise ValueError("No negative values.")
    else:
        return dimension ** 3

#print("The volume of the cube is: %d" % calc(getUserInput()))
