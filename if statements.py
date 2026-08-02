#if Statement : It performs certain task or executes code if some condition is true
# else it executes some other task if that condition is false

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You entered invalid age.")
else:
    print("You are under age!")

#example

response = input("Would you like to have some food? (Y/N): ")

if response == "Y" or response == "y":
    print("Kindly place order...!")
elif response == "N" or response == "n":
    print("Thank you for the visit.")
else:
    print("Invalid response entered")

#example

name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")