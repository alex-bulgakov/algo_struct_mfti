#!/usr/bin/python3

from pyrob.api import *

def up():
    while True:
        if wall_is_above(): break
        move_up()

def down():
    while True:
        if wall_is_beneath(): break
        move_down()

def left():
    while True:
        if wall_is_on_the_left(): break
        move_left()

def right():
    while True:
        if wall_is_on_the_right(): break
        move_right()


@task
def task_8_22():
    if not wall_is_above():
        up()
        if not wall_is_on_the_left():
            left()
        else:
            right()


if __name__ == '__main__':
    run_tasks()
