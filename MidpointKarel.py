from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.

GOAL: Leave beeper in 
1) Fill bottom row with beepers

2) Then remove extreme end beepers 

3) You will get a string of beepers with one corner free of beeper on both ends

4) Now go in that string

5) Now remove extreme beepers one by one till no beeper will present

6) the final position of beeper will be center position then put a beeper
"""

def main():
    put_first_beeper()
    find_midpoint()


def put_first_beeper():
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()


def find_midpoint():
    move()
    while no_beepers_present():
        move()
        if beepers_present():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
            move()
            if beepers_present():
                pick_beeper()
                turn_around()
                move()
                turn_around()
            if front_is_blocked():
                    turn_around()






def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

