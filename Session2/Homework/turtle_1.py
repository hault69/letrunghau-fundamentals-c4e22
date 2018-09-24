from turtle import *
color("red","white")
begin_fill()
for n in range(4):
    for i in range(2):
        forward(100)
        right(45)
        forward(100)
        right(135)
    left(90)
end_fill()
mainloop() 