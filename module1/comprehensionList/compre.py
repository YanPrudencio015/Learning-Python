# [expression for item in iterable if condition]
# expression → what to put in the new list

# item → variable that takes values from the iterable

# condition → optional filter

numbers = [1,2,3,4,5,6,7,8,9]
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)  # [4, 16, 36, 64]



evens = [x for x in range(10) if x % 2== 0]
print(evens) #[0, 2, 4, 6, 8]

words = ["apple", "boy", "work"]

upper_Words = [x.upper() for x in words]

print(upper_Words) #['APPLE', 'BOY', 'WORK']



labels =["even" if x %2 == 0 else "odd" for x in range(5)]

print(labels) #['even', 'odd', 'even', 'odd', 'even']