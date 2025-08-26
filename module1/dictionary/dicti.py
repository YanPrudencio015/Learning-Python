# 🔹 What is a dictionary?

# A dictionary is a collection of key-value pairs.

# Each key is unique.

# Each key maps to a value.

# Dictionaries are unordered in Python versions < 3.7, but from Python 3.7+, they preserve insertion order.

# Dictionaries are mutable → you can add, change, or remove items.


person = {"name":"John", "age": "25", "city": "Madrid"}
print(person.keys()) #dict_keys(['name', 'age', 'city'])
print(person.values()) #dict_values(['John', '25', 'Madrid'])
print(person.items()) #([('name', 'John'), ('age', '25'), ('city', 'Madrid')])



students = {
    "Alice": {"age": 25, "grade": 90},
    "Bob": {"age": 22, "grade": 85}
}

print(students["Alice"]["grade"])  # 90



squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



#🔹 Why use dictionaries?

# Fast lookup of values using keys.

# Flexible: values can be any type.

# Great for JSON data, APIs, and configuration.

# Can be nested → useful for complex structures.