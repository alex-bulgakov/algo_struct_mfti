#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    n = 9
    if wall_is_above() and wall_is_on_the_left():                       #top left
        for i in range(n):
            if wall_is_beneath() or wall_is_on_the_right(): break
            move_down()
            move_right()
    elif wall_is_above() and wall_is_on_the_right():                    #top right
        for i in range(n):
            if wall_is_beneath() or wall_is_on_the_left(): break
            move_down()
            move_left()
    elif wall_is_beneath() and wall_is_on_the_left():                     #bottom left
        for i in range(n):
            if wall_is_above() or wall_is_on_the_right(): break
            move_up()
            move_right()
    elif wall_is_beneath and wall_is_on_the_right():                    #bottom right
        for i in range(n):
            if wall_is_above() or wall_is_on_the_left(): break
            move_up()
            move_left()



if __name__ == '__main__':
    run_tasks()
