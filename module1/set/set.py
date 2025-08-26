# What is a set?

# A set is an unordered collection of unique elements.

# No duplicates → all elements are unique.

# Unordered → you cannot access elements by index.

# Sets are mutable (you can add/remove items).

# There’s also frozenset → immutable version of a set.



fruits = {"orange", "Apple", "cherry"}
numbers = set([1,2,3,4,5,6])

sets1 = {1,2,3}
sets2 = {4,5,6}

union =sets1 | sets2

print(union) #{1, 2, 3, 4, 5, 6}

intersection = sets1 & sets2

print("test: ", intersection) #set()

difference = sets1 - sets2
print(difference) #{1, 2, 3}

difference_simetric = sets1 ^ sets2
print(difference_simetric) #{1, 2, 3, 4, 5, 6}






frutas = {"apple", "banana", "orange"}


frutas.add("cherry")
print(frutas)  # {'banana', 'orange', 'cherry', 'apple'}


frutas.remove("banana")
print(frutas)  # {'orange', 'cherry', 'apple'}


frutas.discard("grape")
print(frutas)  # {'orange', 'cherry', 'apple'}


frutas.clear()
print(frutas)  # set()