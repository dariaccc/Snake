
from turtle import Turtle, Screen
import time
import os
import sys
import random

size = 500

s = Screen()
s.title("Snake Game")
s.setup(size, size)
s.bgcolor("pink")

pieces = []
start_pos = [(0,0), (-20,0), (-40,0)]
s.tracer(0)
s.listen()

screen_x = size // 2
screen_y = size // 2

dot = Turtle()
dot.hideturtle()
dot.shape("circle")
dot.color("black")
dot.penup()
dot.shapesize(stretch_wid=0.5, stretch_len=0.5)

text = Turtle()
text.hideturtle()
text.color("white")

for i in start_pos:
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.setpos(i)
    pieces.append(snake)
s.update()

def new_dot():
    random_x = random.randint(-screen_x + 20, screen_x - 20)
    random_y = random.randint(-screen_y + 20, screen_y - 20)

    dot.showturtle()
    dot.setpos(random_x, random_y)


def go_up():
    if pieces[0].heading() != 270:
        pieces[0].setheading(90)

def go_down():
    if (pieces[0].heading() != 90):
        pieces[0].setheading(270)

def go_right():
    if (pieces[0].heading() != 180):
        pieces[0].setheading(0)

def go_left():
    if (pieces[0].heading() != 0):
        pieces[0].setheading(180)

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def wall():
    x, y = pieces[0].xcor(), pieces[0].ycor()
    if x > screen_x or x < -screen_x or y > screen_y or y < -screen_y:
        return True
    return False

def death():
    for piece in pieces[2:]:
        if pieces[0].distance(piece) < 10:
            return True
    return False

def eat():
    if pieces[0].distance(dot) < 15:
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        pieces.append(snake)
        snake.setpos(new_x, new_y)
        return True
    return False

def exit(x,y):
    s.bye()

def restart(x,y):
    python = sys.executable
    os.execl(python, python, *sys.argv)

s.onkey(go_up, "Up")
s.onkey(go_down, "Down")
s.onkey(go_right, "Right")
s.onkey(go_left, "Left")

new_dot()

score = Turtle()
score.hideturtle()
score.color("black")
score.penup()
score.setheading(90)
score.forward(230)
score_int = 0

def update_score():
    score.clear()
    score.write(f"Score: {score_int}", move=False, align="center", font=("Courier", 12))

update_score()

x = True
while x:
    s.update()
    time.sleep(0.05)

    for piece in range(len(pieces)-1, 0,-1):
        new_x = pieces[piece-1].xcor()
        new_y = pieces[piece-1].ycor()
        pieces[piece].goto(new_x, new_y)
    pieces[0].forward(10)

    if wall() or death():
        s.bgcolor("black")
        text.write("GAME OVER", move=False, align="center", font=("Courier", 20))
        s.onclick(restart)

    if eat():
        new_dot()
        score_int += 1
        update_score()
    
s.exitonclick()