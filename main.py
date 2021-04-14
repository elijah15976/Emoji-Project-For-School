import turtle
import time

bob = turtle.Turtle()


def polygon(tut, side, len, lr):
  for i in range(side):
    tut.forward(len)
    if lr == left:
      tut.left(360/side)
    elif lr == right:
      tut.right(360/side)

polygon(bob, 4, 100, right)


#Put this at end of code
time.sleep( 5 )