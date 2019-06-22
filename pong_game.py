# Simple Python Pong game using turtle


import turtle

#screen setup

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

# score
score_1 = 0
score_2 = 0


#objects

#Paddle 1
p_a = turtle.Turtle()
p_a.speed(0)
p_a.shape("square")
p_a.color("white")
p_a.shapesize(stretch_wid=5,stretch_len=1)
p_a.penup()
p_a.goto(-350, 0)

#paddle 2
p_b = turtle.Turtle()
p_b.speed(0)
p_b.shape("square")
p_b.color("white")
p_b.shapesize(stretch_wid=5,stretch_len=1)
p_b.penup()
p_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.x=0.3
ball.y=0.3

#scores
ink = turtle.Turtle()
ink.speed(0)
ink.color("white")
ink.penup()
ink.hideturtle()
ink.goto(0,260)

msg1 = turtle.Turtle()
msg1.speed(0)
msg1.color("white")
msg1.penup()
msg1.hideturtle()
msg1.goto(-397,-290)
msg1.write("Move using 'w' and 's'", font=("courier", 10, "normal"))

msg2 = turtle.Turtle()
msg2.speed(0)
msg2.color("white")
msg2.penup()
msg2.hideturtle()
msg2.goto(180,-290)
msg2.write("Move using 'Up' and 'Down'", font=("courier", 10, "normal"))


# functions
def p_a_up():
    if p_a.ycor()<260:
        y = p_a.ycor() + 20
        p_a.sety(y)

def p_a_down():
    if p_a.ycor() > -260:
        y = p_a.ycor() -20
        p_a.sety(y)

def p_b_up():
    if p_b.ycor() < 260:
        y = p_b.ycor() +20
        p_b.sety(y)

def p_b_down():
    if p_b.ycor() > -260:
        y = p_b.ycor() -20
        p_b.sety(y)

win.listen()
win.onkeypress(p_a_up, "w")
win.onkeypress(p_a_down, "s")
win.onkeypress(p_b_up, "Up")
win.onkeypress(p_b_down, "Down")

while True:
    win.update()

    #write the current score
    ink.clear()
    ink.write(f"Player 1: {score_1}  Player 2: {score_2}", align="center", font=("courier", 24, "normal"))

    #move the ball
    x_ball = ball.xcor() + ball.x
    y_ball = ball.ycor() + ball.y
    ball.setx(x_ball)
    ball.sety(y_ball)

    #check for collisions  - wall
    if ball.ycor() >290:
        ball.sety(290)
        ball.y = ball.y*-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.x = ball.x * -1
        score_1 = score_1 + 1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.y = ball.y * -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.x = ball.x * -1
        score_2 = score_2 + 1

    #collisions with paddles
    if 340 < ball.xcor() < 350 and p_b.ycor() + 50 > ball.ycor() > p_b.ycor() - 50:
        ball.setx(340)
        ball.x = ball.x*-1

    if -340 > ball.xcor() > -350 and p_a.ycor() + 50 > ball.ycor() > p_a.ycor() - 50:
        ball.setx(-340)
        ball.x = ball.x*-1

#end of while loop  
