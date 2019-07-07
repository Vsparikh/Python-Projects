# paste the code on this website to try without downloading pygame: https://repl.it/languages/pygame
import random
import pygame as g
import math

g.init()
# initialize pygame window
win_width = 800
win_height = 600
win = g.display.set_mode((win_width, win_height))
g.display.set_caption("TSP")
font = g.font.SysFont('Times New Roman', 20)
clock = g.time.Clock()
win.fill((0, 0, 0))

# store the shortest path
shortest_path_ran = []
shortest_path_bf = []

# number of points/cities
num_points = 6
total_poss = math.factorial(num_points)
counter = 0
points = []
min_d_ran = min_d_bf = 100000
ran_array = []

# generate random points on the screen
# store points in points
def GeneratePoints():
    global num_points
    global points
    for i in range(0, num_points):
        x = random.randint(10, win_width - 50)
        y = random.randint(200, win_height-50)
        pos = [x, y]
        points.append(pos)


def drawPoints():
    g.display.update()
    win.fill((0, 0, 0))
    for i in range(0,num_points):
        g.draw.circle(win, (255, 255, 255),(points[i][0],points[i][1]), 8)


def drawPath(array):
    g.display.update()
    win.fill((255, 255, 255))
    for i in range(0,num_points):
        g.draw.circle(win, (0, 191, 255),(points[i][0],points[i][1]), 8)

    for i in range(0,num_points-1):
        #print(array[i])
        g.draw.line(win, (66, 87, 255), array[i], array[i+1], 5)
    g.draw.line(win, (66, 87, 255), array[0], array[num_points-1], 5)
    if counter < total_poss:
        text1 = font.render("Points/Cities: {}".format(num_points), 1, (0, 0, 0))
        text2 = font.render("Minimum Tour Length: {}".format(min_d_bf), 1, (0, 0, 0))
        text3 = font.render("Iterations: {}".format(counter), 1, (0, 0, 0))

        win.blit(text1, (10, 0))
        win.blit(text2, (10, 20))
        win.blit(text3, (10, 40))
    g.time.delay(10)


def findDistance(array):
    d = 0
    for j in range(0, num_points - 1):
        d += ((array[j][0] - array[j + 1][0]) ** 2 + (array[j][1] - array[j + 1][1]) ** 2) ** 0.5

    return d


GeneratePoints()
ran_array = points


def TspRan():
    global min_d_ran, ran_array, shortest_path_ran
    for i in range(0, num_points ** 3):
        random.shuffle(ran_array)
        d = findDistance(ran_array)
        # print(d)
        if d <= min_d_ran:
            min_d_ran = d
            print("min_d_ran = {}".format(min_d_ran))
            shortest_path_ran = ran_array


# Generating permutation using Heap Algorithm
# size = n = len(array)
def TspBf(array, size, n):
    global min_d_bf, shortest_path_bf,counter,flag
    # if size becomes 1 then permutation is complete
    # permutation
    if size == 1:
        for change in g.event.get():
            if change.type == g.QUIT:
                flag = False

        counter += 1
        d = findDistance(array)
        # print(d)
        if d < min_d_bf:
            min_d_bf = d
            print("min_d_bf = {}".format(min_d_ran))
            shortest_path_bf = array
            #drawPoints()
        drawPath(array)

    for i in range(size):
        TspBf(array, size - 1, n)
        # if size is odd, swap first and last
        # element
        # else If size is even, swap ith and last element
        if size % 2 == 1:
            array[0], array[size - 1] = array[size - 1], array[0]
        else:
            array[i], array[size - 1] = array[size - 1], array[i]


TspRan()
flag = True
while flag:
    clock.tick(30)
    for change in g.event.get():
        if change.type == g.QUIT:
            g.quit()
            flag = False


    if counter >= total_poss:
        drawPath(shortest_path_bf)
        text1 = font.render("Points/Cities: {}".format(num_points), 1, (0, 0, 0))
        text2 = font.render("Minimum Tour Length Using Random Samples: {}".format(min_d_ran), 1, (0, 0, 0))
        text3 = font.render("Minimum Tour Length using Brute Force: {}".format(min_d_bf), 1, (0, 0, 0))
        text4 = font.render("Total Iterations: {}".format(counter), 1, (0, 0, 0))

        win.blit(text1, (10, 0))
        win.blit(text2, (10, 20))
        win.blit(text3, (10, 40))
        win.blit(text4, (10, 60))
    else:
        TspBf(points, num_points, num_points)


print("minimum distance using random samples: {}\nminimum distance using brute force {}".format(min_d_ran, min_d_bf))
