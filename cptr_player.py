from player import Player
import random

class Computer(Player):
    def __init__(self, name, avatar, status):
        super().__init__(name, avatar, status)
        self.o_ticks = 0

    def make_play(self, options: list):
        tx_ticks = 0
        fx_ticks = 0
        sx_ticks = 0
        oy_ticks = 0
        ty_ticks = 0
        fy_ticks = 0
        for c in self.cells:
            if c[1][0] == 300:
                tx_ticks += 1
            elif c[1][0] == 300:
                fx_ticks += 1
            elif c[1][0] == 300:
                sx_ticks += 1
            if c[1][1] == 100:
                oy_ticks += 1
            elif c[1][1] == 300:
                ty_ticks += 1
            elif c[1][1] == 500:
                fy_ticks += 1
        xes = [tx_ticks, fx_ticks, sx_ticks]
        ys = [oy_ticks, ty_ticks, fy_ticks]
        try:
            for o in options:
                if o[1][0] + [x for x in xes] == 3:
                    o[0].invoke()
                    return
                elif o[1][1] + [y for y in ys] == 3:
                    o[0].invoke()
                    return
        finally:
            choice = random.choice(options)
            choice[0].invoke()
