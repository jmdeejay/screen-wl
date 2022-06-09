#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from random import randint
from time import sleep

matrix_quit = False
matrix_x_scale = 16
matrix_y_scale = 8
matrix_width = 0
matrix_height = 0

matrix_clock = 0
matrix_population = []
matrix_max_population = 0
characters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
              "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
              "/", "!", "@", "#", "$", "%", "?", "&", "*", "(", ")", "{", "}", "[", "]")


def pseudo_norm(low_range, high_range):
    count = 10
    values = sum([randint(low_range, high_range) for x in range(count)])
    return round(values/count)


def increase_population():
    matrix_population.append([randint(0, int(matrix_width / matrix_x_scale)), 0, pseudo_norm(6, 12) / 10, randint(1, 4)])


def init_matrix(screen_width, screen_height):
    global matrix_quit, matrix_width, matrix_height, matrix_max_population
    matrix_quit = False
    matrix_width = screen_width
    matrix_height = screen_height
    matrix_max_population = int(matrix_width / matrix_x_scale) * 24


def draw_matrix(oled, switch_mode):
    global matrix_quit, matrix_clock, matrix_population
    matrix_clock += 1
    if matrix_clock >= sys.maxsize : matrix_clock = 0
    if matrix_clock % 2 == 0 or matrix_clock % 5 == 0:
        increase_population()
    
    oled.fill(0)
    for person in matrix_population:
        x, y, speed, loop = person
        if matrix_quit: break
        for i in range(0, loop):
            if switch_mode():
                matrix_quit = True
                break
            if 0 <= y * matrix_y_scale < matrix_height + (i * matrix_y_scale):
                letter_index = randint(0, len(characters) - 1)
                oled.text(characters[letter_index], int(x * matrix_x_scale), int((y - i) * matrix_y_scale))
        if 0 <= x * matrix_x_scale < matrix_width and matrix_quit == False:
            line_x = int((x * matrix_x_scale) - (matrix_x_scale / 4))
            line_len = int(loop * matrix_y_scale)
            line_y = int(y * matrix_y_scale) - line_len + matrix_y_scale
            oled.vline(line_x, line_y, line_len, 1)
            oled.vline(line_x + matrix_x_scale, line_y, line_len, 1)
        person[1] += speed
    
    if matrix_quit == False:
        while len(matrix_population) > matrix_max_population:
            matrix_population.pop(0)
        oled.show()
        sleep(0.1)
