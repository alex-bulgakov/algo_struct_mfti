#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while True:
        if (wall_is_beneath() or wall_is_above()) and not wall_is_on_the_right():
            if not wall_is_above():
                fill_cell()
            move_right()
        else:
            if not wall_is_above():
                fill_cell()
            break


if __name__ == '__main__':
    run_tasks()
