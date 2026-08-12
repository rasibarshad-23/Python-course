# Functions -> Block of code to reduce redundancy

def calc_sum(a, b): # Function definition -> function_name(parameters ; optional)
    sum = a + b
    print("Sum: ", sum)
    return sum # Optional

calc_sum(10, 15) # Function Call -> function_name(arguments)
calc_sum(2, 5) 

# Exercise
def avg(num1:int, num2:float, num3): # Can also assign specific data types to parameters
    average = (num1 + num2 + num3) / 3
    print("Average is: ", round(average, 2))

avg(2, 3.4, 5)

# Default parameters
def calc_sum(a = 1, b = 2):
    return a + b

sum = calc_sum()
print(sum)

# Exercise
def calc_length(a:list):
    return len(a)

num = [1, 2, 3, 4, 5]
length = calc_length(num)
print("Length of list: ", length)

# Exercise
def print_ele(a:list):
    for i in range(0, len(a)):
        print(a[i], end=" " ) # to print on the same line

num = [1, 2, 3, 4, 5]
print_ele(num)

# Exercise
def calc_factorial(a:int):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact

num = int(input("Enter number to find factorial: "))
factorial = calc_factorial(num)
print("Factorial: ", factorial)

# Exercise
def dollar_to_pkr(dollar:float):
    result = dollar * 277.48
    return result

amount = float(input("Enter amount in dollar: "))
pkr = dollar_to_pkr(amount)
print("Amount in PKR: Rs", round(pkr, 2))

# Exercise
def even_odd(num:int):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
result = even_odd(n)
print("The Number is: ", result)

# Recursion
def show(a):
    if a == 0: # Base case
        return
    print(a)
    show(a - 1) # Recursive call

show(5)

# def fact(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fact(a - 1)

n = int(input("Enter number to find factorial: "))
factorial = fact(n)
print("Factorial: ", factorial)

# Exercise
def calc_sum(a:int):
    if a == 0:
        return 0
    return calc_sum(a - 1) + a

result = calc_sum(5)
print("Sum: ", result)

# Exercise
def print_ele(a:list, idx = 0):
    if idx == len(list):
        return
    print(a[idx], end=" ")
    print_ele(a, idx + 1)

list = [1, 2, 3, 4]
print_ele(list)