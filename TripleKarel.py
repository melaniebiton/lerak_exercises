from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


#the program starts with main
def main():
#testing the sides
    check_corners()
    check_corners()
    check_right()
    check_corners()
    check_corners()
    check_right()
    check_corners()
    check_corners()
    last_check_corners()


def last_check_corners():
    while left_is_blocked():
        put_beeper()
        move()

def last_corner():
    while left_is_blocked():
        put_beeper()
        move()
    turn_corner()
    if left_is_clear():
        move()
        put_beeper()
        move()
        move()
    if left_is_blocked():
       put_beeper()
    move()

def check_right():
    while left_is_blocked():
        put_beeper()
        move()
    turn_right()


def check_corners():
    while left_is_blocked():
        put_beeper()
        move()
    turn_corner()


def turn_corner():
    turn_left()
    move()
    put_beeper()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
