import turtle
import time
from core_functions import *

bob = turtle.Turtle()

bob.color(0, 100, 200)
bob.begin_fill()
polygon(bob, 4, 300, "right")
bob.end_fill()


#Put this at end of code
time.sleep(5)