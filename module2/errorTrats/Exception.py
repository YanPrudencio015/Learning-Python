def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Error:", e)
        return None

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error: division by zero


# Multiple Exceptions
# want to treat different problems differently:

def read_number(text):
    try:
        return int(text)
    except ValueError:
        print("Error: That is not a number")
    except TypeError:
        print("Error: your must pass a string!")
    
    print(read_number("42")) #42
    print(read_number("abc")) # that is not a number!
    print(read_number(None)) # you must pass a string!



#Custom Exception

class NegativeNumberError(Exception):
    pass


def square_root(x):

    if(x > 0):
        raise NegativeNumberError("Cannot calculate square root of negative number!")
    return x ** 0.5

try:
    print(square_root(16))   # 4.0
    print(square_root(-9))   # Raises our custom exception
except NegativeNumberError as e:
    print("Custom Error: ", e)



# Using finally (cleanup)
#finally runs always, even if there’s an error. Useful for closing files, DB, etc.
def open_file(path):
    try:
        f = open(path, "r")
        data = f.read()
        return data
    except FileNotFoundError:
        print("File not found.")
    finally:
        print("Execution finished (closing resources if needed).")

open_file("not_exist.txt")



# 🔹 5. Raising Your Own Exception Inside a Function

# You can check conditions inside a function and raise errors if invalid input:


def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient funds!")
    return balance - amount

try:
    print(withdraw(100, 50))   # 50
    print(withdraw(100, 200))  # Raises error
except Exception as e:
    print("Bank Error:", e)


# def withdraw(balance, amount):
#     if amount > balance:
#         raise Exception("Insufficient funds!")
#     return balance - amount

# try:
#     print(withdraw(100, 50))   # 50
#     print(withdraw(100, 200))  # Raises error
# except Exception as e:
#     print("Bank Error:", e)
