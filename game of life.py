# Conway's Game of Life simulation
# Background: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# paste the code on this website to try without downloading pygame: https://repl.it/languages/pygame

import pygame as g
import random
g.init()

# initialize pygame window
win_width = 800
win_height = 600
win = g.display.set_mode((win_width, win_height + 50))
g.display.set_caption("Game of Life")
font = g.font.SysFont('Verdana', 20)
clock = g.time.Clock()
win.fill((255, 255, 255))

#length of each square in the game
square_size = 30

rows = int(win_width/square_size)
cols = int(win_height/square_size)

# defining functions

# returns a 2d list with o as initial value
# size of the array: rows x cols


def fill_array():
    n = []
    for i in range(rows):
        r = []
        for j in range(cols):
            r.append(0)
        n.append(r)
    return n


# returns a 2d list with o or 1 as initial value
# size of the array: rows x cols


def fill_array_ran():
    n = []
    for i in range(rows):
        r = []
        for j in range(cols):
            r.append(random.randint(0, 1))
        n.append(r)
    return n

# prints the game of life grid on the pygame window


def show_matrix():
    global matrix
    for i in range(rows):
        for j in range(cols):
            x = i * square_size
            y = j * square_size
            if matrix[i][j] == 1:
                g.draw.rect(win,(203, 245, 66),(x,y,square_size,square_size),0)
            else:
                g.draw.rect(win, (255, 255, 255), (x, y, square_size, square_size), 0)
            g.draw.rect(win, (0, 0, 0), (x, y, square_size, square_size), 1)


# finds the location of the square in the matrix array based on mouse position


def input_check(mouse_pos):
    for i in range(rows):
        for j in range(cols):
            x = i * square_size
            y = j * square_size
            if x <= pos[0] <= x+ square_size and y <= pos[1] <= y + square_size:
                return [i,j]

    return [-1, -1]


# count number of alive neighbours


def count_neighbours(m,n):
    global row, col, matrix
    sum = 0
    for i in range(-1, 2):
        for j in range(-1,2):
            # wrapping
            pos_x = (m + i + rows) % rows
            pos_y = (n + j + cols) % cols
            sum += matrix[pos_x][pos_y]
    sum = sum - matrix[m][n]
    return sum


matrix = fill_array()
user_change = True
while user_change:
    clock.tick(30)
    g.display.update()
    for change in g.event.get():
         if change.type == g.QUIT:
            g.quit()
            user_change = False

    # get mouse position
    pos = g.mouse.get_pos()
    # position of the box in the matrix array
    clicked_box = [-1, -1]

    # draw play box
    g.draw.rect(win, (205, 250, 242), (10,  win_height+ 10, 60, 30), 0)
    g.draw.rect(win, (108, 16, 115), (10,  win_height+ 10, 60, 30), 1)

    # draw random box
    g.draw.rect(win, (205, 250, 242), (win_width - 120, win_height + 10, 100, 30), 0)
    g.draw.rect(win, (108, 16, 115), (win_width - 120, win_height + 10, 100, 30), 1)

    # display text
    text1 = font.render("Play", 1, (16, 115, 18))
    text2 = font.render("Click left mouse button to add/remove cells", 1,(16, 115, 18))
    text3 = font.render("Random", 1, (16, 115, 18))
    win.blit(text1,(18, 612))
    win.blit(text2,(100, 612))
    win.blit(text3, (win_width-112, 612))

    for i in range(rows):
        for j in range(cols):
            x = i * square_size
            y = j * square_size
            g.draw.rect(win, (0, 0, 0), (x, y, square_size, square_size), 1)

    if change.type == g.MOUSEBUTTONDOWN:
        if 10 <= pos[0] <= 70 and win_height+10 <= pos[1] <= win_height+40:
            user_change = False
        if win_width - 120 <= pos[0] <= win_width - 20 and win_height+10 <= pos[1] <= win_height+40:
            matrix = fill_array_ran()
            show_matrix()

        clicked_box = input_check(pos)

    if clicked_box[0] != -1:
        g.time.delay(500)
        x = clicked_box[0] * square_size
        y = clicked_box[1] * square_size
        if matrix[clicked_box[0]][clicked_box[1]] == 0:
            g.draw.rect(win, (203, 245, 66), (x, y, square_size, square_size), 0)
            matrix[clicked_box[0]][clicked_box[1]] = 1
        else:
            g.draw.rect(win, (255, 255, 255), (x, y, square_size, square_size), 0)
            matrix[clicked_box[0]][clicked_box[1]] = 0

win.fill((255, 255, 255))
flag = True
while flag:
    clock.tick(7)
    g.display.update()

    # display the message
    text1 = font.render("Simulating The Game", 1, (16, 115, 18))
    win.blit(text1, (18, 612))
    for change in g.event.get():
        if change.type == g.QUIT:
            g.quit()
            flag = False

    show_matrix()
    matrix_next = fill_array()

    # calculate if the cell will be alive or not
    for i in range(rows):
        for j in range(cols):
            num_neighbours = count_neighbours(i, j)
            if matrix[i][j] == 0 and num_neighbours == 3:
                matrix_next[i][j] = 1
            elif matrix[i][j] == 1 and (num_neighbours > 3 or num_neighbours < 2):
                matrix_next[i][j] = 0
            else:
                matrix_next[i][j] = matrix[i][j]

    # update the state of the cell
    matrix = matrix_next

# matrix = [[random.randint(0,1) for i in range(rows) ]for j in range(cols)]
