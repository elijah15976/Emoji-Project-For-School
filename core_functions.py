def polygon(tut, side, len, lr):
  for i in range(side):
    tut.forward(len)
    if lr == "left":
      tut.left(360/side)
    elif lr == "right":
      tut.right(360/side)

def jump(tut, x, y):
  tut.penup()
  tut.goto(x, y)
  tut.pendown()