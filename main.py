import turtle
import time
from core_functions import *

bob = turtle.Turtle()

bob.speed(0)

jump(bob, -150, 150)

bob.color("#0077FF")
bob.begin_fill()
polygon(bob, 4, 300, "right")
bob.end_fill()

jump(bob, -100, 100)

bob.color("#3F0000")
bob.begin_fill()
rect(bob, 25, 50, "right")
bob.end_fill()

jump(bob, 75, 100)

bob.begin_fill()
rect(bob, 25, 50, "right")
bob.end_fill()

jump(bob, -50, -75)

bob.begin_fill()
rect(bob, 100, 25, "right")
bob.end_fill()


#Put this at end of code
time.sleep(5)