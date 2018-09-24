from turtle import *

for n in range(4):
    if n%2==0:
        color("red","white")
        begin_fill()
        for i in range(6-n):
            forward(100) 
            left(360/(6-n))
        end_fill()
    else:
        color("blue","white")
        begin_fill()
        for i in range(6-n):
            forward(100) 
            left(360/(6-n))
        end_fill()
mainloop() 