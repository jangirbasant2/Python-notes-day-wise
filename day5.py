# loop repeats a block of code until a certain condition is met. There are two types of loops in python, for loop and while loop.
# For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. The syntax of for loop is as follows:
#for condition:
#    code to execute if condition is true
# While loop is used to execute a block of code as long as a certain condition is true. The syntax of while loop is as follows:
#while condition:
#    code to execute if condition is true



# Examples
# 1 counting from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1


# 2 infinite loop
while True:
    print("Hello")
    break


# 3 break statement
while True:
    command = input("Enter command: ")

    if command == "exit":
        print("Goodbye")
        break


# 4 First real assistant loop
while True:

    command = input("Enter command: ").lower()

    if command == "hello":
        print("Hello Basant")

    elif command == "who are you":
        print("I am your assistant")

    elif command == "exit":
        print("Goodbye")
        break

    else:
        print("Command not recognized")


# 5 counting example
count = 1
while count <= 10:
    print("Number: ", count)
    count += 1



# Task
# 1 counting from 1 to 100
count = 1
while count <= 100:
    print(count)
    count += 1


# 2 password system
while True:
    password = input("Enter password: ")
    if password == "rvt@1234":
        print("Access granted")
        break
    else:
        print("Access denied")
 


# 3 Number guessing game
number = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Sorry, that's not the correct number. Try again.")


# Mini project - Assistant v2
while True:
    command = input("Enter command: ").lower()

    if command == "hello":
        print("Hello Basant")

    elif command == "who are you":
        print("I am your assistant")

    elif command == "open youtube":
        print("Opening youtube...")

    elif command == "help":
        print("I can help you with the following commands:")
        print("1. hello - Greet the assistant")
        print("2. who are you - Get information about the assistant")
        print("3. open youtube - Open youtube in your browser")
        print("4. help - Show available commands")
        print("5. exit - Exit the assistant")
        
    elif command == "exit":
        print("Goodbye")
        break

    else:
        print("Command not recognized")



