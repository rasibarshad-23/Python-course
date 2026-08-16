# # Object Oriented Programming -> involves classes and objects (real-world scenarios)

# # Class -> Blueprint of an object
# class Student:
# # Constuctor (__int__()) -> Automatically called function when object is created
#     # Default Constructor
#     def __init__(self):
#         pass

#     # Paramterized constructor
#     def __init__(self, name, marks): # self is default paramter of constructor, points to new object
#         self.name = name # new variable of name will be created and value in fullname will be assigned to new object
#         self.marks = marks
#         print("Creating new student in class...")

#     college = "NIIT" # Common attribute for all objects -> Can also be accessed using class name

#     def welcome(self): # self parameter is compulsory
#         print("Welcome", self.name)

#     def get_marks(self):
#         return self.marks
# # Precedence of object attribute > class attribute (common attribute)

# # Object -> Instance of class
# s1 = Student("Rasib", "98") # Can pass argument through constructor
# s1.welcome()
# print("Marks obtained: ", s1.get_marks())
# print("College: ", s1.college)

# s2 = Student("Rasib Arshad", "95")
# s2.welcome()
# print("Marks obtained: ", s2.get_marks())
# print("College: ", s2.college)

# # Exercise
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avg_marks(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         return sum/len(self.marks)

#     # Decorator for static method
#     @staticmethod # Static method -> Can be operated using class or object
#     def welcome():
#         print("Hello")

# std = Student("Rasib", [95, 98, 92] )
# std.welcome()
# print("Welcome", std.name)
# print("Average marks: ", std.avg_marks())

# # Abstraction -> Hiding the implementation details of the class, only showing essential features to user
# class Car:
#     def __init__(self):
#         self.accelerator = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True # Implementation Hidden
#         self.accelerator = True # Implementation Hidden
#         print("Car started.") # Essential feature shown

# car1 = Car()
# car1.start()

# # Encapsulation -> Wrapping data and methods in a single unit (object) -> capsule

# # Exercise
# class Account:
#     def __init__(self, balance:int, account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def debit(self, amount:int):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("Insufficient balance.")

#     def credit(self, amount:int):
#         self.balance += amount

#     def display_balance(self):
#         print("Your balance is: ", self.balance)

# person1 = Account(5400, "RAS23")
# print("Before debit.")
# person1.display_balance()
# person1.debit(400)
# print("After debit.")
# person1.display_balance()

# print("Before credit.")
# person1.display_balance()
# person1.credit(700)
# print("After credit.")
# person1.display_balance()

# # del keyword -> Used to delete attribute of an object or an entire object
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Rasib")
# print(s1.name)
# del s1 # object deleted
# print(s1.name)

# # Private attribute
# class BankAccount:
#     def __init__(self, account_no, __account_pass):
#         self.account_no = account_no
#         self.__account_pass = __account_pass # can only be accessed inside the class

# user1 = BankAccount("1234", "abcde")
# print(user1.account_no)
# print(user1.__account_pass) # It becomes hidden for user

# Inheritance -> One class (child) inherits the properties and methods of another class (parent)
# Single Inheritance
class Car: # Parent class
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car): # Child class -> Inherits from Car (Parent class)
    def __init__(self, brand):
        self.brand = brand

    @staticmethod
    def demo():
        print("Function of ToyotaCar class")

# Multi-Level Inheritance
class VitzCar(ToyotaCar): # Grand child -> Inherits from ToyotaCar (parent) -> Inherits form Car (grand parent)
    def __init__(self, type):
        self.type = type

    @staticmethod
    def demo1():
        print("Function of vitzCar class")


vitz1 = VitzCar("Electric (PHEV)")
vitz1.start() # Function of Car (grandparent)
vitz1.demo() # Function of ToyotaCar (parent)
vitz1.demo1() # Function of VitzCar (child)
vitz1.stop() # Function of Car (grandparent)