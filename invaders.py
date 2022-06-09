#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from random import randint, random
from img import invaders_img

screen_width = 0
screen_height = 0
invaders_quit = False
invaders_player = None
invaders_army = None
invaders_hud = None
invaders_rows = []

ship = (0x0C, 0x0E, 0x0F, 0x0E, 0x0C)
alien1_1 = (0x18, 0x7D, 0xB6, 0x3C, 0x3C, 0xB6, 0x7D, 0x18)
alien1_2 = (0x18, 0xFD, 0x36, 0x3C, 0x3C, 0x36, 0xFD, 0x18)
alien1 = (alien1_1, alien1_2)
alien2_1 = (0x98, 0x5C, 0xB6, 0x5F, 0x5F, 0xB6, 0x5C, 0x98)
alien2_2 = (0x18, 0xDC, 0x76, 0x9F, 0x9F, 0x76, 0xDC, 0x18)
alien2 = (alien2_1, alien2_2)
aliens = (alien1, alien2)
ARMY_SIZE_ROWS = 2
ARMY_SIZE_COLS = 8


class bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False

    def render(self, oled):
        if self.alive:
            oled.vline(self.x, self.y, 2, 1)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        return

    def update(self, direction):
        if self.alive:
            self.y = self.y + (direction * 4)
            if self.y < 10:
                self.alive = False


class player(object):
    def __init__(self, screen_width, screen_height):
        self.x = int(screen_width / 2)
        self.y = screen_height - 12
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bullets = [bullet(0, 0) for _ in range(4)]

    def render(self, oled):
        for i in range(len(ship)):
            line = ship[i]
            for j in range(4):
                if line & 0x1:
                    oled.pixel(self.x - 2 + i, self.y + j, 1)
                line >>= 1

        for bullet in self.bullets:
            bullet.render(oled)

    def update(self, direction):
        t = self.x + (direction * 2)
        if t > 4 and t < self.screen_width - 4:
            self.x = t
        for bullet in self.bullets:
            bullet.update(-1)

    def shoot(self):
        for bullet in self.bullets:
            if not bullet.alive:
                bullet.reset(self.x, self.y)
                break


class invader(object):
    def __init__(self, minx, maxx, x, y, invader_type):
        self.x = x
        self.y = y
        self._direction = 1
        self.alive = True
        self.score = 10
        self._minx = minx
        self._maxx = maxx
        self.type = invader_type
        self.anim_index = 0
        return


    def render(self, oled):
        if self.alive:
            current_animation = aliens[self.type]
            current_alien = current_animation[int(self.anim_index) % len(current_animation)]
            self.anim_index += 0.5
            if self.anim_index >= 1440: self.anim_index = 0
            for i in range(len(current_alien)):
                line = current_alien[i]
                for j in range(8):
                    if line & 0x1:
                        oled.pixel(self.x - 4 + i, self.y - 4 + j, 1)
                    line >>= 1

    def update(self, screen_height):
        invaded = False
        if self.alive:
            t = self.x + self._direction
            if t > self._minx and t < self._maxx:
                self.x = self.x + self._direction
            else:
                self._direction = self._direction * -1
                self.y = self.y + 3
                if self.y > screen_height - 20:
                    invaded = True
        return invaded


class army(object):
    def __init__(self, screen_width, screen_height):
        self.invaded = False
        self.invaders = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        max_offset = screen_width - 8 - (ARMY_SIZE_COLS * 10)
        for i in range(ARMY_SIZE_ROWS):
            for j in range(ARMY_SIZE_COLS):
                offset = (j * 12)
                minx = 4 + offset
                maxx = max_offset + offset
                x = 4 + offset
                y = 20 + (i * 12)
                self.invaders.append(invader(minx, maxx, x, y, randint(0, len(aliens) - 1)))

    def render(self, oled):
        for invader in self.invaders:
            invader.render(oled)

    def update(self, bullets):
        for invader in self.invaders:
            if invader.update(self.screen_height):
                self.invaded = True

        for invader in self.invaders:
            if invader.alive:
                for bullet in bullets:
                    if bullet.alive:
                        t = (invader.x - bullet.x) * (invader.x - bullet.x) + (invader.y - bullet.y) * (invader.y - bullet.y)
                        # if point is in circle
                        if t < 25:  # 5 * 5 = r * r
                            invader.alive = False
                            bullet.alive = False

    def size(self):
        size = 0
        for invader in self.invaders:
            if invader.alive:
                size += 1
        return size

    def score(self):
        score = 0
        for invader in self.invaders:
            if not invader.alive:
                score += invader.score
        return score


class hud(object):
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def render(self, oled, score):
        oled.hline(0, self.screen_height - 3, self.screen_width, 1)
        oled.hline(0, self.screen_height - 1, self.screen_width, 1)
        score = "Score:{0}".format(score)
        oled.text(score, self.screen_width - (len(score) * 8), 0)


def ai_logic_shoot(army, player):
    for invader in army.invaders:
        if invader.alive:
            if player.x > (invader.x - 2) and player.x < (invader.x + 2):
                if random() < 0.75:
                    player.shoot()
                    return


def ai_logic_move(army, player, rows):
    for i in rows:
        invader = army.invaders[i]
        if invader.alive:
            if player.x < invader.x:
                player.update(1)
                return
            elif player.x > invader.x:
                player.update(-1)
                return
        i += 1


def init_invaders(scr_width, scr_height):
    global screen_width, screen_height, invaders_quit, invaders_player, invaders_army, invaders_hud, invaders_rows
    screen_width = scr_width
    screen_height = scr_height
    invaders_quit = False
    invaders_player = player(scr_width, scr_height)
    invaders_army = army(scr_width, scr_height)
    invaders_hud = hud(scr_width, scr_height)
    invaders_rows = sorted([i for i in range(ARMY_SIZE_ROWS * ARMY_SIZE_COLS)], key = lambda x: random())


def draw_invaders_intro(oled, switch_mode):
    global invaders_quit
    for i in range(60):
        if switch_mode():
            invaders_quit = True
            break
        oled.fill(0)
        oled.blit(invaders_img.get_invaders_fb(), 0, 0)
        title = "Invaders"
        txt_x = int((screen_width - (len(title) * 8)) / 2)
        oled.text(title, txt_x, 5)
        oled.show()


def draw_invaders(oled, switch_mode):
    global invaders_quit
    if invaders_quit == False:
        while not invaders_army.invaded and invaders_army.size() > 0:
            oled.fill(0)
            if switch_mode():
                invaders_quit = True
                break
            ai_logic_shoot(invaders_army, invaders_player)
            ai_logic_move(invaders_army, invaders_player, invaders_rows)
            invaders_army.update(invaders_player.bullets)
            invaders_army.render(oled)
            invaders_player.render(oled)

            invaders_hud.render(oled, invaders_army.score())
            oled.show()
            sleep(0.02)


def draw_invaders_game_over(oled, switch_mode):
    global invaders_quit
    if invaders_quit == False:
        visible = False
        for i in range(180):
            if switch_mode():
                invaders_quit = True
                break
            oled.fill(0)
            if (i % 30) == 0: visible = not visible
            if visible:
                if invaders_army.size() == 0:
                    title = "Victory!"
                else:
                    title = "Defeat!"
                txt_x = int((screen_width - (len(title) * 8)) / 2)
                txt_y = int(((screen_height - 8) / 2))
                oled.text(title, txt_x, txt_y)
            invaders_hud.render(oled, invaders_army.score())
            oled.show()
