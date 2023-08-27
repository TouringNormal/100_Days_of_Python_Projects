# This is code for Reeborg's World website game. This code passes all 4 "Hurdles" using given function snippets
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle_jump():
    turn_left()
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while wall_in_front() != True:
        move()
    turn_left()


while at_goal() != True:
    while wall_in_front() != True:
        move()
        if at_goal() == True:
            done()
    hurdle_jump()
    