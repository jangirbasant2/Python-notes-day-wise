# What is input?
# Input is a way to get data from the user. 
# It allows us to take input from the user and use it in our program.
# In Python, we can use the input() function to get input from the user.
# The input() function takes a string as an argument, 
# which is the prompt that will be displayed to the user. 
# The user can then enter a value, 
# which will be returned as a string.
# For example, we can use the input() function to get the user's name and age:
 
# This it task one too
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
goal = input("Enter your goal: ")
print("Hello", name)
print("You are", age, "years old")
print("You live in", city)
print("Your goal is to", goal)

# It stores the input in the variables name, age, and city.
# We can convert it to the appropriate data type if needed.
# For example, we can convert age to an integer:

age = int(age)
print("You are", age, "years old")
print("Type of age:", type(age))

# calculate using input
# this is task two
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
substraction = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("Total:", total)
print("Substraction:", substraction)
print("Product:", product)
print("Quotient:", quotient)

# Task three
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

# Chalange for the AI
name = input("Enter your name: ")
print("Hello", name)
print("Nice to meet you", name)
