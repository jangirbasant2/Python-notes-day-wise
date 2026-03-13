# Today we will learn how program makes decission using if else statement in python
# We can use if else statement to make decission in our program.
# The syntax of if else statement is as follows:
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false

# Examples
# 1 if age is greater than or equal to 18, then print "You can vote."
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")

# 2 if age is greater than or equal to 18, then print "You can vote." else print "You cannot vote."
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# 3 using elif statement to check multiple conditions
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("You got A grade.")   
elif marks >= 70:
    print("You got B grade.")
elif marks >= 50:
    print("You got C grade.")
else:
    print("Fail")   

# 4 compaing text using if else statement
command = input("enter command: ")
if command == "hello":
    print("Hello Basant")
# == is used to compare two values, if they are equal then it returns true otherwise it returns false.
# and operator is used to check if both conditions are true, if they are true then it returns true otherwise it returns false.

# Task
# 1 even or odd number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2 login system
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "Basant" and password == "1234":
    print("Login successful")
else:
    print("Access denied")

# 3 largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First number is laarger")
else:
    print("Second number is larger")

# Mini project (First assistant)
command = input("Enter command: ")
if command == "hello":
    print("Hello Basant")
elif command == "how are you?":
    print("I am fine, thank you")
elif command == "Who are you?":
    print("I am your first assistant")
elif command == "Open youtube":
    print("Opening youtube...")
elif command == "exit":
    print("Goodbye!")
else:
    print("Command not recognized")

  

