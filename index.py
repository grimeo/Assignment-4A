# Assignment 4A
# Redo the programs on assignment2 but now with functions that return multiple values 
# (move all user inputs in one function)

def getInputs():
    global name
    global age
    global address
    
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")


print("Hi, my name is " + name + ". I am "+ age +" years old and I live in " + address +".")