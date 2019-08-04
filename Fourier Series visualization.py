import math
import pygame as g


# initialize pygame window
g.init()
win_width = 1400
win_height = 600
win = g.display.set_mode((win_width, win_height))
g.display.set_caption("Fourier Series Visualization")
font = g.font.SysFont('Times New Roman', 20)
clock = g.time.Clock()
win.fill((255,255, 255))
theta = 0
radius = 100
wave = []
x_counter = 2*radius + 100 + 30

flag = True
while flag:
    clock.tick(60)
    for change in g.event.get():
        if change.type == g.QUIT:
            g.quit()
            flag = False

    x = int(radius * math.cos(theta))
    y = int(radius * math.sin(theta))
    wave.insert(0,y + 150 + radius)
    win.fill((255, 255, 255))
    #draw wave
    for i in range(0, len(wave)):
        g.draw.circle(win,(30,144,255),(2*radius + 130 + i,wave[i]),1,0)

    #side line
    g.draw.line(win,(30, 144, 255), (radius+100+x, radius+150+y),(x_counter,wave[0]), 3)
    # main circle
    g.draw.circle(win, (255, 165, 0), (radius + 100, radius + 150), radius, 3)
    # point on the circle
    g.draw.circle(win, (30,144,255), (radius + 100 + x, radius + 150 + y), 5, 0)
    # line connecting point and the circle
    g.draw.line(win,(30, 144, 255), (radius + 100, radius + 150), (radius+100+x, radius+150+y),3)
    g.display.update()
    theta -= 0.01

    if len(wave) >= 800:
        wave.pop()

# g.draw.rect(win,(255,255,255),(0,0,2*radius + 110, 2*radius + 310),0)