# 🧮 Basic Calculator in Python (Using `match-case`)

This is a simple command-line calculator built using Python's `match-case` (introduced in Python 3.10). It supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## 🚀 Features

- Supports four basic operations: `+`, `-`, `*`, `/`
- Validates division by zero
- Uses Python's modern `match-case` syntax for clean and readable code

## 🛠️ Requirements

- Python 3.10 or above

## 📦 Usage

Run the script using a Python interpreter:

```bash
python main.py
```

### Example

```text
Enter first number: 10
Choose operation (+, -, *, /): *
Enter second number: 5
Result: 50.0
```

## 📄 Code Overview

```python
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
```

## 📌 Notes

- The `match-case` construct is similar to `switch-case` in other languages and improves readability.
- Division by zero is handled gracefully.

## 📚 License

This project is open-source and free to use.
