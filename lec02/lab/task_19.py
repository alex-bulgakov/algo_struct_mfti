#!/usr/bin/python3

from pyrob.api import *


def left():
    while True:
        if not wall_is_above():
            escape_left()
            break
        if wall_is_on_the_left():
            break
        move_left()


def right():
    while True:
        if not wall_is_above():
            escape_right()
            break
        if wall_is_on_the_right():
            break
        move_right()


def escape_right():
    while True:
        if wall_is_above():
            break
        move_up()
    while True:
        if wall_is_on_the_left():
            break
        move_left()
    global finish
    finish = True

def escape_left():
    while True:
        if wall_is_above():
            break
        move_up()
    global finish
    finish = True


finish = False

@task
def task_8_29():
    global finish
    finish = False
    while not finish:
        left()
        right()




if __name__ == '__main__':
    run_tasks()
