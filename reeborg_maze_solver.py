def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

        ## 📂 Project File
#  The solution is located in:
#    - `maze_solver.py`
#
# > ** Note: ** This code is designed  to run in ** Reeborg's World**. Functions such as `move()`, `turn_left()`, `front_is_clear()`, `right_is_clear()`, and `at_goal()` are provided by the Reeborg's World environment and will not work in a standard Python interpreter.

