import random
import pygame as g
import math

g.init()
# initialize pygame window
win_width = 1200
win_height = 600
win = g.display.set_mode((win_width, win_height))
g.display.set_caption("TSP")
font = g.font.SysFont('Times New Roman', 20)
clock = g.time.Clock()

# store the shortest path
shortest_path_ran = []
shortest_path_bf = []

# number of points/cities
num_points = 7
total_poss = math.factorial(num_points)
counter = 0
points = []
min_d_ran = min_d_bf = 100000
ran_array = []
bf_array = []
sample_size = num_points**4
if sample_size >= total_poss:
    sample_size = math.ceil(total_poss/2)
counter_sample = 0

# generate random points on the screen.py
# store points in points
def GeneratePoints():
    global num_points
    global points
    for i in range(0, num_points):
        x = random.randint(10, win_width//2 - 10)
        y = random.randint(200, win_height-50)
        pos = [x, y]
        points.append(pos)


def drawPath_Bf(array):
    g.display.update()
    g.draw.rect(win,(255, 255, 255), (0,0,win_width//2,win_height))
    for i in range(0,num_points):
        g.draw.circle(win, (0, 191, 255),(points[i][0],points[i][1]), 8)

    for i in range(0,num_points-1):
        #print(array[i])
        g.draw.line(win, (66, 87, 255), array[i], array[i+1], 5)
    g.draw.line(win, (66, 87, 255), array[0], array[num_points-1], 5)
    if counter < total_poss:
        percent = 100*counter/total_poss
        text1 = font.render("Points/Cities: {}".format(num_points), 1, (0, 0, 0))
        text2 = font.render("Brute force:", 1, (0, 0, 0))
        text3 = font.render("Minimum Tour Length: {}".format(min_d_bf), 1, (0, 0, 0))
        text4 = font.render("Iterations: {}".format(counter), 1, (0, 0, 0))
        text5 = font.render("{0:.2f}% completed".format(percent), 1, (0, 0, 0))

        win.blit(text1, (10, 0))
        win.blit(text2, (10, 30))
        win.blit(text3, (10, 50))
        win.blit(text4, (10, 70))
        win.blit(text5, (10, 90))
    #g.time.delay(10)

def drawPath_ran(array):
    g.display.update()
    g.draw.rect(win, (255, 255, 255), (win_width//2, 0, win_width//2, win_height))
    for i in range(0,num_points):
        g.draw.circle(win, (0, 191, 255),(points[i][0]+ win_width//2+10,points[i][1]), 8)

    for i in range(0,num_points-1):
        p1 = [array[i][0]+ win_width//2 + 10, array[i][1]]
        p2 = [array[i+1][0]+ win_width//2 + 10, array[i+1][1]]
        g.draw.line(win, (66, 87, 255), p1, p2, 5)

    p1 = [array[0][0] + win_width // 2 + 10, array[0][1]]
    p2 = [array[num_points-1][0] + win_width // 2 + 10, array[num_points-1][1]]

    g.draw.line(win, (66, 87, 255), p1, p2, 5)

    if (counter_sample < sample_size) or (counter < total_poss) :
        percent = 100*counter_sample/sample_size
        text1 = font.render("Random Sampling:", 1, (0, 0, 0))
        text2 = font.render("Minimum Tour Length: {}".format(min_d_ran), 1, (0, 0, 0))
        text3 = font.render("Iterations: {}".format(counter_sample), 1, (0, 0, 0))
        text4 = font.render("{0:.2f}% completed".format(percent), 1, (0, 0, 0))

        win.blit(text1, (win_width//2+ 10, 30))
        win.blit(text2, (win_width//2+ 10, 50))
        win.blit(text3, (win_width//2+ 10, 70))
        win.blit(text4, (win_width//2+ 10, 90))

def findDistance(array):
    d = 0
    for j in range(0, num_points - 1):
        d += ((array[j][0] - array[j + 1][0]) ** 2 + (array[j][1] - array[j + 1][1]) ** 2) ** 0.5

    return d


GeneratePoints()
ran_array = points
bf_array = points

def TspRan():
    global min_d_ran, ran_array, shortest_path_ran,counter_sample
    if counter_sample <= sample_size:
        random.shuffle(ran_array)
        dis = findDistance(ran_array)
        if dis <= min_d_ran:
            min_d_ran = dis
            shortest_path_ran = ran_array
        drawPath_ran(ran_array)
    counter_sample += 1


# Generating permutation using Heap Algorithm
# size = n = len(array)
def TspBf(array, size, n):
    global min_d_bf, shortest_path_bf,counter,flag
    # if size becomes 1 then permutation is complete
    # permutation
    if size == 1:
        for change in g.event.get():
            if change.type == g.QUIT:
                g.quit()
                flag = False

        counter += 1
        d = findDistance(array)
        # print(d)
        if d < min_d_bf:
            min_d_bf = d
            shortest_path_bf = array
            #drawPoints()
        drawPath_Bf(array)
        if counter_sample < sample_size:
            TspRan()
        else:
            drawPath_ran(shortest_path_ran)

    for i in range(size):
        TspBf(array, size - 1, n)
        # if size is odd, swap first and last
        # element
        # else If size is even, swap ith and last element
        if size % 2 == 1:
            array[0], array[size - 1] = array[size - 1], array[0]
        else:
            array[i], array[size - 1] = array[size - 1], array[i]



flag = True
after_flag = False
while flag:
    #clock.tick(60)
    for change in g.event.get():
        if change.type == g.QUIT:
            g.quit()
            flag = False


    if counter >= total_poss:
        if after_flag == False:
            #win.fill((255, 255, 255))
            drawPath_Bf(shortest_path_bf)
            drawPath_ran(shortest_path_ran)
        g.display.update()
        g.draw.rect(win, (255, 255, 255), (0, 0, win_width, 100))
        text1 = font.render("Points/Cities: {}".format(num_points), 1, (0, 0, 0))
        text2 = font.render("Minimum Tour Length Using Random Samples: {}".format(min_d_ran), 1, (0, 0, 0))
        text3 = font.render("Minimum Tour Length using Brute Force: {}".format(min_d_bf), 1, (0, 0, 0))
        text4 = font.render("Total Iterations(brute force): {}".format(counter), 1, (0, 0, 0))
        text5 = font.render("Total Iterations(random sampling): {}".format(sample_size), 1, (0, 0, 0))

        win.blit(text1, (10, 0))
        win.blit(text2, (10, 20))
        win.blit(text3, (10, 40))
        win.blit(text4, (10, 60))
        win.blit(text5, (10, 80))
        after_flag = True

    else:
        TspBf(bf_array, num_points, num_points)

