# Basic calculator using Python's match-case for operations

num1 = float(input("Enter first number: "))
op = input("Choose operation (+, -, *, /): ").strip()
num2 = float(input("Enter second number: "))

match op:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    case _:
        print("Invalid operator.")