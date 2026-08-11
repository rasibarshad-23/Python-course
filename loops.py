# Loops -> Used to repeat set of instructions for certain times
# While Loop -> Condition (check first) : Set of statements (execute based of condition) : Increment/Decrement(optional)

# counter = 1
# while(counter <= 5):
#     print("Hello", counter)
#     counter += 1

# Exercise
# i = 1
# while(i <= 100):
#     print(i)
#     i += 1

# Exercise
# i = 100
# while(i >= 1):
#     print(i)
#     i -= 1

# Exercise
# n = int(input("Enter any number (greater than 0): "))
# i = 1
# if(n > 0):
#     while(i <= 10):
#         print(n ,"*", i ,"=", n*i)
#         i += 1
# else:
#     print("Invalid number!")

# Exercise
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while(i < len(list)):
#     print(list[i])
#     i += 1

# Exercise
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = int(input("Enter the number you want to search in the list: "))
# i = 0
# while(i < len(tuple)):
#     if(tuple[i] == x):
#         print("Found at index: ", i)
#         break
#     else:
#         print("Finding...")
#     i += 1

# break
# i = 1
# while(i <= 5):
#     print(i)
#     if(i == 3):
#         break # control comes out of the loop
#     i += 1

# continue
# i = 1
# while(i <= 5):
#     if(i == 3):
#         i += 1
#         continue # control goes back to loop
#     print(i)
#     i += 1

# for Loop
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# for i in list:
#     if  i ==  3:
#         break
#     print(i)
#     i += 1
# else: # only executes if the complete loop is iterated
#     print("END")

# Exercise
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in list:
#     print(i)

# Exercise
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter the number to search: "))
# idx = 0
# for i in tuple:
#     if(i == x):
#         print("Found at index: ", idx )
#         break
#     idx += 1
# else:
#     print("Not found")

# Range
# for i in range(5): #range(stop)
#     print(i)

# for i in range(2, 5): #range(start, stop)
#     print(i)

# for i in range(1, 5, 2): #range(start, stop, step)
#     print(i)

# Exercise
# for i in range (101):
#     print(i)

# Exercise
# for i in range (100, 0, -1):
#     print(i)

# Exercise
# n = int(input("Enter any number: "))
# for i in range(11):
#     print(n, "*", i, "=", n*i)

# pass
# for i in range(4):
#     pass # placeholder for future code

# Exercise
n = int(input("Enter the number you want sum for: "))
sum = 0
i = 0
while i <= n:
    sum += i
    i += 1
print("Sum: ", sum)

# Exercise
# n = int(input("Enter the number you want factorial for: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print("Factorial: ", factorial)