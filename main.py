from time import sleep


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't divide by zero"
    return x / y

def getAnswer(input, x, y):
    if input == "add":
        return add(x, y)
    if input == "subtract":
        return subtract(x, y)
    if input == "multiply":
        return multiply(x, y)
    if input == "divide":
        return divide(x, y)

def main():
    print("Input the first number:")
    num1 = float(input())

    print("Input the second number:")
    num2 = float(input())
    
    print("What do you want to do? (add, subtract, multiply, divide)")
    operation = input()

    print(getAnswer(operation, num1, num2))

    sleep(3)

    main()

main()