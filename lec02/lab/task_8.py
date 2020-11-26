#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    while True:
        if wall_is_beneath() or wall_is_above():
            move_right()
        else:
            break


if __name__ == '__main__':
    run_tasks()
