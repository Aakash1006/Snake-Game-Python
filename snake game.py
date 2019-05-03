import turtle
import random
import time

wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("lightblue")
wn.setup(width=480, height=480)
wn.tracer(0)

delay=0.1
ch=0



#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.shapesize(stretch_wid=0.8, stretch_len=0.8)
head.penup()
head.goto(0,0)
head.dx=ch
head.dy=0
head.f=0


#apple
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(stretch_wid=0.6, stretch_len=0.6)
food.penup()
food.goto(random.randint(-220,220),random.randint(-220,220))

st = turtle.Turtle()
st.speed(0)
st.color("red")
st.penup()
st.hideturtle()
st.goto(0, 200)
st.write("Snake game!",align="center",font=("Courier",30,"bold"))
st.goto(0,100)
st.write("Press Enter to start.",align="center",font=("Courier",20,"bold"))
st.goto(0,70)
st.write("Start moving with arrow keys.",align="center",font=("Courier",15,"bold"))



def goup():
    if(head.dy >=0):
        head.dy=ch
        head.dx=0

def godown():
    if(head.dy<=0):
        head.dy=-ch
        head.dx=0

def goright():
    if(head.dx>=0):
        head.dx=ch
        head.dy=0

def goleft():
    if(head.dx<=0):
        head.dx=-ch
        head.dy=0

def spac():
    head.f=1
    st.clear()

wn.listen()
wn.onkeypress(goup,"Up")
wn.onkeypress(godown,"Down")
wn.onkeypress(goleft,"Left")
wn.onkeypress(goright,"Right")
wn.onkeypress(spac,"Return")
length=[]
tails=1
length.append(head)
points=0





while (True):
        wn.update()

        if(head.f==1):
            ch=15
        if head.distance(food)<15:
            food.goto(random.randint(-220, 220), random.randint(-220, 220))
            tail=turtle.Turtle()
            tail.speed(0)
            tail.shape("square")
            tail.color("orange")
            tail.shapesize(stretch_wid=0.8, stretch_len=0.8)
            tail.penup()
            tail.goto(length[tails-1].xcor(),length[tails-1].ycor())
            length.append(tail)
            delay-=0.005
            points+=1
            tails+=1

        if(head.xcor()>230):
            head.setx(-230)
        if (head.xcor() < -230):
            head.setx(230)
        if (head.ycor() > 230):
            head.sety(-230)
        if (head.ycor() < -230):
            head.sety(230)



        for i in range(len(length)-1,0,-1):
            length[i].setx(length[i-1].xcor())
            length[i].sety(length[i - 1].ycor())

        for i in range(len(length)-1,1,-1):
            if(head.distance(length[i])<5):
                wn.clear()
                wn.bgcolor("lightblue")
                pen = turtle.Turtle()
                pen.speed(0)
                pen.color("red")
                pen.penup()
                pen.hideturtle()
                pen.goto(0, 0)
                pen.write("GAME OVER!",align="center",font=("Courier",30,"bold"))
                pen.goto(0,-100)
                pen.color("green")
                pen.write("Your score is: {}".format(points), align="center", font=("Courier", ch, "bold"))



        time.sleep(0.1)
        head.setx(head.xcor()+head.dx)
        head.sety(head.ycor()+head.dy)



