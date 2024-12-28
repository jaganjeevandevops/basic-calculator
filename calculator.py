# Simple calculator app that can add, subtract, multiply, and divide

def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    while True:
        print("Options:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'exit' to end the program")
        user_input = input(": ")

        if user_input == "exit":
            print("Thank you for using the calculator.")
            break

        # Input validation
        if user_input not in ('add', 'subtract', 'multiply', 'divide'):
            print("Invalid Input")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("The result is", add(num1, num2))
        elif user_input == "subtract":
            print("The result is", subtract(num1, num2))
        elif user_input == "multiply":
            print("The result is", multiply(num1, num2))
        elif user_input == "divide":
            print("The result is", divide(num1, num2))

if __name__ == "__main__":
    main()
