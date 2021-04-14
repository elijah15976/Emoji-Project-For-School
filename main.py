import turtle
import time
from core_functions import *

bob = turtle.Turtle()

bob.speed(0)

bob.color("#0077FF")
bob.begin_fill()
polygon(bob, 4, 300, "right")
bob.end_fill()

jump(bob, 50, -50)

bob.color("#3F0000")
bob.begin_fill()
rect(bob, 25, 50, "right")
bob.end_fill()

jump(bob, 225, -50)

bob.color("#3F0000")
bob.begin_fill()
rect(bob, 25, 50, "right")
bob.end_fill()


#Put this at end of code
time.sleep(5)