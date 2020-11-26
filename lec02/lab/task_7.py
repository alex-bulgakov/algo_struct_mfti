#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while True:
        if not wall_is_beneath():
            move_down()
        else:
            while True:
                move_right()
                if not wall_is_beneath():
                    break
            move_down()
            while True:
                move_left()
                if wall_is_on_the_left():
                    break
            break


if __name__ == '__main__':
    run_tasks()
