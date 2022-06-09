#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gc
import math
import micropython
import framebuf, sys
import _thread
from time import sleep, ticks_ms
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C, PWM, ADC, RTC

from img import random_img
from animations import init_animations, load_images, draw_robot, draw_nyan, draw_mario, draw_mel, draw_memory_usage
from gol import init_gol, draw_gol_intro, draw_gol
from stars import init_stars, generate_stars, draw_stars
from matrix import init_matrix, draw_matrix
from maze import init_maze, generate_maze, draw_maze, maze_to_string
from invaders import init_invaders, draw_invaders_intro, draw_invaders, draw_invaders_game_over
from mandelbrot import init_brot, update_brot, draw_brot


# Led
def blink_led(time):
    sleep_time = 0.0001
    for _ in range(time):
        for duty in range(65025, 5):
            pwm.duty_u16(duty)
            sleep(sleep_time)
        for duty in range(65025, 0, -5):
            pwm.duty_u16(duty)
            sleep(sleep_time)


# Settings
def read_settings(filename):
    try:
        f = open(filename, "r")
        value = f.read()
        if value == "":
            value = "0"
        f.close()
        return int(value)
    except OSError:
        print("Config file does not exists.")
        return 0


def save_settings(filename):
    f = open(filename, "w")
    f.write(str(screen_mode))
    f.close()


# Screen
def init_screen():
    i2c_dev = I2C(1, scl=Pin(27), sda=Pin(26), freq=400000)
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    if i2c_addr==[]:
        print('No I2C Display Found')
        blink_led(4)
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))

    oled = SSD1306_I2C(screen_width, screen_height, i2c_dev)
    oled.invert(False)
    return oled


def switch_mode():
    global screen_mode
    if button.value() == 0:
        screen_mode += 1
        if (screen_mode > screen_mode_max): screen_mode = 0
        save_settings(config_filename)
        oled.fill(0)
        for i in range(0, len(random_arr) * 3):
            oled.blit(framebuf.FrameBuffer(random_arr[math.floor(i / 3)], 128, 64, framebuf.MONO_HLSB), 0, 0)
            oled.show()
        oled.fill(0)
        oled.show()
        return True
    return False


def display_screen():
    if screen_mode == 0: # Robot
        draw_robot(oled, switch_mode)
        
    elif screen_mode == 1: # Nyan
        draw_nyan(oled, switch_mode)
        
    elif screen_mode == 2: # Temperature + date + time
        if not switch_mode():
            reading = sensor_temp.read_u16() * conversion_factor
            temperature = 27 - (reading - 0.706) / 0.001721
            _time = rtc.datetime()
            date_str = "Date: {2:02d}/{1:02d}/{0:4d}".format(*_time)
            time_str = "Time: {:02d}:{:02d}:{:02d} {}".format(
                _time[4] % 12, _time[5], _time[6], "P" if (_time[4] > 12) else "A"
            )
            oled.fill(0)
            oled.text("Temp: {:.2f} *C".format(temperature), 0, 5)
            oled.text(date_str, 0, 25)
            oled.text(time_str, 0, 45)
            oled.show()
            sleep(0.1)

    elif screen_mode == 3: # Mario & Toad
        draw_mario(oled, switch_mode)

    elif screen_mode == 4: # Mel
        draw_mel(oled, switch_mode)

    elif screen_mode == 5: # Memory usage
        draw_memory_usage(oled, switch_mode, gc.mem_free(), gc.mem_alloc())

    elif screen_mode == 6: # Game of life
        board = init_gol(screen_width, screen_height)
        draw_gol_intro(oled, switch_mode)
        draw_gol(board, oled, switch_mode)

    elif screen_mode == 7: # Starfield
        init_stars(screen_width, screen_height)
        draw_stars(oled, stars, switch_mode)

    elif screen_mode == 8: # Matrix
        init_matrix(screen_width, screen_height)
        draw_matrix(oled, switch_mode)

    elif screen_mode == 9: # Maze
        init_maze(screen_width, screen_height)
        maze_data = generate_maze(switch_mode)
        draw_maze(oled, maze_data, switch_mode)

    elif screen_mode == 10: # Invaders
        init_invaders(screen_width, screen_height)
        draw_invaders_intro(oled, switch_mode)
        draw_invaders(oled, switch_mode)
        draw_invaders_game_over(oled, switch_mode)

    elif screen_mode == 11: # Mandelbrot
        update_brot()
        draw_brot(oled, brot_fb, 1, switch_mode)


# Led
led = Pin(25, Pin.OUT)
pwm = PWM(led)
pwm.freq(1000)

# Screen mode
config_filename = "config.ini"
screen_mode = read_settings(config_filename)
screen_mode_max = 11
random_arr = random_img.get_random()
button = Pin(16, Pin.IN, Pin.PULL_UP)

# Screen
screen_width = 128
screen_height = 64
oled = init_screen()

# Temperature
rtc = RTC()
sensor_temp = ADC(ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)

# Animations
init_animations(screen_width, screen_height)
load_images()

stars = generate_stars()
brot_fb = init_brot(screen_width, screen_height)

# Main
gc.enable()
pwm.duty_u16(32512)
while True:
    display_screen()
    gc.collect()
