#Eldon Wu #Design Project
import turtle #imports turtle libary
turtle.colormode(255)
from myFunctionsfile import*
ted = turtle.Turtle()
ted.speed(0)
color1 = (135,206,250)
color2 = (255,255,255)
for times in range(74):
    cool2(ted,30,color1,color2)
    ted.penup()
    ted.forward(times*5)
    ted.pendown()
    ted.right(199)
ted.penup()
ted.goto(-10,-65)
ted.pendown()
ted.begin_fill()
for times in range(40):
    ted.color(135,206,250)
    sharpcircle(ted,190,120)
ted.color(255,255,255)
ted.end_fill()
ted.penup()
ted.goto(113,108)
ted.pendown()
for times in range(25):
    dottedline(ted,(255,0,0),2)
    ted.right(120)
    dottedline(ted,(0,100,0),2)
    ted.right(190)
    dottedline(ted,(0,100,0),2)
    ted.right(120)
    dottedline(ted,(255,0,0),2)
ted.penup()
ted.goto(1000,17889)
turtle.done
