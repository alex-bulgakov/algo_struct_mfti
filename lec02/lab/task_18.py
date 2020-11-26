#!/usr/bin/python3

from pyrob.api import *

finish = False

def up():
    while True:
        if wall_is_above():
            break
        move_up()


def down():
    while True:
        if wall_is_beneath():
            break
        move_down()


def left():
    while True:
        if not wall_is_above():
            escape()
            break
        if wall_is_on_the_left():
            break
        move_left()


def right():
    while True:
        if not wall_is_above():
            escape()
            break
        if wall_is_on_the_right():
            break
        move_right()


def escape():
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



@task
def task_8_28():
    global finish
    finish = False
    while not finish:
        if not wall_is_on_the_left():
            left()
        elif not wall_is_on_the_right():
            right()
        else:
            break



if __name__ == '__main__':
    run_tasks()
