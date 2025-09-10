import myModule

name = myModule.Hello("Yan")
print(name)

result = myModule.Calculate(54, 89)

print(result)



import operations
import utilities

# from anotherpackage import pack1, pack2


result2 = operations.sum(5, 3)
utilities.show_message(f"O resultado da soma é: {result2}")


user_name = utilities.get_user_name()
utilities.show_message(f"Olá, {user_name}!")


# pack1.testing("I am learning python !!!!!")
# pack2.condition(66)


x = 5
y = "3"
z = x + int(y)
print("interestellar: ", z)