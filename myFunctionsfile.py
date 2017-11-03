#Eldon Wu
#myFunctionsfile
def square(t,d):#def defines a funtion parameters are information functions needs
    for times in range(4):
        t.forward(d)
        t.right(90)


def triangle(t,d):
    for times in range(3):
        t.forward(d)
        t.right(120)


def polygon(t,s,d): #parameters(information)
    a = 360/s #angle variable is inside the function
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.right(a)
    t.end_fill()


def jump(t,x,y): #parameters(information)
    t.penup()
    t.goto(x,y)
    t.pendown()


def cool2(t,d,c1,c2): #parameters(information)
    t.color(c1)
    polygon(t,5,d) #call to the function polygon
    t.color(c2)
    polygon(t,3,d)


def dottedline(t,c,rad):
    t.color(c)
    t.penup()
    t.forward(100)
    t.pendown()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

def sharpcircle(t,l,r):
    t.penup()
    t.forward(70)
    t.pendown()
    t.forward(60)
    t.left(l)
    t.forward(60)
    t.right(r)






