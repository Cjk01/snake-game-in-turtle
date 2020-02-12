#imports
import turtle
import math
import random


#create play area
window = turtle.Screen()
window.bgcolor('black')
window.tracer(3)
window.setup(600,600)

#creating a border
border = turtle.Turtle()
border.color('white')
border.penup()
border.setposition(-285,-285)
border.pendown()
border.pencolor('white')
border.pensize(3)
for side in range(4):
    border.forward(570)
    border.left(90)
border.hideturtle()

#Creating the snake squares + an array to store the seperate turtles inside
snakeArr = []


#wee is the snake head
wee = turtle.Turtle()
wee.setposition(0,0)
wee.shape('square')
wee.color('green')
wee.penup()
wee.speed(10)
snakeArr.append(wee)




#defining body square to be repeated
body1 = turtle.Turtle()
body1.setposition(0,0)
body1.color('blue')
body1.shape('square')
body1.penup()
snakeArr.append(body1)   

#length counter for the size of the snake
lengthCount = 2

#defining movement functions 
def moveUp():
    wee.seth(90)
    
def moveLeft():
    wee.seth(180)
    
def moveDown():
    wee.seth(270)
    
def moveRight():
    wee.seth(0)




#calling movement functions with user input
turtle.listen()
turtle.onkeypress(moveUp, "Up")
turtle.onkeypress(moveLeft, "Left")
turtle.onkeypress(moveDown, "Down")
turtle.onkeypress(moveRight, "Right")



#function to update the length of the snakeArr when lengthCount > arr.len
def lengthUpdater():
    if len(snakeArr) < lengthCount:
        bodytemp = turtle.Turtle()
        snakeArr.append(bodytemp)
#game loop 
running = True
while running:
    wee.forward(0.15)
    window.delay(16.33)
    window.update()
    
    

        
    












