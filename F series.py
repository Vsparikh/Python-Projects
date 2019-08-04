# Fourier Series Visualization {square wave}
# paste the code on this website to try without downloading pygame: https://repl.it/languages/pygame

import math
import pygame as g

# controls
# change translate_x and translate_y to move the simulation on the screen.py
translate_x = 150
translate_y = 250
# do not change terms to more than 20 as it would result in radius of circles less than 1, pixel size
terms = 4
radius_scl = 70
win_width = 1200
win_height = 600

# initialize pygame window
g.init()
win = g.display.set_mode((win_width, win_height))
g.display.set_caption("Fourier Series Visualization")
font = g.font.SysFont('Times New Roman', 20)
clock = g.time.Clock()
win.fill((255, 255, 255))

theta = 0
wave = []

flag = True
while flag:
    clock.tick(60)
    for change in g.event.get():
        if change.type == g.QUIT:
            g.quit()
            flag = False
    x = 0
    y = 0
    win.fill((255, 255, 255))
    for m in range(0, terms):
        pre_x = x
        pre_y = y
        n = m * 2 + 1
        radius = int(radius_scl * (4 / (n * math.pi)))
        x += int(radius * math.cos(n * theta))
        y += int(radius * math.sin(n * theta))

        # main circle
        g.draw.circle(win, (255, 165, 0), (translate_x + pre_x, translate_y + pre_y), radius, 2)
        # line connecting point and the circle
        g.draw.line(win, (30, 144, 255), (translate_x + pre_x, translate_y + pre_y), (translate_x + x, translate_y + y),
                    2)
        # point on the circle
        g.draw.circle(win, (30, 144, 255), (translate_x + x, translate_y + y), 5, 0)

    wave.insert(0, y + translate_y + radius)
    for i in range(0, len(wave)):
        g.draw.circle(win, (30, 144, 255), (translate_x + radius_scl + 50 + i, wave[i]), 1, 0)


    # side line
    g.draw.line(win, (30, 144, 255), (translate_x + x, translate_y + y), (translate_x + radius_scl + 50, wave[0]), 3)

    g.display.update()
    theta -= 0.01

    if len(wave) >= win_width - translate_y - radius_scl - 150:
        wave.pop()

# g.draw.rect(win,(255,255,255),(0,0,2*radius + 110, 2*radius + 310),0)