#!/usr/bin/env python
# -*- coding: utf-8 -*-

import framebuf


def get_mario():
    mario_1_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x00\x06\x04\x00\x00\x18\x02\x00\x00 \x91\x00\x00BI\x00\x00\x85\xff\xc0\x01\x17\xff\xe0\x02/\xff\xe0\x02|\x03\xc0\x02\xf8!\x80\x07\xe0\xd9\x00\t\xe8\xd9\x00\x0c\xe0\xd9\x00\n\xfd@\xc0\tx\x00\xc0\x0c\xa5\xaa\xc0\x05/\xff\xc0\x03G\xff\xc0\x01\xa9\xff\x00\x00\xc5\xff\x00\x00x\x06\x00\x00\x87\xfe\x00\x01\x07\xfe\xe0\x02\x1f\x070\x02$\xc1\x90\x022\xc1P\x02H\x7f\xb0\x02U?\x90\x02\xa2\xae\xe0\x07hD\x80\x0f%\xee\x80\t\xff\xff\x80\r\xff\xff\x80\x0b\xff\xff\x00\t\xff\xff\x00\r\xff\xff\x00\x08\xe7\xfe\x00\n\xc7\xfc\x00\x08\x87\xfc\x00\t\x04\x83\x00\t\x06Q\x00\x0e\x05$\x80\x00\x04\x91\x80\x00\x07\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_2_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x00\x06\x04\x00\x00\x18\x02\x00\x00 \x91\x00\x00BI\x00\x00\x85\xff\xc0\x01\x17\xff\xe0\x02/\xff\xe0\x02|\x03\xc0\x02\xf8!\x80\x07\xe0\xd9\x00\t\xe8\xd9\x00\x0c\xe0\xd9\x00\n\xfd@\xc0\tx\x00\xc0\x0c\xa5\xaa\xc0\x05/\xff\xc0\x03G\xff\xc0\x01\xa9\xff\x00\x00\xc5\xff\x00\x01\xf2\x06\x00\x02?\xfe\x00\x04\x1f\xfe\x00\x08\x12g\xc0\x08)\x13 \x08*Y\xa0\x08!?`\x084\x9f \r\x15o`\x04O\xc7\xc0\x03/\xef\x00\x01\xff\xff\x00\x01\xff\xff\x00\x01\xff\xfe\x00\x00\xff\xfc\x00\x00\x7f\xf8\x00\x00?\xf0\x00\x00O\xe0\x00\x00g\xe0\x00\x00T \x00\x00I \x00\x00d\x10\x00\x00?\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_3_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x00\x06\x04\x00\x00\x18\x02\x00\x00 \x91\x00\x00BI\x00\x00\x85\xff\xc0\x01\x17\xff\xe0\x02/\xff\xe0\x02|\x03\xc0\x02\xf8!\x80\x07\xe0\xd9\x00\t\xe8\xd9\x00\x0c\xe0\xd9\x00\n\xfd@\xc0\tx\x00\xc0\x0c\xa5\xa9\xc0\x05/\xff\xc0\x03G\xff\xc0\x01\xa9\xff\x00\x00\xc5\xff\x00\x07\xf2\x0e\x00\x08?\xf8\x00\x08?\xf8\x00\x10\xc9\x1c\x00\x11R\x87\x00\x11$\x87\x80\x11\x92\xfe\xe0\x11I\xfe\xe0\x18\xd3} \n\xfe8 \t\xff|\xa0\x07\xff\xfe`\x07\xff\xfe \x07\xff\xfe\xa0\x07\xff\xfe\xa0\x07\xff\xfe`\x05\xfe\x1a\xc0\n\xfe\x07\x00\t\xfe\x00\x00\x0c\x18\x00\x00\n\x0c\x00\x00\x06\xa4\x00\x00\x01\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario = [mario_1_buffer, mario_2_buffer, mario_3_buffer, mario_2_buffer]
    return mario


def get_mario2():
    mario_1_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\x00\x00\x00\x00\x00\x00\x01\xaa\x00\x00\x00\x00\x00\x00\x00\x01h\x00\x00\x00\x00\x00\x00\x00\x03QL\x00\x00\x00\x00\x00\x00\x05\xb06\x00\x00\x00\x00\x00\x00\x05b/\x00\x00\x00\x00\x00\x00\x06\xb0\xfa\x00\x00\x00\x00\x00\x00\x05\xd8\xac\x00\x00\x00\x00\x00\x00\x06\xab\xd8\x00\x00\x00\x00\x00\x00\x05m`\x00\x00\x00\x00\x00\x00\x06\xd6\xa8\x00\x00\x00\x00\x00\x00\x03m\x80\x00\x00\x00\x00\x00\x00\x05\xb6\x9a\x00\x00\x00\x00\x00\x00\x02\xad\x10\x80\x00\x00\x00\x00\x00\x03\xf8\x04@\x00\x00\x00\x00\x00\x06\xaa@\x00\x00\x00\x00\x00\x00\x1f\xf0\x12\x80\x00\x00\x00\x00\x00\x15U\xab\x00\x00\x00\x00\x00\x00?\xf1}\x00\x00\x00\x00\x00\x00*\x18\xea\x00\x00\x00\x00\x00\x00?a>\x00\x00\x00\x00\x00\x00+\x08\x10\x80\x00\x00\x00\x00\x00\x1d\xaa\xe0 \x00\x00\x00\x00\x00\x06\x8f\xa4 \x00\x00\x00\x00\x00\x00u\xfb\xa0\x00\x00\x00\x00\x00\x00\xa2\xae\xc0\x00\x00\x00\x00\x00\x02\xc3\xfa\x00\x00\x00\x00\x00\x00\x02\x80\xd0\x00\x00\x00\x00\x00\x00\n\xc3\xb8\x00\x00\x00\x00\x00\x00\x02\x83\xf0\x00\x00\x00\x00\x00\x00\x01\x06\xb0\x00\x00\x00\x00\x00\x00\x00\x0b\xd0\x00\x00\x00\x00\x00\x00\x00\x1e8\x00\x00\x00\x00\x00\x00\x00h\x14\xc0\x00\x00\x00\x00\x00\x01\xb8\x0fp\x00\x00\x00\x00\x00\x01\xe0\x05\xd0\x00\x00\x00\x00\x00\x02\xf0\x07\xe0\x00\x00\x00\x00\x00\x01\xa8\x03@\x00\x00\x00\x00\x00\x01\xf8\x03\x80\x00\x00\x00\x00\x00\x01h\x01\x00\x00\x00\x00\x00\x00\x00\xf4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_2_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00\x00\x00\x01\xb8\x00\x00\x00\x00\x00\x00\x00\x02\xd2\x00\x00\x00\x00\x00\x00\x00\x03`x\x00\x00\x00\x00\x00\x00\x05D\xac\x00\x00\x00\x00\x00\x00\x06\xe0\xdc\x00\x00\x00\x00\x00\x00\x0bQt\x00\x00\x00\x00\x00\x00\r\xaa\xd8\x00\x00\x00\x00\x00\x00\x05k\xf0\x00\x00\x00\x00\x00\x00\x0bZ\x90\x00\x00\x00\x00\x00\x00\x05\xb7@\x00\x00\x00\x00\x00\x00\x06\xdd\xa4\x00\x00\x00\x00\x00\x00\x05j\x10\x80\x00\x00\x00\x00\x00\x03\xba\x92\x00\x00\x00\x00\x00\x00\x02\xd8\x00\x00\x00\x00\x00\x00\x00\x03\xb5\t@\x00\x00\x00\x00\x00\x06\xf0\x90\x00\x00\x00\x00\x00\x00\x0f\xb2\xa5\x80\x00\x00\x00\x00\x00\x1a\xe8\xfa\x00\x00\x00\x00\x00\x00\x17\xbc\xde\x00\x00\x00\x00\x00\x00\x1d\xd86\x00\x00\x00\x00\x00\x00\x17D\x98\x00\x00\x00\x00\x00\x00\x1d\xa2 \x00\x00\x00\x00\x00\x00\x07W\xe1 \x00\x00\x00\x00\x00\x00\xad^\xa0\x00\x00\x00\x00\x00\x00r\xf7@\x00\x00\x00\x00\x00\x02A\xd8\x00\x00\x00\x00\x00\x00\x05Ap\x00\x00\x00\x00\x00\x00\x02\x81\xdc\x00\x00\x00\x00\x00\x00\x03\x01x\x00\x00\x00\x00\x00\x00\x00\x03\xe8\x00\x00\x00\x00\x00\x00\x00\x05p\x00\x00\x00\x00\x00\x00\x00\x17\x1c\x00\x00\x00\x00\x00\x00\x00\xed\x0e\x00\x00\x00\x00\x00\x00\x01\xfc\x05\xf0\x00\x00\x00\x00\x00\x01h\x07\xd0\x00\x00\x00\x00\x00\x01\xf0\x03x\x00\x00\x00\x00\x00\x01X\x03\xe0\x00\x00\x00\x00\x00\x00\xf8\x02\x80\x00\x00\x00\x00\x00\x00\xec\x01\x00\x00\x00\x00\x00\x00\x008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_3_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x01\xb8\x00\x00\x00\x00\x00\x00\x00\x03@ \x00\x00\x00\x00\x00\x00\x06\xe4\xd8\x00\x00\x00\x00\x00\x00\x0b@\xb4\x00\x00\x00\x00\x00\x00\r`\xdc\x00\x00\x00\x00\x00\x00\n\xa1\xf0\x00\x00\x00\x00\x00\x00\r\xd2\xb0\x00\x00\x00\x00\x00\x00\x16\xab\xc0\x00\x00\x00\x00\x00\x00\x0bu`\x00\x00\x00\x00\x00\x00\r\xae\x90\x00\x00\x00\x00\x00\x00\n\xb7B\x00\x00\x00\x00\x00\x00\x06\xda\x88\x80\x00\x00\x00\x00\x00\x06\xad\x10\x00\x00\x00\x00\x00\x00\x03\xda\x12@\x00\x00\x00\x00\x00\x02\xf4@\x00\x00\x00\x00\x00\x00\x07Z\x89\x00\x00\x00\x00\x00\x00\x05\xf4\x82\x80\x00\x00\x00\x00\x00\x0fX\xfd\x00\x00\x00\x00\x00\x00\n\xf4n\x00\x00\x00\x00\x00\x00\x0f\xbd:\x00\x00\x00\x00\x00\x00\n\xec\x0c\x00\x00\x00\x00\x00\x00\x0f\xa0\xb0\x90\x00\x00\x00\x00\x00\x05\xedP \x00\x00\x00\x00\x00\x03S\xef\xc0\x00\x00\x00\x00\x00\x00>\xba\xa0\x00\x00\x00\x00\x00\x05@\xec\x00\x00\x00\x00\x00\x00\x02\xa0\xb8\x00\x00\x00\x00\x00\x00\x01\xc0\xfc\x00\x00\x00\x00\x00\x00\x02\x00\xd4\x00\x00\x00\x00\x00\x00\x00\x01|\x00\x00\x00\x00\x00\x00\x00\x01\xd8\x00\x00\x00\x00\x00\x00\x00&\xde\x00\x00\x00\x00\x00\x00\x00{\x83\x00\x00\x00\x00\x00\x00\x00\xbe\x02\x00\x00\x00\x00\x00\x00\x00\xe8\x01\xe0\x00\x00\x00\x00\x00\x00x\x01\xf8\x00\x00\x00\x00\x00\x00\xd8\x01\xb4\x00\x00\x00\x00\x00\x00t\x01\xf8\x00\x00\x00\x00\x00\x00x\x03T\x00\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_4_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00u\x00\x00\x00\x00\x00\x00\x00\x00\\\x00\x00\x00\x00\x00\x00\x00\x01\xaa@\x00\x00\x00\x00\x00\x00\x01h\x0c\x00\x00\x00\x00\x00\x00\x01\xb5\x16\x00\x00\x00\x00\x00\x00\x02\xd8;\x00\x00\x00\x00\x00\x00\x02\xa8.\x00\x00\x00\x00\x00\x00\x01\xb6z\x00\x00\x00\x00\x00\x00\x02\xdb\xac\x00\x00\x00\x00\x00\x00\x01mp\x00\x00\x00\x00\x00\x00\x01\xab\xd2\x00\x00\x00\x00\x00\x00\x01mH\x00\x00\x00\x00\x00\x00\x00\xb7F\x80\x00\x00\x00\x00\x00\x00\xdbP \x00\x00\x00\x00\x00\x00\xf6\x84\x80\x00\x00\x00\x00\x00\x01\xbd\x00 \x00\x00\x00\x00\x00\x03\xd6R@\x00\x00\x00\x00\x00\x03}4\x80\x00\x00\x00\x00\x00\x05\xd6:\x80\x00\x00\x00\x00\x00\x07}\x17\x80\x00\x00\x00\x00\x00\x05\xda\r\x00\x00\x00\x00\x00\x00\x07n\xa8\x00\x00\x00\x00\x00\x00\x02\xf1 \x00\x00\x00\x00\x00\x00\x03\xa5\xf0\x00\x00\x00\x00\x00\x00\x00\xd1P@\x00\x00\x00\x00\x00\x00\x03m`\x00\x00\x00\x00\x00\x00M\xfa\x80\x00\x00\x00\x00\x00\x00V\xbc\x00\x00\x00\x00\x00\x00\x00\xa9\xe8\x00\x00\x00\x00\x00\x00\x00P\xbc\x00\x00\x00\x00\x00\x00\x00\xa1\xec\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x11\xa8\x00\x00\x00\x00\x00\x00\x00.\xf8\x00\x00\x00\x00\x00\x00\x00?\x8e\x00\x00\x00\x00\x00\x00\x005\x04\x00\x00\x00\x00\x00\x00\x00>\x0e\x00\x00\x00\x00\x00\x00\x00.\x1f\xc0\x00\x00\x00\x00\x00\x00:\x17@\x00\x00\x00\x00\x00\x00,\x1d\xc0\x00\x00\x00\x00\x00\x00\x18\x1f@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_5_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xe0\x00\x00\x00\x00\x00\x00\x00\r \x00\x00\x00\x00\x00\x00\x00\x15\xc2\x00\x00\x00\x00\x00\x00\x00\x1a\x88\x00\x00\x00\x00\x00\x00\x00.\x80\x00\x00\x00\x00\x00\x00\x003A\x00\x00\x00\x00\x00\x00\x00-\x85\xe0\x00\x00\x00\x00\x00\x00Z\xc6\xb0\x00\x00\x00\x00\x00\x00.\xbb\xf0\x00\x00\x00\x00\x00\x005\xd6\x80\x00\x00\x00\x00\x00\x00*\xba\x00\x00\x00\x00\x00\x00\x00=\xac\x80\x00\x00\x00\x00\x00\x00&\xf0\xa0\x00\x00\x00\x00\x00\x00\x1b@\x80\x00\x00\x00\x00\x00\x00\x1d\xd4\x10\x00\x00\x00\x00\x00\x007\x01\x04\x00\x00\x00\x00\x00\x00}\x91(\x00\x00\x00\x00\x00\x00\xd7\x0e\x08\x00\x00\x00\x00\x00\x01\xfd#\xf4\x00\x00\x00\x00\x00\x01W\x81\xb0\x00\x00\x00\x00\x00\x01\xfbI\xc0\x00\x00\x00\x00\x00\x01Y\x81\x00\x00\x00\x00\x00\x00\x01\xea$\x00\x00\x00\x00\x00\x00\x01y\xb8\x00\x00\x00\x00\x00\x00\x00\xd4\xe8\x00\x00\x00\x00\x00\x00\x00 \xba\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x01V@\x00\x00\x00\x00\x00\x00\x03\xfb\x00\x00\x00\x00\x00\x00\x00\x12\xb5\x00\x00\x00\x00\x00\x00\x00\r\xf8\x00\x00\x00\x00\x00\x00\x00\x15\xa8\x00\x00\x00\x00\x00\x00\x00\x08\xf8\x00\x00\x00\x00\x00\x00\x00\x16h\x00\x00\x00\x00\x00\x00\x00\x1f\xb0\x00\x00\x00\x00\x00\x00\x00\n\xe0\x00\x00\x00\x00\x00\x00\x00\x1f`\x00\x00\x00\x00\x00\x00\x00\r\xc0\x00\x00\x00\x00\x00\x00\x00\x0fx\x00\x00\x00\x00\x00\x00\x00\x1a\xec\x00\x00\x00\x00\x00\x00\x00\x0c\xbc\x00\x00\x00\x00\x00\x00\x00\x08\xf6\x00\x00\x00\x00\x00\x00\x00\x00\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_6_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01P\x00\x00\x00\x00\x00\x00\x00\x06\xe0\x00\x00\x00\x00\x00\x00\x00\x0b@\x00\x00\x00\x00\x00\x00\x00\x1dD\x00\x00\x00\x00\x00\x00\x00+\x00\x00\x00\x00\x00\x00\x00\x00-\x88\xc0\x00\x00\x00\x00\x00\x005Ap\x00\x00\x00\x00\x00\x00-\x86\xd0\x00\x00\x00\x00\x00\x006\xe5\xe0\x00\x00\x00\x00\x00\x00[_\x00\x00\x00\x00\x00\x00\x00*\xb5@\x00\x00\x00\x00\x00\x006\xda\x00\x00\x00\x00\x00\x00\x00+t\x80\x00\x00\x00\x00\x00\x00=\xa1\x00\x00\x00\x00\x00\x00\x00*\xd0\xa0\x00\x00\x00\x00\x00\x00\x1f\xa4\x08\x00\x00\x00\x00\x00\x00:\x80\x80\x00\x00\x00\x00\x00\x00o\x12 \x00\x00\x00\x00\x00\x00\xfbG\x08\x00\x00\x00\x00\x00\x01\xad\r\xb0\x00\x00\x00\x00\x00\x01\xfb!\xf0\x00\x00\x00\x00\x00\x01S\x81@\x00\x00\x00\x00\x00\x03\xf2\n\x00\x00\x00\x00\x00\x00\x00\xa8\xa8\x00\x00\x00\x00\x00\x00\x01\xfax\x00\x00\x00\x00\x00\x00\x00\xa0\xdc\x00\x00\x00\x00\x00\x00\x00\x01\xb4\x00\x00\x00\x00\x00\x00\x00\x02\xfa\x00\x00\x00\x00\x00\x00\x00\x03\xad\x00\x00\x00\x00\x00\x00\x00\x02\x9b\x00\x00\x00\x00\x00\x00\x00\x01\xe6\x00\x00\x00\x00\x00\x00\x00\x01Y\x00\x00\x00\x00\x00\x00\x00\x00\xa8\x00\x00\x00\x00\x00\x00\x00\x00\xa8\x00\x00\x00\x00\x00\x00\x00\x01\xb8\x00\x00\x00\x00\x00\x00\x00\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x03\xf0\x00\x00\x00\x00\x00\x00\x00\x06\xa0\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x03`\x00\x00\x00\x00\x00\x00\x00\x03\xd0\x00\x00\x00\x00\x00\x00\x00\x02\xf8\x00\x00\x00\x00\x00\x00\x00\x03\xb8\x00\x00\x00\x00\x00\x00\x00\x03\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_7_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x03\xb0\x00\x00\x00\x00\x00\x00\x00\r@\x00\x00\x00\x00\x00\x00\x00\n\x82\x00\x00\x00\x00\x00\x00\x007\x88\x00\x00\x00\x00\x00\x00\x00*\x80\x80\x00\x00\x00\x00\x00\x006\x8a\xe0\x00\x00\x00\x00\x00\x00Z\x83P\x00\x00\x00\x00\x00\x00k\xcd\xf0\x00\x00\x00\x00\x00\x006v\xa0\x00\x00\x00\x00\x00\x00[\xad\x80\x00\x00\x00\x00\x00\x00j\xb6@\x00\x00\x00\x00\x00\x006\xda\x00\x00\x00\x00\x00\x00\x00[q\x00\x00\x00\x00\x00\x00\x005\xd1@\x00\x00\x00\x00\x00\x00.\xc1\x10\x00\x00\x00\x00\x00\x00;H\x00\x00\x00\x00\x00\x00\x00/\x02H\x00\x00\x00\x00\x00\x00\xfa\x91\x00\x00\x00\x00\x00\x00\x00\xaf\x05\x10\x00\x00\x00\x00\x00\x01\xfd\x97P\x00\x00\x00\x00\x00\x02\xa3\x82\xe0\x00\x00\x00\x00\x00\x03\xea\t\xc0\x00\x00\x00\x00\x00\x02\xb2E\x00\x00\x00\x00\x00\x00\x03\xd4\xb4\x00\x00\x00\x00\x00\x00\x01px\x00\x00\x00\x00\x00\x00\x00\xc1\xac\x00\x00\x00\x00\x00\x00\x00\x02\xf8\x00\x00\x00\x00\x00\x00\x00\x03\xb6\x80\x00\x00\x00\x00\x00\x00\x06\xbd@\x00\x00\x00\x00\x00\x00\x06\xd6\x80\x00\x00\x00\x00\x00\x00\x05z\xc0\x00\x00\x00\x00\x00\x00\x05\xb4\x80\x00\x00\x00\x00\x00\x00\x02\xb8\x00\x00\x00\x00\x00\x00\x00\x03l\x00\x00\x00\x00\x00\x00\x00\x02\xac\x00\x00\x00\x00\x00\x00\x00\x03L\x00\x00\x00\x00\x00\x00\x00\x05\x1c\x00\x00\x00\x00\x00\x00\x00\x074\x00\x00\x00\x00\x00\x00\x00\x04~\x00\x00\x00\x00\x00\x00\x00\x0f,\x00\x00\x00\x00\x00\x00\x00\x15\x9e\x00\x00\x00\x00\x00\x00\x00\x1fN\x00\x00\x00\x00\x00\x00\x00\x1b\xc4\x00\x00\x00\x00\x00\x00\x00\x0e\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_8_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x00\x00\x00m\x80\x00\x00\x00\x00\x00\x00\x00V\x80\x00\x00\x00\x00\x00\x00\x00\xda \x00\x00\x00\x00\x00\x00\x00\xb6\x00\x00\x00\x00\x00\x00\x00\x01Z\x9f\x00\x00\x00\x00\x00\x00\x01\xea\x15\x80\x00\x00\x00\x00\x00\x01-^\x80\x00\x00\x00\x00\x00\x01\xd6\xeb\x00\x00\x00\x00\x00\x00\x01{^\x00\x00\x00\x00\x00\x00\x01J\xe8\x00\x00\x00\x00\x00\x00\x01\xb7j\x00\x00\x00\x00\x00\x00\x01[\xa0\x00\x00\x00\x00\x00\x00\x00\xedJ\x00\x00\x00\x00\x00\x00\x00\xb7H\x80\x00\x00\x00\x00\x00\x00\xdd\x04 \x00\x00\x00\x00\x00\x00\xf6!\x00\x00\x00\x00\x00\x00\x03\xba\x08 \x00\x00\x00\x00\x00\x02\xdc@\x80\x00\x00\x00\x00\x00\x07\xea\n@\x00\x00\x00\x00\x00\x05|O\x80\x00\x00\x00\x00\x00\x07\x825\x00\x00\x00\x00\x00\x00\r\xa8\n\x00\x00\x00\x00\x00\x00\x06\xc5,\x00\x00\x00\x00\x00\x00\x03\xa1\xa8\x00\x00\x00\x00\x00\x00\x00\x00\xf4\xa0\x00\x00\x00\x00\x00\x00\x07\xb5\x80\x00\x00\x00\x00\x00\x00\x0e\xf6\xd0\x00\x00\x00\x00\x00\x00\x08\xda\xa0\x00\x00\x00\x00\x00\x00\x19y\x00\x00\x00\x00\x00\x00\x00\x0c\xdc\x00\x00\x00\x00\x00\x00\x00\x15p\x00\x00\x00\x00\x00\x00\x00\x17\xd0\x00\x00\x00\x00\x00\x00\x00*\xf8\x00\x00\x00\x00\x00\x00\x00\x1a\xac\x00\x00\x00\x00\x00\x00\x00\x07\x1c\x00\x00\x00\x00\x00\x00\x00\x05\r\x00\x00\x00\x00\x00\x00\x00>\x0e\x80\x00\x00\x00\x00\x00\x00t\x0b\x80\x00\x00\x00\x00\x00\x00^\x0f\x80\x00\x00\x00\x00\x00\x00{\x1d\x00\x00\x00\x00\x00\x00\x007\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_9_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\x00\x00\x00\x00\x00\x00\x00\xa8\x80\x00\x00\x00\x00\x00\x00\x03\xb2\x10\x00\x00\x00\x00\x00\x00\x02\xd0(\x00\x00\x00\x00\x00\x00\x05X~\x00\x00\x00\x00\x00\x00\x06\xd4\xd5\x00\x00\x00\x00\x00\x00\x0bk~\x00\x00\x00\x00\x00\x00\n\xbd\xa8\x00\x00\x00\x00\x00\x00\x0bU\xf0\x00\x00\x00\x00\x00\x00\r\xd6\x80\x00\x00\x00\x00\x00\x00\x05kP\x00\x00\x00\x00\x00\x00\r\xbe\x84\x00\x00\x00\x00\x00\x00\x06\xaa\x10\x00\x00\x00\x00\x00\x00\x05\xd8J\x00\x00\x00\x00\x00\x00\x03t\x00\x80\x00\x00\x00\x00\x00\x07\xb1$\x00\x00\x00\x00\x00\x00\r\xd4\x81\x00\x00\x00\x00\x00\x00\x1e\xf0\xda\x00\x00\x00\x00\x00\x007X\xf6\x00\x00\x00\x00\x00\x00\x1bX^@\x00\x00\x00\x00\x00\x1d\"4\x00\x00\x00\x00\x00\x00\x17@\x88\xd0\x00\x00\x00\x00\x00\x1d\x14!P\x00\x00\x00\x00\x00\x00+\xd3`\x00\x00\x00\x00\x00\x00]n\x80\x00\x00\x00\x00\x00\x00c\xd8\x00\x00\x00\x00\x00\x00\x01@\xb0\x00\x00\x00\x00\x00\x00\x02\xa1\xd8\x00\x00\x00\x00\x00\x00\x02\xd1t\x00\x00\x00\x00\x00\x00\x03A\xd8\x00\x00\x00\x00\x00\x00\x02\xc2\xf0\x00\x00\x00\x00\x00\x00\x01\x0b\xa0\x00\x00\x00\x00\x00\x00\x00>\xf8\x00\x00\x00\x00\x00\x00\x01\xea\x1c\x00\x00\x00\x00\x00\x00\x01\xb4\x17\xf0\x00\x00\x00\x00\x00\x02\xe0\x0f\xd0\x00\x00\x00\x00\x00\x01\xe0\x05x\x00\x00\x00\x00\x00\x01\xb0\x03\xe0\x00\x00\x00\x00\x00\x01\xf0\x02\x80\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_10_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\x00\x00\x00\x00\x00\x00\x01\xa8\x00\x00\x00\x00\x00\x00\x00\x02\xd2\x00\x00\x00\x00\x00\x00\x00\x02\xb0p\x00\x00\x00\x00\x00\x00\x06\xd0X\x00\x00\x00\x00\x00\x00\x0bj\xdc\x00\x00\x00\x00\x00\x00\n\xa9l\x00\x00\x00\x00\x00\x00\r\xdd\xb8\x00\x00\x00\x00\x00\x00\n\xaa\xe0\x00\x00\x00\x00\x00\x00\r\xb7\xa0\x00\x00\x00\x00\x00\x00\n\xda\x88\x00\x00\x00\x00\x00\x00\x0fn\xa0\x00\x00\x00\x00\x00\x00\x05V\n\x00\x00\x00\x00\x00\x00\x07mH\x80\x00\x00\x00\x00\x00\x03\xba\x00\x00\x00\x00\x00\x00\x00\x05\xec*@\x00\x00\x00\x00\x00\x06\xb8\x80\x80\x00\x00\x00\x00\x00\x0f\xe8r\x80\x00\x00\x00\x00\x00\n\xbdm\x00\x00\x00\x00\x00\x00\x1f\xcc?\x00\x00\x00\x00\x00\x00\x15,\xb4\x00\x00\x00\x00\x00\x00\x0f\x90\x08\xa0\x00\x00\x00\x00\x00\r\x8aQ\xb0\x00\x00\x00\x00\x00\x015\xb2\xd0\x00\x00\x00\x00\x00\x00_^\x80\x00\x00\x00\x00\x00\x00a\xd8\x00\x00\x00\x00\x00\x00\x01@\xd0\x00\x00\x00\x00\x00\x00\x02\xa0\xf8\x00\x00\x00\x00\x00\x00\x03aX\x00\x00\x00\x00\x00\x00\x02\x81\xf0\x00\x00\x00\x00\x00\x00\x03AX\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x00\x00\x00\x00\x00\x00\x00\xbf\\\x00\x00\x00\x00\x00\x00\x01\xd5\x1e@\x00\x00\x00\x00\x00\x01\xfc\x05\xe0\x00\x00\x00\x00\x00\x01P\x07x\x00\x00\x00\x00\x00\x01\xf0\x03\xd0\x00\x00\x00\x00\x00\x01\xd0\x03p\x00\x00\x00\x00\x00\x01p\x03\x80\x00\x00\x00\x00\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_11_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0\x00\x00\x00\x00\x00\x00\x00\x01h\x00\x00\x00\x00\x00\x00\x00\x06\xb1\x00\x00\x00\x00\x00\x00\x00\x03\xa2`\x00\x00\x00\x00\x00\x00\r`\xb8\x00\x00\x00\x00\x00\x00\x05\xa0\xdc\x00\x00\x00\x00\x00\x00\rQp\x00\x00\x00\x00\x00\x00\x0b\xbd\xd8\x00\x00\x00\x00\x00\x00\x15f\xe8\x00\x00\x00\x00\x00\x00\x0e\xbbP\x00\x00\x00\x00\x00\x00\x15\xd5\xa0\x00\x00\x00\x00\x00\x00\x0e\xae\xc4\x00\x00\x00\x00\x00\x00\x0bk\x12@\x00\x00\x00\x00\x00\r\xb6\x88\x00\x00\x00\x00\x00\x00\x07n$\x80\x00\x00\x00\x00\x00\x03\xda\x80@\x00\x00\x00\x00\x00\x02\xfc$\x00\x00\x00\x00\x00\x00\x07U!\x80\x00\x00\x00\x00\x00\x05\xfc}\x00\x00\x00\x00\x00\x00\x0fW+\x00\x00\x00\x00\x00\x00\r\xeb>\x00\x00\x00\x00\x00\x00\x0fJ\x14\x80\x00\x00\x00\x00\x00\x05\xc8(@\x00\x00\x00\x00\x00\x06\xf6\xd9\xb0\x00\x00\x00\x00\x00\x00[\xee\xd0\x00\x00\x00\x00\x00\x00a:\x80\x00\x00\x00\x00\x00\x01\x80\xd0\x00\x00\x00\x00\x00\x00\x06\xc0\xec\x00\x00\x00\x00\x00\x00\x02\xa0\xb8\x00\x00\x00\x00\x00\x00\x05Ax\x00\x00\x00\x00\x00\x00\x03\x01\xd8\x00\x00\x00\x00\x00\x00\x00\x01v\x00\x00\x00\x00\x00\x00\x00\xe9\xac\x00\x00\x00\x00\x00\x00\x01w\x06\x00\x00\x00\x00\x00\x00\x00\xdd\x07`\x00\x00\x00\x00\x00\x01\xf2\x03\xb0\x00\x00\x00\x00\x00\x00\xb0\x05\xf8\x00\x00\x00\x00\x00\x00\xf8\x03\xa8\x00\x00\x00\x00\x00\x00\xd8\x03\xf8\x00\x00\x00\x00\x00\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_12_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x16\xc0\x00\x00\x00\x00\x00\x00\x005\xa0\x00\x00\x00\x00\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00V \x00\x00\x00\x00\x00\x00\x00j\x84\x00\x00\x00\x00\x00\x00\x00\xbc\x16\x00\x00\x00\x00\x00\x00\x00\xd6\x1b\x80\x00\x00\x00\x00\x00\x00\xab\xaf\x00\x00\x00\x00\x00\x00\x00\xda\xda\x00\x00\x00\x00\x00\x00\x01mz\x00\x00\x00\x00\x00\x00\x00\xb6\xd4\x80\x00\x00\x00\x00\x00\x01\xabh\x00\x00\x00\x00\x00\x00\x00\xda\xd1\x00\x00\x00\x00\x00\x00\x00\xef\xa2\x90\x00\x00\x00\x00\x00\x00\xb5\x80\x00\x00\x00\x00\x00\x00\x00\xee\x8a@\x00\x00\x00\x00\x00\x01\xbb\x00\x10\x00\x00\x00\x00\x00\x01\xee)\x10\x00\x00\x00\x00\x00\x03v\x18P\x00\x00\x00\x00\x00\x03\xbbN\xa0\x00\x00\x00\x00\x00\x05\xd5\r\xc0\x00\x00\x00\x00\x00\x03e\x07\x00\x00\x00\x00\x00\x00\x03\xa8$\x80\x00\x00\x00\x00\x00\x02\xf2\x94\x00\x00\x00\x00\x00\x00\x00\x80\xfa@\x00\x00\x00\x00\x00\x00\x03v\x80\x00\x00\x00\x00\x00\x00\x1d\xb7`\x00\x00\x00\x00\x00\x00\xd4T\x80\x00\x00\x00\x00\x00\x01P~@\x00\x00\x00\x00\x00\x01`X\x00\x00\x00\x00\x00\x00\x01@\xec\x00\x00\x00\x00\x00\x00\x00\x81p\x00\x00\x00\x00\x00\x00\x00\x8a\xd8\x00\x00\x00\x00\x00\x00\x00\x1f\x98\x00\x00\x00\x00\x00\x00\x00:\x18\x00\x00\x00\x00\x00\x00\x00\x1e<\x00\x00\x00\x00\x00\x00\x00,.\x00\x00\x00\x00\x00\x00\x00\x1e;\x00\x00\x00\x00\x00\x00\x006?\x00\x00\x00\x00\x00\x00\x00\x1cj\x00\x00\x00\x00\x00\x00\x00\x0c*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_13_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x01V\x00\x00\x00\x00\x00\x00\x00\x03\xad\x00\x00\x00\x00\x00\x00\x00\x06\xd0\x00\x00\x00\x00\x00\x00\x00\x05`\x80\x00\x00\x00\x00\x00\x00\r\xa0\x00\x00\x00\x00\x00\x00\x00\n\xa4`\x00\x00\x00\x00\x00\x00\r\xd0\xb0\x00\x00\x00\x00\x00\x00\x16\xb5h\x00\x00\x00\x00\x00\x00\x1bZ\xe0\x00\x00\x00\x00\x00\x00\x15\xad\x80\x00\x00\x00\x00\x00\x00\x1a\xf7@\x00\x00\x00\x00\x00\x00\x1e\x9a@\x00\x00\x00\x00\x00\x00\x15\xecP\x00\x00\x00\x00\x00\x00\x1fq\x04\x00\x00\x00\x00\x00\x00\x15\xa4 \x00\x00\x00\x00\x00\x00~\xc0\x84\x00\x00\x00\x00\x00\x00\xab\x92\x90\x00\x00\x00\x00\x00\x00\xfe\x87l\x00\x00\x00\x00\x00\x00\xab\x92\xe8\x00\x00\x00\x00\x00\x01\xfa\xc1\xb0\x00\x00\x00\x00\x00\x00\xaa\x80\xc0\x00\x00\x00\x00\x00\x00\xf2*\x80\x00\x00\x00\x00\x00\x00\x11*\x00\x00\x00\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x00\x00\x00\x00=\x00\x00\x00\x00\x00\x00\x00\x00-\x00\x00\x00\x00\x00\x00\x00\x00v\x80\x00\x00\x00\x00\x00\x00\x00_\x00\x00\x00\x00\x00\x00\x00\x00\xf5\x80\x00\x00\x00\x00\x00\x00\x04\xbe\x00\x00\x00\x00\x00\x00\x00\x06\xa8\x00\x00\x00\x00\x00\x00\x00\n\xfc\x00\x00\x00\x00\x00\x00\x00\rl\x00\x00\x00\x00\x00\x00\x00\x05\xba\x00\x00\x00\x00\x00\x00\x00\x06\xf8\x00\x00\x00\x00\x00\x00\x00\x0b\x80\x00\x00\x00\x00\x00\x00\x00\r\xa0\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x05p\x00\x00\x00\x00\x00\x00\x00\x07\xd0\x00\x00\x00\x00\x00\x00\x00\x05\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_14_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\xe8\x00\x00\x00\x00\x00\x00\x00\x03^\x00\x00\x00\x00\x00\x00\x00\x02\xd0\x00\x00\x00\x00\x00\x00\x00\x05a\x00\x00\x00\x00\x00\x00\x00\x07D@\x00\x00\x00\x00\x00\x00\n\xe1p\x00\x00\x00\x00\x00\x00\rB\xc0\x00\x00\x00\x00\x00\x00\x0b\xb3\xe0\x00\x00\x00\x00\x00\x00\r]\x00\x00\x00\x00\x00\x00\x00\x15\xab\xa0\x00\x00\x00\x00\x00\x00\n\xee\x00\x00\x00\x00\x00\x00\x00\x0fZP\x00\x00\x00\x00\x00\x00\x15h@\x00\x00\x00\x00\x00\x00\r\xb9$\x00\x00\x00\x00\x00\x00\x1e\xd0\x00\x00\x00\x00\x00\x00\x00\x0b\xe4\x92\x00\x00\x00\x00\x00\x00\x1d@\x00\x00\x00\x00\x00\x00\x007\xd3\xaa\x00\x00\x00\x00\x00\x00}E\xd4\x00\x00\x00\x00\x00\x00W\xe0\xf8\x00\x00\x00\x00\x00\x00z\x08P\x00\x00\x00\x00\x00\x00,\xa2\x80\x00\x00\x00\x00\x00\x00>\xb5\x00\x00\x00\x00\x00\x00\x00\x14\x1c\x00\x00\x00\x00\x00\x00\x00\x006\x00\x00\x00\x00\x00\x00\x00\x00=\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00=\x00\x00\x00\x00\x00\x00\x00\x00_\x00\x00\x00\x00\x00\x00\x00\x00u\x00\x00\x00\x00\x00\x00\x00\x00[\x80\x00\x00\x00\x00\x00\x00\x00\xfc\x80\x00\x00\x00\x00\x00\x00\x01\xa6\xa0\x00\x00\x00\x00\x00\x00\x01\xf5@\x00\x00\x00\x00\x00\x00\x02\xbb@\x00\x00\x00\x00\x00\x00\x0b\xe8\x00\x00\x00\x00\x00\x00\x00\x1fp\x00\x00\x00\x00\x00\x00\x00\x16\xd8\x00\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x00\x00\x00\x00\x00\x15\xa0\x00\x00\x00\x00\x00\x00\x00\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x05@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_15_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x00\x00\x00\xea\x00\x00\x00\x00\x00\x00\x00\x03P\x00\x00\x00\x00\x00\x00\x00\x02\xc1\x00\x00\x00\x00\x00\x00\x00\x05D\xa0\x00\x00\x00\x00\x00\x00\x07\xa1p\x00\x00\x00\x00\x00\x00\x04\xc2\xe0\x00\x00\x00\x00\x00\x00\x0bE\x80\x00\x00\x00\x00\x00\x00\r\xb7@\x00\x00\x00\x00\x00\x00\n\xda\x80\x00\x00\x00\x00\x00\x00\x0e\xae\x10\x00\x00\x00\x00\x00\x00\x0bt@\x00\x00\x00\x00\x00\x00\x15\xa9 \x00\x00\x00\x00\x00\x00\rX(\x00\x00\x00\x00\x00\x00\x0e\xf2\x82\x00\x00\x00\x00\x00\x00\x0bP\x08\x00\x00\x00\x00\x00\x00\x0f\xe4\xa0\x00\x00\x00\x00\x00\x00\n\xa1D\x00\x00\x00\x00\x00\x00\x0f\xf3\x88\x00\x00\x00\x00\x00\x00\x1a\xaa\xec\x00\x00\x00\x00\x00\x00?P\xa0\x00\x00\x00\x00\x00\x00\x15\"\xc0\x00\x00\x00\x00\x00\x00\x1f\x9c\x00\x00\x00\x00\x00\x00\x00\n\xd7\x00\x00\x00\x00\x00\x00\x00\x05=\x80\x00\x00\x00\x00\x00\x00\x00.\x80\x00\x00\x00\x00\x00\x00\x00w\xc0\x00\x00\x00\x00\x00\x00\x00]\x90\x00\x00\x00\x00\x00\x00\x007@\x00\x00\x00\x00\x00\x00\x00=\xe8\x00\x00\x00\x00\x00\x00\x00n\xa0\x00\x00\x00\x00\x00\x00\x00v\xb0\x00\x00\x00\x00\x00\x00\x00\xd3T\x00\x00\x00\x00\x00\x00\x01\xc1\xa0\x00\x00\x00\x00\x00\x00\x07C\x00\x00\x00\x00\x00\x00\x00\x0b\x07\x00\x00\x00\x00\x00\x00\x00>\r\x80\x00\x00\x00\x00\x00\x00\x1a\x0f\x80\x00\x00\x00\x00\x00\x00>\n\x80\x00\x00\x00\x00\x00\x00\x17\x87\x80\x00\x00\x00\x00\x00\x00\x1d\x81\x80\x00\x00\x00\x00\x00\x00\x17\x01\x00\x00\x00\x00\x00\x00\x00\x05\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_16_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x90\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x1b$\x00\x00\x00\x00\x00\x00\x00,\x07\x00\x00\x00\x00\x00\x00\x00*U\x80\x00\x00\x00\x00\x00\x006\x1e\x80\x00\x00\x00\x00\x00\x00[+\x00\x00\x00\x00\x00\x00\x00m\xfc\x00\x00\x00\x00\x00\x00\x005*\x00\x00\x00\x00\x00\x00\x00V\xe8\x00\x00\x00\x00\x00\x00\x00u\xa2\x80\x00\x00\x00\x00\x00\x00[\xd2\x00\x00\x00\x00\x00\x00\x00mA@\x00\x00\x00\x00\x00\x007\x80\x00\x00\x00\x00\x00\x00\x00Z$\x90\x00\x00\x00\x00\x00\x00\x7f\x80\x00\x00\x00\x00\x00\x00\x00\xd5\x1a@\x00\x00\x00\x00\x00\x00\xbe\xac \x00\x00\x00\x00\x00\x00\xeb\xbb\x80\x00\x00\x00\x00\x00\x01\xb4\x8e\x80\x00\x00\x00\x00\x00\x01\xf2,\x00\x00\x00\x00\x00\x00\x00\xa9P\x00\x00\x00\x00\x00\x00\x00\xfa\xe8\x00\x00\x00\x00\x00\x00\x00\x03|\x80\x00\x00\x00\x00\x00\x00\x05\xaf0\x00\x00\x00\x00\x00\x00\x06z\xd0\x00\x00\x00\x00\x00\x00\x04\xedP\x00\x00\x00\x00\x00\x00\x06\xb8\xa0\x00\x00\x00\x00\x00\x00\x04\xec\x00\x00\x00\x00\x00\x00\x00\x0b\xbc\x00\x00\x00\x00\x00\x00\x00\x15\xf6\x00\x00\x00\x00\x00\x00\x00\x1bF\x00\x00\x00\x00\x00\x00\x00\x07\x83\x00\x00\x00\x00\x00\x00\x00\x1d\x02\x80\x00\x00\x00\x00\x00\x00v\x07\xc0\x00\x00\x00\x00\x00\x00\xd8\x0e\xc0\x00\x00\x00\x00\x00\x00\xf8\x07\x80\x00\x00\x00\x00\x00\x00l\x0c\x00\x00\x00\x00\x00\x00\x00\xbc\x00\x00\x00\x00\x00\x00\x00\x00v\x00\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario_17_buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\x00\x00\x00\x00\x00\x00\x01\xaa\x00\x00\x00\x00\x00\x00\x00\x01h\x00\x00\x00\x00\x00\x00\x00\x03QL\x00\x00\x00\x00\x00\x00\x05\xb06\x00\x00\x00\x00\x00\x00\x05b/\x00\x00\x00\x00\x00\x00\x06\xb0\xfa\x00\x00\x00\x00\x00\x00\x05\xd8\xac\x00\x00\x00\x00\x00\x00\x06\xab\xd8\x00\x00\x00\x00\x00\x00\x05m`\x00\x00\x00\x00\x00\x00\x06\xd6\xa8\x00\x00\x00\x00\x00\x00\x03m\x80\x00\x00\x00\x00\x00\x00\x05\xb6\x9a\x00\x00\x00\x00\x00\x00\x02\xad\x10\x80\x00\x00\x00\x00\x00\x03\xf8\x04@\x00\x00\x00\x00\x00\x06\xaa@\x00\x00\x00\x00\x00\x00\x1f\xf0\x12\x80\x00\x00\x00\x00\x00\x15U\xab\x00\x00\x00\x00\x00\x00?\xf1}\x00\x00\x00\x00\x00\x00*\x18\xea\x00\x00\x00\x00\x00\x00?a>\x00\x00\x00\x00\x00\x00+\x08\x10\x80\x00\x00\x00\x00\x00\x1d\xaa\xe0 \x00\x00\x00\x00\x00\x06\x8f\xa4 \x00\x00\x00\x00\x00\x00u\xfb\xa0\x00\x00\x00\x00\x00\x00\xa2\xae\xc0\x00\x00\x00\x00\x00\x02\xc3\xfa\x00\x00\x00\x00\x00\x00\x02\x80\xd0\x00\x00\x00\x00\x00\x00\n\xc3\xb8\x00\x00\x00\x00\x00\x00\x02\x83\xf0\x00\x00\x00\x00\x00\x00\x01\x06\xb0\x00\x00\x00\x00\x00\x00\x00\x0b\xd0\x00\x00\x00\x00\x00\x00\x00\x1e8\x00\x00\x00\x00\x00\x00\x00h\x14\xc0\x00\x00\x00\x00\x00\x01\xb8\x0fp\x00\x00\x00\x00\x00\x01\xe0\x05\xd0\x00\x00\x00\x00\x00\x02\xf0\x07\xe0\x00\x00\x00\x00\x00\x01\xa8\x03@\x00\x00\x00\x00\x00\x01\xf8\x03\x80\x00\x00\x00\x00\x00\x01h\x01\x00\x00\x00\x00\x00\x00\x00\xf4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    mario = (mario_1_buffer, mario_2_buffer, mario_3_buffer, mario_4_buffer, mario_5_buffer, mario_6_buffer, mario_7_buffer, mario_8_buffer, mario_9_buffer, mario_10_buffer,
             mario_11_buffer, mario_12_buffer, mario_13_buffer, mario_14_buffer, mario_15_buffer, mario_16_buffer, mario_17_buffer)
    return mario