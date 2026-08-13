# dictionary -> used to stores (key : value) pairs
# They are unordered, mutuable and does not allow duplicate values

std_info = {
    "Name" : "Rasib",
    "CGPA" : 3.57,
    "Dept" : "Software Engineering",
    "Subjects" : ["COAL", "DSA", "SDA", "SRE"]
}

empty_dict = {}

print(type(std_info))
print(std_info)
print(std_info["Subjects"])

std_info["CGPA"] = 3.67
print(std_info["CGPA"])

# Nested dictonaries
std = {
    "Name" : "Rasib", 
    "Subjects" : {
        "Phy" : 54,
        "Chem" : 66
    }
}

print(std)
print(std["Subjects"])
print(std["Subjects"]["Chem"])

# Dictionary methods
print(len(list(std_info.keys()))) #shows the keys in the dictionary
print(list(std_info.values())) #shows the values associated with the keys
print(list(std_info.items())) #shows the keys and items (combined in pairs)
print(std_info.get("Name")) #returns the valued of desired key
std_info.update({"City" : "Multan"}) #used to add new key or dictionary
print(std_info)

# Sets -> Collection of unordered items, cannot be repeated, and are immutable.

collection = {1, 2, "Rasib", 3.57}
print(type(collection))
print(collection)

empty_set = set()
print(empty_set)

# Set Methods

empty_set.add(1) #adds element into the set
print(empty_set)

empty_set.remove(1) #removes element from the set
print(empty_set)

collection.clear() #clears all the values in the set (makes it empty set)
print(collection)

set = {1, 22, 44}
set.pop() #removes a random value from the set
print(set)

set1 = {1, 2, 3}
set2 = {1, 3, 2, 4, 5}

print(set1.union(set2)) #combines both set (does not allow duplication)
print(set1.intersection(set2)) #takes common values from both sets and makes a new set

#exercise

dict = {}
dict.update({"table" : ["a piece of furniture" , "list of facts & figures"]})
dict.update({"cat" : "a small animal"})

print(dict)

#exercise
subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print("Total classroom required : ", len(subjects))

#exercise

dict = {}

subj1 = input("Enter the name of 1st subject: ")
marks1 = int(input("Enter the marks of 1st subject: "))

dict.update({subj1 : marks1})

subj2 = input("Enter the name of 2nd subject: ")
marks2 = int(input("Enter the marks of 2nd subject: "))

dict.update({subj2 : marks2})

subj3 = input("Enter the name of 3rd subject: ")
marks3 = int(input("Enter the marks of 3rd subject: "))

dict.update({subj3 : marks3})

print("Subjects and their marks: ", dict)

#exercise
set = {9, "9.0"}
print(set)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)