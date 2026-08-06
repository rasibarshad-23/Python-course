#input() -> function to take input of data from the user (always returns the entered data in string)

name = input("What is your name: ")
age = int(input("How old are you: "))

age += 1

print(f"Your name is {name}")
print("Your name is ", name) #both are same -> either simple or fstring
print(f"You are {age} years old")

#exercise to calculate the area of rectangle

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width

print(f"Area of retangle = {area}cm")

#exercise: shopping cart program

item = input("Enter your item: ")
price = float(input("Enter the price of one unit: "))
quantity = int(input("Enter the quantity you want to buy: "))

total_bill = price * quantity

print(f"You bought {item} x {quantity}")
print(f"Your total bill is: Rs {total_bill}/-")