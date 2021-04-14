import turtle

bob = turtle.Turtle()


def polygon(tut, side, len, lr):
  for i in range(side):
    tut.forward(len)
    if lr == left:
      tut.left(360/side)
    elif lr == right:
      tut.right(360/side)