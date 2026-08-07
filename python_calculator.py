#simple arithmetic operations calculator using if statements

op1 = float(input("Enter your first operand: "))
op2 = float(input("Enter your second operand: "))

operation = input("Enter the operation you want to perform (+, -, *, /, %) : ")

if operation == "+":
    result = op1 + op2
    print(f"Result: {op1} + {op2} = {result}")
elif operation == "-":
    result = op1 - op2
    print(f"Result: {op1} - {op2} = {result}")
elif operation == "*":
    result = op1 * op2
    print(f"Result: {op1} * {op2} = {result}")
elif operation == "/":
    result = op1 / op2
    print(f"Result: {op1} / {op2} = {result}")
elif operation == "%":
    result = op1 % op2
    print(f"Result: {op1} % {op2} = {result}")
else:
    print("Invalid operator entered")