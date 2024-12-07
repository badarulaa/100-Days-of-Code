# this script can run in reeborg.ca (section hurdle3)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# tips 1
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# tips 2
while not at_goal():
  if front_is_clear():
    move()
  else:
    jump()