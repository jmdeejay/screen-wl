#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
from random import randint

gol_iteration = 300
gol_scale = 4
gol_quit = False
gol_width = 0
gol_height = 0
gol_size = 0
screen_width = 0
screen_height = 0


def get_flat_index(x, y, row, col):
    return ((int(x / gol_scale) + row) + ((int(y / gol_scale) + col) * gol_width)) % gol_size


def add_glider(x, y, board):
    board[get_flat_index(x, y, 2, 0)] = 1
    board[get_flat_index(x, y, 0, 1)] = 1
    board[get_flat_index(x, y, 2, 1)] = 1
    board[get_flat_index(x, y, 1, 2)] = 1
    board[get_flat_index(x, y, 2, 2)] = 1


def add_spinner(x, y, board):
    board[get_flat_index(x, y, 0, 0)] = 1
    board[get_flat_index(x, y, 1, 0)] = 1
    board[get_flat_index(x, y, 2, 0)] = 1


def add_gosper_glider_gun(x, y, board):
    board[get_flat_index(x, y, 1, 5)] = 1
    board[get_flat_index(x, y, 2, 5)] = 1
    board[get_flat_index(x, y, 1, 6)] = 1
    board[get_flat_index(x, y, 2, 6)] = 1
    
    board[get_flat_index(x, y, 13, 3)] = 1
    board[get_flat_index(x, y, 14, 3)] = 1
    board[get_flat_index(x, y, 12, 4)] = 1
    board[get_flat_index(x, y, 16, 4)] = 1
    board[get_flat_index(x, y, 11, 5)] = 1
    board[get_flat_index(x, y, 17, 5)] = 1
    board[get_flat_index(x, y, 11, 6)] = 1
    board[get_flat_index(x, y, 15, 6)] = 1
    board[get_flat_index(x, y, 17, 6)] = 1
    board[get_flat_index(x, y, 18, 6)] = 1
    board[get_flat_index(x, y, 11, 7)] = 1
    board[get_flat_index(x, y, 17, 7)] = 1
    board[get_flat_index(x, y, 12, 8)] = 1
    board[get_flat_index(x, y, 16, 8)] = 1
    board[get_flat_index(x, y, 13, 9)] = 1
    board[get_flat_index(x, y, 14, 9)] = 1
    
    board[get_flat_index(x, y, 25, 1)] = 1
    board[get_flat_index(x, y, 23, 2)] = 1
    board[get_flat_index(x, y, 25, 2)] = 1
    board[get_flat_index(x, y, 21, 3)] = 1
    board[get_flat_index(x, y, 22, 3)] = 1
    board[get_flat_index(x, y, 21, 4)] = 1
    board[get_flat_index(x, y, 22, 4)] = 1
    board[get_flat_index(x, y, 21, 5)] = 1
    board[get_flat_index(x, y, 22, 5)] = 1
    board[get_flat_index(x, y, 23, 6)] = 1
    board[get_flat_index(x, y, 25, 6)] = 1
    board[get_flat_index(x, y, 25, 7)] = 1
    
    board[get_flat_index(x, y, 35, 3)] = 1
    board[get_flat_index(x, y, 36, 3)] = 1
    board[get_flat_index(x, y, 35, 4)] = 1
    board[get_flat_index(x, y, 35, 4)] = 1


def init_gol(width, height):
    global gol_quit, screen_width, screen_height, gol_width, gol_height, gol_size
    gol_quit = False
    screen_width = width
    screen_height = height
    gol_width = int(width / gol_scale)
    gol_height = int(height / gol_scale)
    gol_size = int(gol_width * gol_height)
    
    choice = randint(0, 3)
    board = bytearray(gol_size)
    if choice == 0:
        for i in range(gol_size):
            board[i] = int(randint(0, 4) == 1)
    if choice == 1:
        add_glider(0, 16, board)
        add_glider(32, 32, board)
        add_glider(64, 16, board)
        add_glider(96, 32, board)
        add_glider(0, 48, board)
        add_glider(32, 64, board)
        add_glider(64, 48, board)
        add_glider(96, 64, board)
    elif choice == 2:
        add_spinner(16, 8, board)
        add_spinner(48, 16, board)
        add_spinner(80, 8, board)
        add_spinner(112, 16, board)
        add_spinner(0, 32, board)
        add_spinner(32, 48, board)
        add_spinner(64, 32, board)
        add_spinner(96, 48, board)
    elif choice == 3:
        add_gosper_glider_gun(0, 8, board)
    
    return board


def update_gol(board):
    new_board = bytearray()
    new_board[:] = board
    for i in range(gol_size):
        prev_row = i - gol_width
        next_row = i + gol_width
        total = int(board[prev_row - 1] + board[prev_row] + board[prev_row + 1] +
                    board[i - 1] + board[(i + 1) % gol_size] +
                    board[(next_row - 1) % gol_size] + board[next_row % gol_size] + board[(next_row + 1) % gol_size])
        if board[i] == 1:
            if (total < 2) or (total > 3):
                new_board[i] = 0
        else:
            if total == 3:
                new_board[i] = 1
    board[:] = new_board[:]


def draw_gol_intro(oled, switch_mode):
    global gol_quit
    for i in range(32):
        if switch_mode():
            gol_quit = True
            break
        oled.fill(0)
        title = "Game of Life"
        txt_x = int((screen_width - (len(title) * 8)) / 2)
        oled.text(title, txt_x, 5)
        str_loading = "Loading"
        dot = "."
        if i > 8: str_loading += dot
        if i > 16: str_loading += dot
        if i > 24: str_loading += dot
        oled.text(str_loading, 26, 28)
        oled.show()


def draw_gol(board, oled, switch_mode):
    global gol_quit
    if gol_quit == False:
        for i in range(gol_iteration):
            oled.fill(0)
            if gol_quit: break
            for j in range(gol_size):
                if switch_mode():
                    gol_quit = True
                    break
                left = (j % gol_width) * gol_scale
                top = math.floor(j / gol_width) * gol_scale
                if board[j] == 1:
                    if gol_scale == 1:
                        oled.pixel(left, top, 1)
                    else:
                        oled.fill_rect(left, top, gol_scale, gol_scale, 1)
            if gol_quit == False:
                oled.fill_rect(0, 0, int((i * screen_width) / gol_iteration), 1, 1)
                oled.show()
                update_gol(board)
