#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_di = number % 10
else:
    last_di = number % -10

if last_di > 5:
    print(f"Last digit of {number} is {last_di} and is greater than 5")
elif (last_di < 6 and last_di != 0):
    print(f"Last digit of {number} is {last_di} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_di} and is 0")
