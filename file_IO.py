# # Reading the file

# f = open("demo.txt", "r") # r is reading mode (default)
# data = f.read(5) # can also specify no. of character to read
# print(data)
# print(type(data))
# line1 = f.readline() # reads one line at a time
# print(line1)
# f.close()

# # Writing in the file

# f = open("demo.txt", "w") # W is for over writing in the file (deletes previous data)
# f.write("Hello 123") 
# f.close()

# f = open("demo.txt", "a") # a is for append (adds data at the end of the file)
# f.write("Hello 123") 
# f.close()

# # If file is opened in writing mode and it does not exists, Python automatically creates file with that name.

# # Reading and Writing in the file

# # 'r+' -> It does not truncates the file (still overwrites), the pointer is placed at the beginning of the file.
# # 'w+' -> It truncates the file and allows read & overwrite.
# # 'a+' -> Pointer is at the end of the file, allows read & append.

# # with Syntax
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)
#     # with automatically closes the file, you do not have to do it manually

# # Deleting the file
# import os # Module to delete a file
# os.remove("demo.txt") 

# # Exercise
# with open("practice.txt", "a+") as f:
#     f.write("Hi everyone\nWe are learning file I/O\nusing Java\nI like programming in Java")

# # Exercise
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")

# with open("practice.txt", "w+") as f:
#     f.write(new_data)

# # Exercise
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
# if data.index(word) != -1:
#     print("Found.")
# else:
#     print("Not found.")

# # Exercise
# word = "using"

# def search_line_no(): 
#     with open("practice.txt", "r") as f:
#         data = True
#         line_no = 1
#         while data:
#             line = f.readline()
#             if line.find(word) != -1:
#                 return line_no
#             line_no += 1
#         return -1

# print(search_line_no())

# # Exercise
# count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()

#     new_data = data.split(",")
#     print(new_data)

#     for val in new_data:
#         if int(val) % 2 == 0:
#             count += 1
#     print("Count of even number: ", count)

import os
os.remove("practice.txt")