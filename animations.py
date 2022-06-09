#!/usr/bin/env python
# -*- coding: utf-8 -*-

import framebuf
import math
from time import sleep
from random import randint
from img import robot_img, notes_img, nyan_img, mel_img, rpi_img, mario_img, toad_img

screen_width = 0
screen_height = 0
robot = None
note_t = 0
note1_fb = None
note2_fb = None
nyan = None
nyan_t = 0
nyan_x = -48
mel = None
rpi_fb = None
mario = None
mario2 = None
mario_x = -48
toad = None
toad_x = 48


def init_animations(width, height):
    global screen_width, screen_height
    screen_width = width
    screen_height = height


def load_images():
    global robot, note1_fb, note2_fb, nyan, mel, rpi_fb, mario, mario2, toad
    # python img2bytearray.py ./robot/ robot jpg 82 42 48
    robot = robot_img.get_robot()
    # python img2bytearray.py ./notes/ notes jpg 2 8 9
    note1_fb = notes_img.get_note1_fb()
    note2_fb = notes_img.get_note2_fb()
    # python img2bytearray.py ./nyan/ nyan jpg 12 48 32
    nyan = nyan_img.get_nyan()
    # python img2bytearray.py ./mel/ mel jpg 2 128 64
    mel = mel_img.get_mel()
    rpi_fb = rpi_img.get_rpi_fb()
    # python img2bytearray.py ./mario/ mario jpg 17 66 48
    mario = mario_img.get_mario()
    # python img2bytearray.py ./mario3/ mario jpg 3 30 48
    mario2 = mario_img.get_mario2()
    # python img2bytearray.py ./toad/ toad jpg 9 38 48
    toad = toad_img.get_toad()
    print("Images loaded")


def draw_robot(oled, switch_mode):
    global note_t
    robot_len = len(robot)
    for i in range(0, robot_len):
        if switch_mode(): break
        oled.fill(0)
        
        title = "Robot dance"
        txt_x = int((screen_width - (len(title) * 8)) / 2)
        oled.text(title, txt_x, 5)
        
        note_t += 5
        if (note_t > 1440): note_t = 0
        note_y = int(math.sin(note_t / 20.0) * 2) + 4
        oled.blit(note1_fb, 8, note_y)
        oled.blit(note2_fb, 112, note_y)
        oled.blit(framebuf.FrameBuffer(robot[i], 42, 48, framebuf.MONO_HLSB), 0, 16)
        oled.blit(framebuf.FrameBuffer(robot[(i + 30) % robot_len], 42, 48, framebuf.MONO_HLSB), 43, 16)
        oled.blit(framebuf.FrameBuffer(robot[(i + 60) % robot_len], 42, 48, framebuf.MONO_HLSB), 86, 16)
        oled.show()
        sleep(0.09)


def draw_nyan(oled, switch_mode):
    global nyan_x, nyan_t
    for i in range(0, len(nyan)):
        if switch_mode(): break
        nyan_x += 6
        nyan_t += 10
        if (nyan_x > screen_width + 10): nyan_x = -48
        if (nyan_t > 1440): nyan_t = 0
        nyan_y = int(math.sin(nyan_t / 20.0) * 6) + 24
        nyan_y2 = int(math.sin((nyan_t + 100) / 20.0) * 6) + 24
        oled.fill(0)
        oled.text("Nyan! Nyan! Nyan! Nyan! Nyan! Nyan! Nyan! Nyan!", -128 + nyan_x, 5)
        oled.blit(framebuf.FrameBuffer(nyan[i], 48, 32, framebuf.MONO_HLSB), nyan_x - 128, nyan_y)
        oled.blit(framebuf.FrameBuffer(nyan[i], 48, 32, framebuf.MONO_HLSB), nyan_x - 64, nyan_y2)
        oled.blit(framebuf.FrameBuffer(nyan[i], 48, 32, framebuf.MONO_HLSB), nyan_x, nyan_y)
        oled.blit(framebuf.FrameBuffer(nyan[i], 48, 32, framebuf.MONO_HLSB), nyan_x + 64, nyan_y2)
        oled.blit(framebuf.FrameBuffer(nyan[i], 48, 32, framebuf.MONO_HLSB), nyan_x + 128, nyan_y)
        oled.show()
        sleep(0.1)
        

def draw_mario(oled, switch_mode):
    global mario_x, toad_x
    for i in range(0, len(mario2)):
        if switch_mode(): break
        mario_x += 2
        toad_x += 2
        if (mario_x > screen_width): mario_x = -48
        if (toad_x > screen_width): toad_x = -48
        oled.fill(0)
        oled.text("It's a me Mario!", 0, 5)
        oled.blit(framebuf.FrameBuffer(mario2[i], 66, 48, framebuf.MONO_HLSB), mario_x, 16)
        oled.blit(framebuf.FrameBuffer(toad[round(i / 2.2)], 38, 48, framebuf.MONO_HLSB), toad_x, 16)
        oled.show()
        sleep(0.02)


def draw_mel(oled, switch_mode):
    choice = randint(0, len(mel) - 1)
    for _ in range (500): # Change choice every minute +/-
        if switch_mode(): break
        oled.fill(0)
        oled.blit(framebuf.FrameBuffer(mel[choice], 128, 64, framebuf.MONO_HLSB), 0, 0)
        oled.show()
        sleep(0.1)


def draw_memory_usage(oled, switch_mode, mem_free, mem_alloc):
    if not switch_mode():
        oled.fill(0)
        oled.blit(rpi_fb, 98, 16)
        oled.text("Raspberry Pi", 5, 5)
        oled.text("Memory usage", 5, 18)
        oled.text('Free: {:.1f}kb'.format(mem_free / 1024), 5, 36)
        oled.text('Total: {:.1f}kb'.format((mem_free + mem_alloc) / 1024), 5, 52)
        oled.show()
        sleep(0.1)
