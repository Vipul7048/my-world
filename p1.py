from turtle import Turtle
vip = Turtle()
vip.color('red')
vip.shape('turtle')
vip.penup()
vip.goto(-160, 100)
vip.pendown()
from random import randint

for movement in range(100):
 vip.forward(randint(1,5))
import winsound
frequency = 50 # Set Frequency To 2500 Hertz
duration = 1500  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
