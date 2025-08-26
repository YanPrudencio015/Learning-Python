frutas = ["maçã", "limão", "jamelão"]

for fruta in frutas:
    print(fruta)
    # maçã
    # limão        
    # jamelão 

contador = 0
while contador <= 5: 
    print("contador: ", contador) 
    contador +=1
    # contador:  0 
    # contador:  1 
    # contador:  2 
    # contador:  3 
    # contador:  4 
    # contador:  5 


contador2 = 0

while True:
    print("contador2: ", contador2)
    contador2 +=1
    # contador2:  0
    # contador2:  1
    # contador2:  2
    # contador2:  3
    # contador2:  4

    if contador2 == 5: break

    # Using Continue
    # 'continue' skips the rest of the code in the current iteration
    # and moves directly to the next loop cycle.
for i in range(10):

    if i % 2 == 0:
        continue
    print("continue example 1:", i)
    # continue example 1: 1
    # continue example 1: 3
    # continue example 1: 5
    # continue example 1: 7
    # continue example 1: 9

for i in range(1, 6):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)

    # Output:
    # 1
    # 3
    # 5


# 'pass' does nothing; it is used as a placeholder
# to avoid syntax errors when code is required but not written yet.

def my_function():
    pass  # function not implemented yet


for i in range(5):
    pass  # later we will add logic here


class Animal:
    pass  # class definition will be added later


x = 10
if x > 5:
    pass  # we know something must happen here, but not now
else:
    print("x is 5 or less")
