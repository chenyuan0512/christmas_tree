import turtle
from numpy import arange


#設定螢幕長寬
screen = turtle.Screen()
screen.bgcolor("wheat")
screen.setup(800,640)

turtle.penup() #提筆
#預設位置在(0,0)，所以沒有提筆，會從(0,0)移動到我設定的初始座標，會有線(痕跡)
turtle.color("green")#改變比的顏色
turtle.fillcolor("green")#填充顏色
turtle.begin_fill()
turtle.setposition(0,150*3**0.5)#設定初始位置
turtle.pendown()#把筆放下


def walking(angle , length):
    turtle.setheading(angle) #設定移動的方向，以正x軸(東方)方向為0度，正y軸(北方)為90度
    turtle.forward(length) #向前移動多少


def curve_lines(x_left , x_rignt , y_origin , ste , power):
    i = 1
    for x in arange(x_left , x_rignt , ste):
        turtle.goto(x , y_origin - i**power)
        i+=1


def rings(x1 , y1):
    turtle.penup()
    turtle.setposition(x1 , y1)
    turtle.color("#81C0C0")
    turtle.fillcolor("#81C0C0")

    turtle.pendown()
    turtle.begin_fill()
    turtle.pensize(2)
    turtle.circle(10)
    turtle.end_fill()


#畫出上半部
walking(240 , 260)
walking(0 , 60)

walking(240 , 200)
walking(0 , 220)

walking(0 , 120)
walking(120 , 200)

walking(0 , 60)
walking(120 , 260)

turtle.end_fill()

#畫樹幹的部分
turtle.setposition(-50,-138.56)
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.color("brown")
walking(270 , 150)

walking(0 , 100)
walking(90 , 150)

turtle.end_fill()
turtle.penup()

#畫星星#FFDC35
turtle.color("yellow")
turtle.setposition(0,150*3**0.5+25)
turtle.pendown()

turtle.fillcolor("yellow")
turtle.begin_fill()

walking(250 , 35)
walking(30 , 35)
walking(180 , 35)
walking(330 , 35)
walking(110 , 35)

turtle.end_fill()

#畫燈
turtle.color("yellow")
turtle.penup()
turtle.setposition(-50,180)
turtle.pendown()
turtle.pensize(5)

curve_lines(-50 , 60.5 , 180 , 0.5 , 0.5)
curve_lines(60.5 , -89 , 165.13 , -0.5 , 0.7)
curve_lines(-88.5 , 113 , 111.06 , 0.5 , 0.6)
curve_lines(112.5 , -90 , 74.49 , -0.5 , 0.7)
curve_lines(-89.5 , 130 , 7.62 , 0.5 , 0.7)
curve_lines(129.5 , -165 , -63.13 , -0.5 , 0.65)

rings(-30 , 165)
rings(40 , 158)
rings(10 , 80)
rings(100 , 56)
rings(-40 , -25)
rings(80 , -91)

turtle.penup()
turtle.color("#AE57A4")
turtle.fillcolor("#AE57A4")
turtle.setposition(-300 , -200)
turtle.pendown()

turtle.begin_fill()
walking(180 , 50)
walking(270 , 50)
walking(0 , 50)
walking(90 , 50)
turtle.end_fill()

turtle.penup()
turtle.color("#7373B9")
turtle.fillcolor("#7373B9")
turtle.setposition(-300 , -200)
turtle.pendown()

turtle.begin_fill()
walking(90 , 30)
walking(180 , 30)
walking(270 , 30)
walking(0 , 30)
turtle.end_fill()

walking(180 , 10)
walking(90 , 10)

turtle.mainloop()#讓螢幕卡著