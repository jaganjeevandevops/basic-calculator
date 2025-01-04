import argparse

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    parser = argparse.ArgumentParser(description='Perform an arithmetic operation on two numbers.')
    parser.add_argument('operation', type=str, choices=['add', 'subtract', 'multiply', 'divide'],
                        help='The operation to perform.')
    parser.add_argument('num1', type=float, help='First number')
    parser.add_argument('num2', type=float, help='Second number')

    args = parser.parse_args()

    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    result = operations[args.operation](args.num1, args.num2)
    print(f"The result of {args.operation} {args.num1} and {args.num2} is {result}")

if __name__ == '__main__':
    main()
