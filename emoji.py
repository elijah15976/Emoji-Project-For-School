import turtle
from core_functions import *

def Moody():
  bob = turtle.Turtle()
  bob.speed(0)

  bob.color("#0077FF")

  #Box head
  jump(bob, -150, 150)
  bob.begin_fill()
  polygon(bob, 4, 300, "right")
  bob.end_fill()

  bob.color("#3F0000")
  #Left Eye
  jump(bob, -100, 100)
  bob.begin_fill()
  rect(bob, 25, 50, "right")
  bob.end_fill()

  #Right Eye
  jump(bob, 75, 100)
  bob.begin_fill()
  rect(bob, 25, 50, "right")
  bob.end_fill()

  #Mouth
  jump(bob, -50, -75)
  bob.begin_fill()
  rect(bob, 100, 25, "right")
  bob.end_fill()

  bob.color("#0037FF")

  #Nose
  jump(bob, 0, 0)
  bob.begin_fill()
  bob.circle(10)
  bob.end_fill()

  bob.color("#000000")

  #Eye Brows
  jump(bob, -115, 100)
  bob.begin_fill()
  rect(bob, 230, 15, "left")
  bob.end_fill()