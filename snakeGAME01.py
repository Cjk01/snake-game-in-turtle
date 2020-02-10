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
    

#length counter for the size of the snake
lengthCount = 4


#Creating the snake squares + an array to store the seperate turtles inside
snakeArr = []


#wee is the snake head
wee = turtle.Turtle()
snakeArr.append(wee)
wee.color('green')
wee.shape('square')
wee.penup()
wee.setposition(0,0)
wee.forward(20)


#defining body square to be repeated
body1 = turtle.Turtle()
snakeArr.append(body1)
body1.color('blue')
body1.shape('square')
body1.penup()
body1.setposition(0,0)
body1.forward(0)



#function to update the length of the snakeArr when lengthCount > arr.len
def lengthUpdater():
    if len(snakeArr) < lengthCount:
        bodytemp = turtle.Turtle()
        snakeArr.append(bodytemp)


lengthUpdater()









