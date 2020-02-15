

import turtle
import math
import random

#creating the play area

window = turtle.Screen()
window.bgcolor('black')
window.setup(600,600)



#creating a border representing the play area

border = turtle.Turtle()
border.penup()
border.setposition(-285,-285)
border.pendown()
border.speed(0)
border.pencolor('white')
border.pensize(3)
for side in range(4):
    border.forward(570)
    border.left(90)
border.hideturtle()

#creating the head of the snake

head = turtle.Turtle()
head.shape('square')
head.color('green')
head.speed(0)
head.penup()




#If snake head position is touching the border, end the game
def borderTouched():
    iBORDER_POS = 273
    iBORDER_NEG = -273
    xPosHead = int(head.xcor())
    yPosHead = int(head.ycor())
    if xPosHead >= iBORDER_POS or xPosHead <= iBORDER_NEG:        #Left or right out of bounds
        turtle.done()
    elif yPosHead >= iBORDER_POS or yPosHead <= iBORDER_NEG:        #Top or bottom out of bounds
        turtle.done()





    
        


#defining movement functions to be called by direction checker function
iMOVEMENT_AMOUNT = 20

def moveUp():
    head.seth(90)
      

def moveLeft():
    head.seth(180)
   
    
      
def moveDown():
    head.seth(270)
    
   
def moveRight():
    head.seth(0)
   
  

#direction checker function that calls the movement function associated with it
def movement():
    if head.heading() == 90:
        head.sety(head.ycor() + iMOVEMENT_AMOUNT )
    if head.heading() == 180:
        head.setx(head.xcor() - iMOVEMENT_AMOUNT )
    if head.heading() == 270:
        head.sety(head.ycor() - iMOVEMENT_AMOUNT )
    if head.heading() == 0:
        head.setx(head.xcor() + iMOVEMENT_AMOUNT )


#calling movement functions with user input
turtle.listen()
turtle.onkeypress(moveUp, "Up")
turtle.onkeypress(moveLeft, "Left")
turtle.onkeypress(moveDown, "Down")
turtle.onkeypress(moveRight, "Right")


#apple object to be randomly generated later on
apple = turtle.Turtle()
apple.hideturtle()
apple.shape('circle')
apple.penup()
apple.color('red')
apple.speed(0)
apple.goto(-90,-100)
apple.showturtle()

#detect collision with snake head and apple
def appleTouched():
    if head.distance(apple) < 20:
        apple.goto(random.randrange(-270, 270, 20),random.randrange(-270, 270, 20))

        





running = True
while running:
    window.delay(60)
    borderTouched()
    movement()
    appleTouched()
    window.update()


    







    

    



