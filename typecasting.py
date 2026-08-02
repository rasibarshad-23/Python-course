#typecasting in Python (converting variables from one data type to another)

name = "Rasib Arshad" 
age = 20
cgpa = 3.61
is_student = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

age = float(age)
print(age)

cgpa = int(cgpa)
print(cgpa)

age = str(age)
age += "1"
print(age)


name = bool(name)
print(name)

bool = int(is_student)
print(is_student)

#practice 

age1 = 20.9
integer_age = int(age1)
print(integer_age)