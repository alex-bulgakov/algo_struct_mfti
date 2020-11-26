#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    flag1 = False
    flag2 = False
    while True:
        flag1 = wall_is_beneath()
        if not wall_is_on_the_right():
            move_right()
            flag2 = wall_is_beneath()
        if flag1 and not flag2: break


if __name__ == '__main__':
    run_tasks()
