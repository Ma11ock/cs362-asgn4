#!/usr/bin/env python

# Generates a full name when given a first and last name.

# Get user's first name.
def getFirstName():
    return input("What is your first name?: ")

# Get user's last name.
def getLastName():
    return input("What is your last name?: ")

# Combine first and last name into one string.
def genName(str1, str2):
    return str1 + " " + str2
