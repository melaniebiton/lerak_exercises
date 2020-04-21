from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    clear_one_row()
    clear_one_row()
    turn_left()
    finish_repair_column()
# code works in all worlds up to here
    hit_wall_turn()
# code works in all worlds up to here
    turn_left()
    finish_repair_column()
# code works in all worlds up to here
    next_column()
# code works in all worlds up to here
    finish_repair_column()
    turn_left()
    invert_beeper()
    finish_repair_column()
    dont_hit_wall()
    finish_repair_column()
    turn_left()

# karel turns, repairs column, turns around, repair column
# and go to next column
def clear_one_row():
    turn_left()
    finish_repair_column()
    dont_hit_wall()
    finish_repair_column()
    next_column()

# dont hit the wall karel
def dont_hit_wall():
    while front_is_blocked():
        turn_around()



# karelhitswallturnsandleavebeeperifthereisnone
def hit_wall_turn():
    while front_is_blocked():
        turn_left()
    if no_beepers_present():
        put_beeper()

# karelgoestonextcolumn4spacesaway
def next_column():
    turn_left()
    move()
    move()
    move()
    move()


# iffrontisclearfixbeepersincolumn
# beeperpresentkarelmovesifnotitsputsbeeper
def finish_repair_column():
    while front_is_clear():
        invert_beeper()
    if no_beepers_present():
        put_beeper()


# cleancolumnifnobeeperthenkarelputsbeeper
# ifbeeperthenkarelmoves
def invert_beeper():
    if no_beepers_present():
        put_beeper()
        move()
    else:
        move()

# karelturnsaround
def turn_around():
    turn_left()
    turn_left()

# karelturnsright
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
