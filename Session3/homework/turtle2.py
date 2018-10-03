from turtle import *
colors = ['red','blue','brown','yellow','gray']
for i in range(5):
    color(colors[i])
    begin_fill()
    left(90)
    forward(100)
    left(90)
    forward(300-60*i)
    left(90)
    forward(100)
    left(90)
    forward(300-60*i)
    end_fill()
mainloop()