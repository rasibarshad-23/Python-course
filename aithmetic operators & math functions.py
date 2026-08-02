# arithmetic operators & math functions
import math

friends = 0
friends = friends + 1
friends += 1 #augmented assignment operator (same for sub, mul and div)
friends = friends**2 #exponent operator **
friends **= 2
print(friends)

# Built-in maths functions
x = 3.14
y = -3

result = round(x) #rounds-off to nearest whole number
print(result)

absolute = abs(y) #gives absolute value
print(absolute)

power = pow(3, 2) #power function
print(power)

print(max(x, y)) #gives maximum value
print(min(x, y)) #gives minimum value

print(math.pi) #gives value of pi (3.14....)
print(math.e) #gives value of e (2.71....)
print(math.sqrt(25)) #give square root of the number
print(math.ceil(9.1)) #rounds-off a number upwards
print(math.floor(9.1)) #rounds-off a number downwards

#practice exercise (circumference of circle)

radius = float(input(("Enter radius of the cricle: ")))
pi = math.pi
circum = (2*pi*radius)
print(f"Circumference of circle: {round(circum, 3)}")



