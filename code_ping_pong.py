import turtle

# Game_name
player_1 = input('Введите свое имя: ')
player_2 = input(('Введите свое имя: '))

# Window
win = turtle.Screen()
win.title('My Game')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# rocket_left
rocket_left = turtle.Turtle()
rocket_left.speed(0)
rocket_left.shape('square')
rocket_left.color('green')
rocket_left.shapesize(stretch_len=0.5, stretch_wid=5)
rocket_left.penup()
rocket_left.goto(-350, 0)

# rocket_right
rocket_right = turtle.Turtle()
rocket_right.speed(0)
rocket_right.shape('square')
rocket_right.color('red')
rocket_right.shapesize(stretch_len=0.5, stretch_wid=5)
rocket_right.penup()
rocket_right.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'{player_1}: 0  {player_2}: 0', align='center', font=('Verdana', 22, 'normal'))
score_1 = 0
score_2 = 0


# Leave Game
leave = turtle.Turtle()
leave.speed(0)
leave.shape('square')
leave.color('white')
leave.penup()
leave.hideturtle()
leave.goto(-230, -280)
leave.write(f'Если хочешь выйти: "q"', align='right', font=('Verdana', 10, 'normal'))

def leave_game():
    turtle.bye()




# functions
def rocket_left_up():
    y = rocket_left.ycor()
    if rocket_left.ycor() > 250:
        rocket_left.ycor()
    else:
       y += 20
    rocket_left.sety(y)

def rocket_left_down():
    y = rocket_left.ycor()
    if rocket_left.ycor() < -250:
        rocket_left.ycor()
    else:
       y -= 20
    rocket_left.sety(y)

def rocket_right_up():
    y = rocket_right.ycor()
    if rocket_right.ycor() > 250:
        rocket_right.ycor()
    else:
       y += 20
    rocket_right.sety(y)

def rocket_right_down():
    y = rocket_right.ycor()
    if rocket_right.ycor() < -250:
        rocket_right.ycor()
    else:
        y -= 20
    rocket_right.sety(y)


# keyboard

win.listen()
win.onkeypress(rocket_left_up, 'w')
win.onkeypress(rocket_left_down, 's')
win.onkeypress(rocket_right_up, 'Up')
win.onkeypress(rocket_right_down, 'Down')
win.onkeypress(leave_game, 'q')


while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write (f'{player_1}: {score_1}  {player_2}: {score_2}', align='center', font=('Verdana', 20, 'normal'))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write (f'{player_1}: {score_1}  {player_2}: {score_2}', align='center', font=('Verdana', 20, 'normal'))

    if ball.xcor() > 340 and ball.ycor() < rocket_right.ycor() + 50  and ball.ycor() > rocket_right.ycor() - 50:
         ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < rocket_left.ycor() + 50 and ball.ycor() > rocket_left.ycor() - 50:
        ball.dx *= -1

    # End Game

    if score_1 >= 11:
        print(f'{player_1} WIN')
        break
    elif score_2 >=  11:
        print(f'{player_2} WIN')
        break

