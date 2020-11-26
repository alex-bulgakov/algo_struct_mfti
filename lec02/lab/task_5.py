#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    while True:
        if not wall_is_on_the_right() and wall_is_beneath():
            move_right()
        else:
            break



if __name__ == '__main__':
    run_tasks()
