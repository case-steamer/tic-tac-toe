from player import Player
import random

class Computer(Player):
    def __init__(self, name, avatar, status):
        super().__init__(name, avatar, status)
        self.o_ticks = 0

    def make_play(self, options: list):
        need_random = 0
        tx_ticks = 0
        fx_ticks = 0
        sx_ticks = 0
        oy_ticks = 0
        ty_ticks = 0
        fy_ticks = 0
        for c in self.cells:
            print(c)
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
                print('tried x value')
                if (o[1][0]/100) + x == [num for num in range(3, 8, 2)]:
                    o[0].invoke()
                    need_random = 1
            for y in ys:
                print('tried y value')
                if (o[1][1]/100) + y == [num for num in range(3, 6, 2)]:
                    o[0].invoke()
                    need_random = 1
            if need_random == 0:
                choice = random.choice(options)
                choice[0].invoke()
