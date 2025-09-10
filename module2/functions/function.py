def greet():
    print("Hello World, welcome to python")

greet() #Hello World, welcome to python

# def → keyword to define a function
# greet → function name
# () → parentheses (where we put inputs if needed)

def greet_User(name):
    print(f"hello {name}")

greet_User("Yan") #hello Yan

# name is a parameter (input for the function)

# f"Hello, {name}!" → f-string for formatting


# Function with Multiple Parameters
def sum(a,b):
    result = a+ b

    print("The sum is:", result)
sum(5,5) #The sum is:10


# Function that Returns a Value

def multiply(number1,number2):
    return number1 * number2

result_of_Multiply = multiply(15,68)

print(result_of_Multiply) #1020


# Default Parameters

def helloDefault(name = "Guest"):
    print(f"hello {name}")

helloDefault("Alice") # hello Alice
helloDefault() # hello Guest


# Functions with Keyword Arguments

def person_describle(name, age):
    print(f"{name} is {age} years old")

person_describle(age = 35, name = "Juliana") #Juliana is 35 years old


# Funções anônimas (lambda)


function_lampda = lambda x: x ** 2

print("using lampda: ", function_lampda(673)) #using lampda:  452929



def multsum(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total

print("multi args: ", multsum(1,2,3,4,5))
