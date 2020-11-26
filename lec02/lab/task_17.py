#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while True:
        if not wall_is_above():
            if cell_is_filled():
                move_left()
                if cell_is_filled():
                    break
                move_right()
                if cell_is_filled():
                    move_right()
                    break
            move_up()


if __name__ == '__main__':
    run_tasks()
