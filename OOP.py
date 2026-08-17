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

# # Inheritance -> One class (child) inherits the properties and methods of another class (parent)
# # Single Inheritance
# class Car: # Parent class
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class ToyotaCar(Car): # Child class -> Inherits from Car (Parent class)
#     def __init__(self, brand):
#         self.brand = brand

#     @staticmethod
#     def demo():
#         print("Function of ToyotaCar class")

# # Multi-Level Inheritance
# class VitzCar(ToyotaCar): # Grand child -> Inherits from ToyotaCar (parent) -> Inherits form Car (grand parent)
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def demo1():
#         print("Function of vitzCar class")


# vitz1 = VitzCar("Electric (PHEV)")
# vitz1.start() # Function of Car (grandparent)
# vitz1.demo() # Function of ToyotaCar (parent)
# vitz1.demo1() # Function of VitzCar (child)
# vitz1.stop() # Function of Car (grandparent)

# # Multiple Inheritance -> Child inherits from multiple parents
# class A:
#     varA = "I am Class A."

# class B:
#     varB = "I am class B." 

# class C(A, B): # Inherited from multiple classes (Parents)
#     varC = "I am class C."

# demo = C()
# print(demo.varC) # Accessing own variable
# print(demo.varB) # Accessing varaible of 2nd parent
# print(demo.varA) # Accessing variable of 1st parent

# # Super method -> For accessing methods and data of parent class
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car is started.")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type) # calls the parent consturctor and assigns value to type
#         self.name = name
#         super().start()

# car1 = ToyotaCar("Vitz", "PHEV")
# print(car1.name)
# print(car1.type)

# # Class methods
# class A:
#     name  = "Anonymous"
#     @staticmethod
#     def hello():
#         print("Hello.")

#     @classmethod
#     def changeName(cls):
#         cls.name = "Rasib" # Changes the default value of name from anonymous to Rasib

# person1 = A()
# print(person1.name) # Before changing the name
# person1.changeName()
# print(person1.name) # After changing the name
# print(A.name) # Changed for class -> common attribute -> name = "Rasib"

# # @property decorator -> returns latest value from a method (turns method into attribute)
# class Student:
#     def __init__(self, maths, phy, chem):
#         self.maths = maths
#         self.phy = phy
#         self.chem = chem

#     @property
#     def percentage(self):
#         return str(round((self.maths + self.phy + self.chem) / 3, 2)) + "%"

# std1 = Student(98, 97, 94)
# print(std1.percentage) # prints latest calculated percentage
# std1.phy = 92 # Value of attribute changed
# print(std1.percentage) # prints updated percentage

# # Polymorphism -> using one thing in many form (operator overloading)
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def show(self):
#         print(self.real, "i + ", self.img, "j")

#     def __add__(self, num2): # Dunder function for overloading + operator
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __sub__(self, num2): # Dunder function for overloading - operator
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(4, 3)
# num1.show()
# num2 = Complex(3, 2)
# num2.show()
# num3 = num1 + num2 # Simple add operator can now add two complex numbers using operator overloading
# num3.show()
# num4 = num1 - num2 # Subtraction operator overloaded
# num4.show()


#  # Exercise
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def Area(self):
#         return (round(math.pi * pow(self.radius, 2), 2))

#     def Perimeter(self):
#         return (round(2 * math.pi * self.radius, 2))

# circle1 = Circle(4)
# print("Area of circle is: ", circle1.Area(), "cm^2")
# print("Perimeter of circle is: ", circle1.Perimeter(), "cm")

# # Exercise
# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role: ", self.role)
#         print("Department: ", self.dept)
#         print("Salary: ", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age, role, dept, salary):
#         super().__init__(role, dept, salary)
#         self.name = name
#         self.age = age
        

# e1 = Engineer("Rasib", 20, "Software Engineer", "IT", 400000)
# e1.showDetails()

# Exercise
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price

order1 = Order("Football", 1200)
order2 = Order("Tennis ball", 450)
if order1 > order2:
    print(order1.item, " has greater price.")
else:
    print(order2.item, "has greater price.")