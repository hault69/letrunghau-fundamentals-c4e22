from turtle import *
colors = ['red','blue','brown','yellow','gray']
for n in range(5):
    color(colors[4-n])
    for i in range(7-n):
        forward(100) 
        left(360/(7-n))
mainloop() 