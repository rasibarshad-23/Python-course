# list -> It can store values of different data types (It is mutable -> can be altered/changed)

marks = [93.3, 63.4, 87.4, 78.3]
print(marks)
print(type(marks))
print(marks[0], marks[1])
print(len(marks))

student1 = ["Rasib", 20, 84, "Multan"]
print("Details of student1: ")
print("Name:", student1[0])
print("Age:", student1[1])
print("Marks:", student1[2])
print("City:", student1[3])

#list slicing
list = ["This", "is", "a", "list", "."]
print(list)
print(list[:5])

#negative index slicing
print(list[-3:-1])

# list methods
number_list = [1, 2, 3, 4]
number_list.append(-2) #adds one element at the end of the list
print(number_list)

number_list.sort() #arranges/sorts in ascending order
print(number_list)

number_list.sort(reverse= True) #sorts the list in descending order
print(number_list)

number_list.reverse() #reverses the order of the list
print(number_list)

number_list.insert(1, 9) #inserts element at the required index (does not replaces but inserts)
print(number_list)

number_list.remove(3) #removes first occurence of mentioned element
print(number_list)

number_list.pop(2) #removes elements at mentioned index
print(number_list)

# Tuples -> same as lists but it is immutable (cannot be changed/altered)
tuple = (3, 5, 2, 4, 5)
print(type(tuple))
print(tuple)
print(tuple[0])

# Tuple slicing
print(tuple[1:3])
print(tuple[1:])
print(tuple[:len(tuple)])

print(tuple.index(2)) #returns the index of first occurence of element
print(tuple.count(5)) #returns the total occurences of an element in the tuple

# exercise
fav_movies = []

fav_movies.append((input("Enter name of your 1st favourite movies: ")))
fav_movies.append((input("Enter name of your 2nd favourite movies: ")))
fav_movies.append((input("Enter name of your 3rd favourite movies: ")))

print(fav_movies)

#exercise
user_list = []
user_list.append(input("Enter the element of list: "))
user_list.append(input("Enter the element of list: "))
user_list.append(input("Enter the element of list: "))
user_list.append(input("Enter the element of list: "))

copy_list = user_list.copy()
copy_list.reverse()

if(user_list == copy_list):
    print("Palindrome.")
else:
    print("NOT.")

# exercise
Tuple = ("C", "B", "A", "A", "D", "A", "C")
count = Tuple.count("A")
print("No. of students with grade 'A': ", count)

list_std = ["C", "B", "A", "A", "D", "A", "C"]
list_std.sort()
print(list_std)