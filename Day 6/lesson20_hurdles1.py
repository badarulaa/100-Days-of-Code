# this script can run in reeborg.ca (section hurdle1)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

blockade = 6
for i in range(blockade):
  jump()