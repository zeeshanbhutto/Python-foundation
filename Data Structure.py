#Lists are ordered collections of items. They are mutable, meaning you can change their contents after creation
my_list = [1, 2, 3, "apple", True]
print(my_list)

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: True

# Modifying elements
my_list[2] = "banana"
print(my_list)

# Adding elements
my_list.append("orange")
print(my_list)

# Removing elements
my_list.remove("apple")
print(my_list)

my_list.insert(3,"papaya")
print(my_list)

#Tuples are similar to lists but are immutable, meaning their contents cannot be changed after creation.

my_tuple = (10, 20, "hello")
print(my_tuple)

# Accessing elements
print(my_tuple[1])  # Output: 20

#Dictionaries store data in key-value pairs. They are unordered and mutable.

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

# Accessing values
print(my_dict["name"])  # Output: Alice

# Adding key-value pairs
my_dict["occupation"] = "data scientist"
print(my_dict)

# Removing key-value pairs
del my_dict["age"]
print(my_dict)

#File handling
# Writing to a file
with open("my_file.txt", "w") as file:
    file.write("Hello, world!")

# Reading from a file
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)


#Exception handling
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Division by zero error!")
except ValueError:
    print("Invalid input. Please enter numbers only.")

#Modules and Packages
#Modules are Python files containing functions and variables. Packages are collections of modules.
import math

print(math.sqrt(16))  # Output: 4.0

import random

print(random.randint(1, 10))  # Generate a random integer between 1 and 10

list=[1,2,"abc","efg",True]
print(list)

list.append("color")
print(list)

list.remove("color")
print(list)

list.insert(1,"blue")
print(list)

list1=["apple","banana","pynaple","stobary","Graps","Mango"]
print(list1[2])
list1.append("kivi")
print(list1)
list1.insert(0,"Applee")
print(list1)
list1.pop()
del list1[-1]#delete and pop are both same logic for deleteing last element from the list
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)#this is how can we sort in descending order
print(list1)
list1.reverse()
print(list1)
a=list1.index("banana")
print(a)
#create a code to find the largest and smallest number in the list
number=[1,2,3,4,5,6,7,8,9]
Max_number=max(number)
Min_number=min(number)
print("Greatest number in the list ", Max_number)
print("smallest number in the list", Min_number)

#Converting List to Tuple and Vice Versa
m_list=[1,2,3,4,5]
m_tuple=tuple(m_list)

#we have a nice practice

#tuple practice
tap=(1,2,"Zeeshan")
print(tap)
#how to access tuple
print(tap[2])
color=("red","green","blue","pink")
b=color.index("red")
print(b)
#dictionary

dict={"name":"zeeshan","Age":"18","Class":"14"}
print(dict)
print(type(dict))
#let see how can we modify dictionary
print(dict["name"])

dict["occupation"]="Data scientist"
print(dict)

dict["name"]= "bhutto"
print(dict)

dic1={"A":"1","B":"2","C":"3"}
dic2={"e":"4","C":"3","F":"5"}
merge_dictionary= dic1 | dic2
print(merge_dictionary)
#Aggregating Data:
#When processing data, intermediate results might be stored in dictionaries.
#Combining these dictionaries can provide a consolidated view of the data.
#Updating Data Structures:
#You might have a base dictionary that needs to be updated with new key-value pairs from another dictionary.

#find the comman elements in two lists
