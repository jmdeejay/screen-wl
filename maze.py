#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from time import sleep
from random import randint, randrange

maze_quit = False
maze_width = 16
maze_height = 8
maze_size = maze_width * maze_height
screen_width = 0
screen_height = 0
maze_scale = 8

NORTH = 1
WEST = 2


def offset(coords):
    """ Converts [x,y] co-ords into an offset in the maze data """
    return ((coords[1] % maze_height) * maze_width) + (coords[0] % maze_width)


def coords(offset):
    """ Converts offset to [x,y] co-ords """
    return (offset % maze_width, offset // maze_width)


def neighbours(pos):
    neighbours = []
    if pos > maze_width:
        neighbours.append(pos - maze_width)
    if pos % maze_width > 0:
        neighbours.append(pos - 1)
    if pos % maze_width < maze_width - 1:
        neighbours.append(pos + 1)
    if pos + maze_width < maze_size:
        neighbours.append(pos + maze_width)
    return neighbours


def is_wall_between(data, p1, p2):
    """ Checks to see if there is a wall between two (adjacent) points
        in the maze. The return value will indicate true if there is a
        wall else false. If the points aren't adjacent, false is returned. """
    if p1 > p2:
        return is_wall_between(p2, p1)
    if p2 - p1 == maze_width:
        return data[p2] & NORTH != 0
    if p2 - p1 == 1:
        return data[p2] & WEST != 0
    return False


def knockdown_wall(data, p1, p2):
    """ Knocks down the wall between the two given points in the maze.
        Assumes that they are adjacent, otherwise it doesn't make any
        sense (and wont actually make any difference anyway) """
    if p1 > p2:
        return knockdown_wall(data, p2, p1)
    if p2 - p1 == maze_width:
        data[p2] &= WEST
    if p2 - p1 == 1:
        data[p2] &= NORTH


def init_maze(scr_width, scr_height):
    global maze_quit, screen_width, screen_height
    maze_quit = False
    screen_width = scr_width
    screen_height = scr_height


def generate_maze(switch_mode):
    global maze_quit
    data = [NORTH | WEST] * maze_size
    visited = {0: True}
    stack = [0]
    not_visited = lambda x: not visited.get(x, False)

    while len(stack) > 0:
        if switch_mode():
            maze_quit = True
            break
        curr = stack[-1]
        n = list(filter(not_visited, neighbours(curr)))
        sz = len(n)
        if sz == 0:
            stack.pop()
        else:
            np = n[randrange(sz)]
            knockdown_wall(data, curr, np)
            visited[np] = True
            if sz == 1:
                stack.pop()
            stack.append(np)
    return data


def draw_maze(oled, data, switch_mode):
    global maze_quit
    if maze_quit == False:
        oled.fill(0)
        for i in range(maze_size):
            if switch_mode():
                maze_quit = True
                break
            p1 = coords(i)
            x = p1[0] * maze_scale
            y = p1[1] * maze_scale
            if(0 <= x <= screen_width and 0 <= y <= screen_height):
                if data[i] & NORTH > 0:
                    oled.hline(x, y, maze_scale, 1)
                if data[i] & WEST > 0:
                    oled.vline(x, y, maze_scale, 1)
        if maze_quit == False:
            oled.rect(0, 0, maze_width * maze_scale, maze_height * maze_scale, 1)
            oled.show()
            sleep(0.1)


def maze_to_string(data):
    s = ""
    for y in range(maze_height):
        for x in range(maze_width):
            s += "+"
            if data[offset((x, y))] & NORTH != 0:
                s += "---"
            else:
                s += "   "
        s += "+\n"
        for x in range(maze_width):
            if data[offset((x, y))] & WEST != 0:
                s += "|"
            else:
                s += " "
            s += "   "
        s += "|\n"
    s += "+---" * maze_width
    s += "+\n"
    print(s)
