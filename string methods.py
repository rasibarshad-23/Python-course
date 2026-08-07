
# name = input("Enter your full name: ")

# count = len(name) #used to find the lenght of the string
# print(f"Letter count: {count}")

# find = name.find("a") #used to find the first occurence of any character in string
# print(f"First occurence of letter 'a' is at {find}th index.")

# rfind = name.rfind("a") #used to find the last occurence of any character in string
# print(f"Last occurence of letter 'a' is at: {rfind}th index.")

# name = name.capitalize() #only capitalized first letter of the string
# print(f"Capitalized first letter: {name}.")

# name = name.upper() #converts complete string to UPPERCASE
# print(f"Your name in uppercase: {name}.")

# name = name.lower() #converts complete string to lowercase
# print(f"Your name in lowercase: {name}.")

# result = name.isdigit() #only returns True if string has only numbers
# print(f"Is this string a number? {result}.")

# result = name.isalpha() #only returns True if string only contains alphabets
# print(f"Is this string an alphabet? {result}.")

# count = name.count("a") #counts occurences of any character you want to in the string
# print(f"The letter 'a' in you name is {count} times.")

# name = name.replace("r", "j") #used to replace character with any other character
# print(f"Your name replaced version: {name}.")

# print(help(str)) #useful string methods detail


# #exercise

# username = input("Enter your username: ")

# if len(username) > 12:
#     print("Your username cannot be greater than 12 characters.")
# elif username.isalpha() == False:
#     print("Your username cannot contain spaces OR digits.")
# else:
#     print(f"Welcome {username}.")

# #concatenation
# str1 = "Rasib" 
# str2 = "Arshad"
# print(str1 + " " + str2)

email = "f2024se004@niit.edu.pk" 
print(email.endswith("@niit.edu.pk")) #checks if string ends with specific characters - returns (True/False)

