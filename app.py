# imported turtle module
import turtle
import winsound
wind=turtle.Screen() #screen

wind.title("♥ Kamal & Salma ♥") #title of the window
wind.bgcolor("black") #'window's background
wind.setup(width=800, height=600)
wind.tracer(0) #stop the window from updating

#madrab1
madrab1=turtle.Turtle() #initializes turtle object
madrab1.speed(0)#speed animation
madrab1.shape("square")#shape of the object
madrab1.color("red")#color
madrab1.shapesize(stretch_wid=5,stretch_len=1)#stretches
madrab1.penup()#stops the object from drawing lines
madrab1.goto(-360,0)#set the position
#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("green")
madrab2.shapesize(stretch_wid=5,stretch_len=1)
madrab2.penup()
madrab2.goto(360,0)
#lkora
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3 #delta x
ball.dy = 0.3 #delta y

#score
score1=0
score2=0
score= turtle.Turtle()
score.speed(0)
score.color("red")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(" KAMAL: 0  ♥SOULAYMA♥: 0", align="center", font=("Courier", 24, "bold"))

#
copyright= turtle.Turtle()
copyright.speed(0)
copyright.color("white")
copyright.penup()
copyright.hideturtle()
copyright.goto(0,-260)
copyright.write("SD-PAINK1LL4R02 ♥", align="center", font=("Arial", 10, "normal"))

#functions
def madrab1_up():
    y=madrab1.ycor() #lblassa dyal madrab " hit kitle3 w kinzel safe donc kanchofo ghi y mashi y,x"
    if y <=240:
        y+= 20 #bchhal kitle3
        madrab1.sety(y) # bdelt y 9dima b y jdida


def madrab1_down():
    y=madrab1.ycor()
    if y >= -240:
        y+= -20 #bchhal kihbet
        madrab1.sety(y) # bdelt y 9dima b y jdida

def madrab2_up():
        y=madrab2.ycor() #lblassa dyal madrab " hit kitle3 w kinzel safe donc kanchofo ghi y mashi y,x"
        if y <=240:
            y+= 20 #bchhal kitle3
            madrab2.sety(y) # bdelt y 9dima b y jdida
def madrab2_down():
        y=madrab2.ycor()
        if y >= -240:
            y+= -20 #bchhal kihbet
            madrab2.sety(y) # bdelt y 9dima b y jdida

# Keyboard Bindings
wind.listen()
wind.onkeypress(madrab2_up, 'w')
wind.onkeypress(madrab2_down, 's')
wind.onkeypress(madrab1_up, 'Up')
wind.onkeypress(madrab1_down, 'Down')


#main game loop
while True:
    wind.update()#updates the screen everytime the loop run
    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and everytime loops run : +2 x.axis
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and everytime loops run : +2 y.axis
    #border check , top border +300px, bottom -300px , ball is 10 px
    if ball.ycor() > 290: # if ball is at top border
        winsound.PlaySound('sound.wav', winsound.SND_ASYNC) #sound
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1   #reverse direction

    if ball.ycor() < -290: #bottom
        winsound.PlaySound('sound.wav', winsound.SND_ASYNC) #sound
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: #x right
        winsound.PlaySound('sound.wav', winsound.SND_ASYNC) #sound
        ball.goto(0,0) #lball katrje3 lcentre
        ball.dx *=-1 #katbdel direction d x
        score1 += 1 #score aytzad b 1 l Kamal
        score.clear() #katmse7 score l9dim
        score.write(" KAMAL: {}  ♥SOULAYMA♥: {}".format(score1, score2), align="center", font=("Courier", 24, "bold")) #kat update score
    if ball.xcor() < -390: # x left
        winsound.PlaySound('sound.wav', winsound.SND_ASYNC) #sound
        ball.goto(0,0) #lball katrje3 lcentre
        ball.dx *=-1 #katbdel direction d y
        score2 =+ 1 #score aytzad b 1 l soulayma♥
        score.clear() #katmse7 score l9dim
        score.write(" KAMAL: {}  ♥SOULAYMA♥: {}".format(score1, score2), align="center", font=("Courier", 24, "bold"))

    #kora tdreb madrab
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1
