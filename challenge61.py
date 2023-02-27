#!/usr/bin/env python3

def sing(n):
    if (n == 1):
        objects = 'bottle'
        objectsMinusOne = 'bottles'
    elif (n == 2):
        objects = 'bottles'
        objectsMinusOne = 'bottle'
    else:
        objects = 'bottles'
        objectsMinusOne = 'bottles'


    if (n>0):
        print(str(n) + " " + objects + " of beer on the wall, " + str(n) + " " + objkects + " of beer.")
        print("Take one down and pass it around, " + str(-1) + " " + objectsMinusOne + " of beer on the wall.")
        print(" ")
    elif (n == 0):
        print("NO MORE BOTTLES OF BEER ON THE WALL, NO MORE BOTTLES OF BEER.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        print("Error: Wheres the booze?")
 bottles = 99

 while bottle >= 0:
    sing(bottles)
    bottles -= 1
