import turtle
import time
import random
from core_functions import *
from emoji import *

em = random.randint(1, 3)

print("You Got:")

if em == 1:
  print("MOODY GUY")
  Moody()
elif em == 2:
  print("HAPPY GUY")
  Happy()
elif em == 3:
  print("SAD GUY")
  Sad()
else:
  print("Something went wrong, please try again.")
  print("\nError: Num greater than 3 or less than 1")


#Put this at end of code
time.sleep(5)
