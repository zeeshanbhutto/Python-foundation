# control structures
fruits = ["apple", "banana", "cherry"]
for fruit in fruits: # for each fruit in the list of fruits
    print(fruit)


for fruit in fruits: # for each fruit in the list of fruits
    x = fruit + " pie"
    print(x)

print("done")

# for loop
for i in range(10):
    print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i = i + 1

# if statement
if (5 > 2):
    print("Five is greater than two!")

# if-else statement
if (5 > 2):
    print("Five is greater than two!")
else:
    print("Five is not greater than two!")

# if-elif-else statement
if (5 > 2):
    print("Five is greater than two!")
elif (5 == 2):
    print("Five is equal to two!")
else:
    print("Five is not greater than two!")

def greet(name):
    print("Hello,", name)

greet("Bob")

def add(x, y):
    return x + y

result = add(3, 4)
print(result)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "says Woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()

#Write a Python program to check if a number is even or odd.
#Create a function to calculate the factorial of a number.
#Design a class to represent a car with attributes like color, make, and model, and methods like start and stop.

number = int(input("Enter your number:- "))
if number %2 == 0:
    print("this is even number")
else:
    print("this is a odd number")




def factorial(n):
    """Calculate the factor of the non negative integer"""
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    #get user input:-

num = int(input("Enter a non negstive integer:- "))
result=factorial(num)

print("The factorial of ",num,"is",result,)

class car:
    def __init__(self,color,make,model):
        self.color = color
        self.make = make
        self.model = model
        self.is_started = False

   # self.is_started = False initializes a flag to track the car's starting state.
    def start(self):
        if not self.is_started:
            print("Car started")
            self.is_started = True
        else:
            print("Car is already started")

    def stop(self):
        if not self.is_started:
            print("Car stops")
            self.is_started = True
        else:
            print("Car is already stops")


# Create a car object
my_car = car("Black", "Toyata", "Camry")
# Start the car
my_car.start()
# Stop the car
my_car.stop()
