#!/usr/bin/env python
# -*- coding: utf-8 -*-

import framebuf
from random import randint

MAX_ITER = 80
realStart, realEnd = -2-.8, 2
imStart, imEnd = -1, 1
screen_width = 0
screen_height = 0


def init_brot(width, height):
    global screen_width, screen_height
    screen_width = width
    screen_height = height
    brotBitmap = bytearray(int(screen_width * screen_height / 8))
    return framebuf.FrameBuffer(brotBitmap, screen_width, screen_height, framebuf.MVLSB)


def update_brot():
    global realStart, realEnd, imStart, imEnd
    real = randint(10, 30) / 10
    realStart = -1 * real
    realEnd = real
    im = randint(10, 20) / 10
    imStart = -1 * im
    imEnd = im


def draw_brot(oled, brot_fb, res, switch_mode):
    brot_quit = False
    step = res
    for x in range(0, screen_width, step):
        if brot_quit: break
        xx = realStart + (x / screen_width) * (realEnd - realStart)
        for y in range(0, screen_height, step):
            if switch_mode():
                brot_quit = True
                break
            yy = imStart + (y / screen_height) * (imEnd - imStart)
            c = complex(xx, yy)
            m = mandelbrot(c)
            color = 1 - int(m / MAX_ITER)
            if res == 1:
                brot_fb.pixel(x, y, 1 if color > 0 else 0)
            else:
                brot_fb.fill_rect(x, y, res, res, 1 if color > 0 else 0)
        if not brot_quit:
            oled.blit(brot_fb, 0, 0)
            oled.show()
    if not brot_quit:
        oled.show


def mandelbrot(c):
    z, n = 0, 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n
