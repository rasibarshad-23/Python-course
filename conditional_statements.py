#if Statement : It performs certain task or executes code if some condition is true
# else it executes some other task if that condition is false

age = int(input("Enter your age: "))

if (age >= 18):
    print("You are now signed up!")
elif (age < 0):
    print("You entered invalid age.")
else:
    print("You are under age!")

#example

response = input("Would you like to have some food? (Y/N): ")

if (response == "Y" or response == "y"):
    print("Kindly place order...!")
elif (response == "N" or response == "n"):
    print("Thank you for the visit.")
else:
    print("Invalid response entered")

#example

name = input("Enter your name: ")

if (name == ""):
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

for_sale = True

if (for_sale):
    print("This item is for sale")
else:
    print("This item is not for sale")

#exercise
marks = int(input("Enter your marks: "))

if(marks > 100 or marks <= 0):
    print("Invalid marks.")
elif(marks >= 90):
    print("Your grade is 'A'.")
elif(90 > marks >= 80):
    print("Your grade is 'B'.")
elif(80 > marks >= 70):
    print("Your grade is 'C'.")
elif(marks < 70):
    print("Your grade is 'D'.")

#exercise
number = int(input("Enter any positive number (0-9): "))

if(number > 9 or number < 0):
    print("INVALID ENTRY!!!")
elif(number % 2 == 0):
    print("Number is Even.")
else:
    print("Number is Odd.")

#exercise
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3= int(input("Enter third number: "))

if(n1 > n2 and n1 > n3):
    print(n1, "is the greatest number.")
elif(n2 > n1 and n2 > n3):
    print(n2, "is the greatest number.")
else:
    print(n3, "is the greatest number.")

#exercise

num = int(input("Enter a positive number: "))

if(num < 0 ):
    print("INVALID ENTRY!!")
elif(num % 7 == 0):
    print(num, "is multiple of 7.")
else:
    print(num, "is not the multiple of 7.")