#!/usr/bin/python3

from pyrob.api import *


def detect_direction():
    """

    :return: True if walls on Right, False if walls on Left
    """
    move_right()
    if wall_is_beneath():
        move_left()
        return True
    else:
        move_left()
        return False

@task
def task_5_2():
    while True:
        if not wall_is_on_the_right() and wall_is_beneath():
            move_right()
        else:
            break



if __name__ == '__main__':
    run_tasks()
