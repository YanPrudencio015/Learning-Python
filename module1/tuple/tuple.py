# What is a tuple?

# A tuple is an ordered collection of items, just like a list, but it is immutable.

# Immutable means you cannot change its contents after creation (no adding, removing, or modifying elements).

# Tuples are defined using parentheses ().

my_tuple = (1, 2, 3, 4)
my_tuple = 1, 2, 3 #You can also create a tuple without parentheses (comma defines it):
single = (5,) # Without the comma, Python treats it as a normal integer.



person =("Yan", 24, "Software Engeneer")

print(person[0])# Yan
print(person[1])# 24
print(person[2])# Software Engeneer

# person[1] = 26 
 # ❌ Error! Tuples cannot be modified


points = [(1,2), (3,4), (5,6)]
for x, y in points:
    print(x + y)

# Output:
# 3
# 7
# 11


data = ("Alice", 25, True, [1,2,3]) 
#Immutable for the tuple itself, but mutable objects inside (like the list [1,2,3]) can be changed.



fruits = ("apple", "banana", "cherry")
print(fruits[0]) #apple
print(fruits[2]) #cherry


number = 10,20,30
a = number[0],
b = number[1],
c = number[2],
print(number[0]) #10
print(number[1]) #20
print(number[2]) #30

student = ("alice", (90, 85, 92))

print("student: ", student[1][1])


change = 1,2,3

 # change[1] = 99

print("Test: ", change) #will give error

# 🔹 Why use tuples instead of lists?

# Immutable → safer if you don’t want data to change.

# Faster → tuples are slightly faster than lists.

# Can be used as dictionary keys → lists cannot.

# Semantic meaning → tuple often represents a single record or group of related values (like (x, y) coordinates).

# 💡 Quick analogy:

# List = shopping cart (you add/remove items)

# Tuple = ID card (fixed info, doesn’t change)