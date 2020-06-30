"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`

#read pi from the math library.
pi = math.pi

#The value of pi
print(pi)

#the data type of pi.

print(type(pi))

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if i != 50: 
	if i > 50: 
		print(i," is greater than 50")
	else:
		print(i, "is less than 50")
else:
	print(i, " is equal to 50")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

print(picked_fruit)

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiplier(x,y):
	prod = x*y

	return prod 

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 = ",multiplier(12,96))

print("48 x 17 =", multiplier(48,17))

print("196523 x 87323 =",multiplier(196523,87323))
