# Logical operators in Python (AND, OR, NOT)
# AND -> Both conditions must be True
# OR -> At least one condition should be True
# NOT -> Negation of something

temp = -8
is_raining = False

if temp > 35 or temp < 0  or is_raining:
    print("Outdoor event is cancelled due to bad weather conditions.")
else:
    print("Outdoor event is scheduled as per routine.")


is_sunny = True

if temp >= 25 and is_sunny:
    print("It is HOT outside AND it is sunny.")
elif temp < 0:
    print("It is COLD outside AND it is sunny.")