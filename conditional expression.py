# conditional expression -> one-liner form of if-else statment as known as ternary operator

num = 10

print("Positive." if num > 0 else "Negative." )

result = ("Even." if num % 2 == 0 else "Odd.")
print(f"The number is {result}")

#exercise

num1 = 3
num2 = 4
age = 16

max_num = num1 if num1 > num2 else num2
min_num = num1 if num1 < num2 else num2

print(f"{max_num} is the maximum number.")
print(f"{min_num} is the minimum number.")

print("Adult." if age >= 18 else "Child.")