import turtle
import time
import random
from core_functions import *
from emoji import *

em = random.randint(1, 2)

print("You Got:")

if em == 1:
  print("MOODY GUY")
  Moody()
elif em == 2:
  print("HAPPY GUY")
  Happy()


#Put this at end of code
time.sleep(5)
