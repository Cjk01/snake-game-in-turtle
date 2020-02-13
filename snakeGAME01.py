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
body1.setposition(-40,-40)
body1.color('blue')
body1.shape('square')
body1.penup()
#snakeArr.append(body1)     TEMP MUTE

#length counter for the size of the snake
lengthCount = 20        #was 3

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
        body1 = turtle.Turtle()
        snakeArr.append(body1)

#If snake head position is touching the border, return 1
def borderTouched():
    iBORDER_POS = 273
    iBORDER_NEG = -273
    xPosHead = int(wee.xcor())      #x position of snake head
    yPosHead = int(wee.ycor())      #y position of snake head
    if xPosHead >= iBORDER_POS or xPosHead <= iBORDER_NEG:        #Left or right out of bounds
        return 1
    if yPosHead >= iBORDER_POS or yPosHead <= iBORDER_NEG:        #Top or bottom out of bounds
        return 1



        




#position checker function from positionLog array

def collisionDetector():
    for j in range(len(snakeArr) - 1):
        if snakeArr[j].distance(wee) < 20:
            turtle.done()
            



    
def headTracker():
    snakeArr.append(wee.pos())


#Array used to log the direction
snakePoint = []
snakePoint.append(wee.heading())
def makeTail():
    #trailPos = ((wee.xcor()),(wee.ycor()))
    if wee.distance(body1) > lengthCount or wee.heading() != snakePoint[-1]:
        body1.goto(wee.pos())
        body1.stamp()
        snakePoint.append(wee.heading())

        


#game loop 
running = True
while running:
    wee.forward(0.15)
    window.delay(16.33)
    #lengthUpdater()        TEMP MUTE
    headTracker()
    makeTail()
    #collisionDetector()    TEMP MUTE
    window.update()
    #gameover sequence
    out = borderTouched()
    if out == 1:
        print(snakeArr)
        turtle.done()
        break
    
    

        
    












