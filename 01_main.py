def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    menu = """
Simple Calculator
1) Addition (+)
2) Subtraction (-)
3) Multiplication (*)
4) Division (/)
5) Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
        if choice == '5':
            print("Goodbye!")
            break
        if choice not in {'1','2','3','4'}:
            print("Invalid option. Try again.")
            continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            if choice == '1':
                result = add(a, b)
                op = '+'
            elif choice == '2':
                result = subtract(a, b)
                op = '-'
            elif choice == '3':
                result = multiply(a, b)
                op = '*'
            else:
                result = divide(a, b)
                op = '/'
            print(f"{a} {op} {b} = {result}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
