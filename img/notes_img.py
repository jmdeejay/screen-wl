#!/usr/bin/env python
# -*- coding: utf-8 -*-

import framebuf

def get_note1_fb():
    note1_buffer = bytearray(b"\x00\x0e:\"\"\"ff\x00")
    note1_fb = framebuf.FrameBuffer(note1_buffer, 8, 9, framebuf.MONO_HLSB)
    return note1_fb

def get_note2_fb():
    note2_buffer = bytearray(b"\x00\x08\x0c\x14\x10\x1000\x00")
    note2_fb = framebuf.FrameBuffer(note2_buffer, 8, 8, framebuf.MONO_HLSB)
    return note2_fb
