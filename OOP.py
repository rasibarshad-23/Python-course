# Object Oriented Programming -> involves classes and objects (real-world scenarios)

# Class -> Blueprint of an object
class Student:
# Constuctor (__int__()) -> Automatically called function when object is created
    def __init__(self, name, marks): # self is default paramter of constructor, points to new object
        self.name = name # new variable of name will be created and value in fullname will be assigned to new object
        self.marks = marks
        print("Creating new student in class...")

# Object -> Instance of class
s1 = Student("Rasib", "98") # Can pass argument through constructor
print("Student name: ", s1.name)
print("Marks obtained: ", s1.marks)
s2 = Student("Abdullah", "95")
print("Student name: ", s2.name)
print("Marks obtained: ", s2.marks) 


