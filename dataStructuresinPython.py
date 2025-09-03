from collections import deque

# Data Structures in Python

# 1. List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an item
print("List:", fruits)

# 2. Tuple
coordinates = (10.0, 20.0)
print("Tuple:", coordinates)

# 3. Set
unique_numbers = {1, 2, 3, 2, 1}
unique_numbers.add(4)
print("Set:", unique_numbers)

# 4. Dictionary
student = {
    "name": "Alice",
    "age": 22,
    "courses": ["Math", "Science"]
}
student["age"] = 23  # Update value
print("Dictionary:", student)

# 5. Stack (using list)
stack = []
stack.append(1)
stack.append(2)
print("Stack pop:", stack.pop())

# 6. Queue (using collections.deque)
queue = deque()
queue.append("first")
queue.append("second")
print("Queue popleft:", queue.popleft())

# 7. For Loops (Beginner to Advanced)

# Beginner: Loop through a list
for fruit in fruits:
    print("Fruit:", fruit)

# Intermediate: Loop with index using enumerate
for idx, fruit in enumerate(fruits):
    print(f"Fruit {idx}: {fruit}")

# Advanced: Nested loops
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for item in row:
        print("Matrix item:", item)

# Advanced: List comprehension
squared = [x**2 for x in range(5)]
print("Squared numbers:", squared)

# 8. Functions (Beginner to Advanced)

# Beginner: Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Intermediate: Function with default argument
def power(base, exponent=2):
    return base ** exponent

print("Power:", power(3))
print("Power with exponent:", power(3, 3))

# Advanced: Function with variable arguments
def summarize(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

summarize(1, 2, 3, a=4, b=5)

# Advanced: Lambda function
multiply = lambda x, y: x * y
print("Multiply:", multiply(4, 5))

# Exercise

# Create a list of 5 favorite movies
movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Forrest Gump"]

# Replace the 3rd movie
movies[2] = "Parasite"

# Create a dictionary for yourself
myself = {
    "name": "John",
    "favorite_color": "Blue",
    "hobbies": ["Reading", "Cycling", "Coding"]
}

# Print your name and the second hobby
print("Name:", myself["name"])
print("Second hobby:", myself["hobbies"][1])