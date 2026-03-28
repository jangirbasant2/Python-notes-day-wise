# 1 What is list?
# A list is a collection of items that are ordered and changeable. 
# In Python, lists are written with square brackets [] and can contain items of different data types. 
# Lists are one of the most versatile data structures in Python and are commonly used to store and manipulate collections of data.
# 2 Accessing List Elements 
# We can access the elements of a list using their index.
# The index of the first element is 0, the second element is 1, and so on.
# 3 Adding Items to List 
# We can add items to a list using the append() method, which adds an item to the end of the list.
# We can also use the insert() method to add an item at a specific index in the list.
# 4 Removing Items from List
# We can remove items from a list using the remove() method, which removes the first occurrence of the specified item.
# We can also use the pop() method to remove an item at a specific index and return it.
# 5 For Loop with List
# We can use a for loop to iterate over the elements of a list and perform operations on them.
# 6 Using for loop with range() function to iterate over a list by index.
# The range() function generates a sequence of numbers, which can be used to iterate over a list by index.


# Examples
# 1 Creating a list
from click import command


fruits = ["apple", "banana", "cherry"]

# 2 Accessing list elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana  
print(fruits[2])  # Output: cherry

# 3 Adding items to list
task = []
task.append("Learn Python")
task.append("Build an AI Assistant")
print(task)  # Output: ['Learn Python', 'Build an AI Assistant']

# 4 Removing items from list
task.remove("Learn Python")
print(task)  # Output: ['Build an AI Assistant']

# 5 For loop with list
for fruit in fruits:
    print(fruit)

# 6 Using for loop with range() function to iterate over a list by index
for i in range(len(fruits)):
    print(fruits[i])

# 7 Real Example
numbers = [10, 20, 30, 40]
for num in numbers:
    print("Number:", num)



# Task

# Task 1 — Favorite Foods List
food = ["pizza", "burger", "pasta", "sushi", "ice cream"]
for item in food:
    print("I love", item)

# Task 2 — Number List
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print("Number:", num)

# Task 3 — Simple Task Manager With Empty List and asking user for input and using .append() method to add tasks to the list and using for loop to print the tasks. 
tasks = []
while True:
    task = input("Enter a task (or 'done' to finish): ").lower()
    if task == "done":
        break
    tasks.append(task)
for task in tasks:
    print("Task:", task)



# Mini Project: Assistant command list
commands = ["hello", "who are you", "help", "exit"]

while True:

    command = input("Enter command: ").lower()

    if command == "hello":
        print("Hello Basant")

    elif command == "who are you":
        print("I am your Python assistant")

    elif command == "help":
        print("Available commands:")
        
        for cmd in commands:
            print(cmd)

    elif command == "exit":
        print("Goodbye")
        break

    else:
        print("Command not recognized")