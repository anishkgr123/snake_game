import turtle
import time
import random
import os 

delay = 0.1

# Score
if os.path.isfile("highScore.txt"):
    f=open("highScore.txt", "r")
    high_score=int(f.read())
    f.close()
else:
    high_score = 0

score = 0

# f = open("highScore.txt", "w")
# f.write(str(high_score))
# f.close()

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# Border

turtle.speed(5)
turtle.pensize(10)
turtle.penup()
turtle.goto(-310, 310)
turtle.pendown()
turtle.color("red")
turtle.forward(620)
turtle.right(90)
turtle.forward(620)
turtle.right(90)
turtle.forward(620)
turtle.right(90)
turtle.forward(620)
turtle.right(90)
turtle.penup()
turtle.hideturtle()


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("yellow")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Score: 0  High Score: "+str(high_score), align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"


        for segment in segments:
            segment.goto(1000, 1000)
        
    
        segments.clear()

        
        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        
        delay -= 0.001

    
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        
        f = open("highScore.txt", "w")
        f.write(str(high_score))
        f.close()
        
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()

            score = 0

            delay = 0.1
        
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            
            
            
    time.sleep(delay)
    



  
wn.mainloop()



