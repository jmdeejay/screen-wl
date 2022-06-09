#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from random import randrange

max_depth = 32
num_stars = 192
stars_quit = False
stars_width = 0
stars_height = 0
t = 0;


def init_stars(width, height):
    global stars_width, stars_height, stars_quit
    stars_quit = False
    stars_width = width
    stars_height = height


def generate_stars():
    stars = []
    for _ in range(num_stars):
        star = [randrange(-25, 25), randrange(-25, 25), randrange(1, max_depth)]
        stars.append(star)
    return stars


def draw_stars(oled, stars, switch_mode):
    global t, stars_quit
    oled.fill(0)
    for star in stars:
        if switch_mode():
            stars_quit = True
            break
        star[2] -= 0.19
        if star[2] <= 0:
            star[0] = randrange(-25, 25)
            star[1] = randrange(-25, 25)
            star[2] = max_depth
        k = 64 / star[2]
        x = int(star[0] * k + (stars_width / 2) + 8)
        y = int(star[1] * k + (stars_height / 2))
        if 0 <= x < stars_width and 0 <= y < stars_height:
            size = int((1 - float(star[2]) / max_depth) * 4)
            oled.fill_rect(x, y, size, size, 1)
    if stars_quit == False:
        t += 1
        if (t > 1440): t = 0
        title = "Starfield"
        txt_x = int((stars_width - (len(title) * 8)) / 2)
        txt_y = int(((stars_height - 8) / 2) + math.sin(t / 20.0) * 4)
        oled.text(title, txt_x, txt_y)
        oled.show()
