from turtle import *
n = int(input("enter a number: ")) #khai bao bien
for i in range(40): #tao vong lap
    forward(10*n+1) 
    left(90)
    n=n+1 #tang gia tri bien
mainloop() # = return(0)