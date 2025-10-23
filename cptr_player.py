import tkinter

from player import Player
import random

class Computer(Player):
    def __init__(self, name, avatar, status):
        super().__init__(name, avatar, status)
        self.o_ticks = 0

    def make_play(self, options: list):
        need_random = 0
        clicked: tuple
        tx_ticks = 0
        fx_ticks = 0
        sx_ticks = 0
        oy_ticks = 0
        ty_ticks = 0
        fy_ticks = 0
        for c in self.cells:
            if c[0] == 300:
                tx_ticks += 1
            elif c[0] == 500:
                fx_ticks += 1
            elif c[0] == 700:
                sx_ticks += 1
            if c[1] == 100:
                oy_ticks += 1
            elif c[1] == 300:
                ty_ticks += 1
            elif c[1] == 500:
                fy_ticks += 1
        xes = [tx_ticks, fx_ticks, sx_ticks]
        ys = [oy_ticks, ty_ticks, fy_ticks]
        for o in options:
            for x in xes:
                if 3 - (x/100) >= 0:
                    clicked = o
                    need_random = 1
                    break
            if need_random == 1:
                break
            elif need_random == 0:
                for y in ys:
                    if 3 - (y/100) >= 0:
                        clicked = o
                        need_random = 1
                        break
                if need_random == 1:
                    break
            if need_random == 1:
                break
            elif need_random == 0:
                choice = random.choice(options)
                clicked = choice
        return clicked
