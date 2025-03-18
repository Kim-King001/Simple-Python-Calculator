def get_user_input():
    """Get user input for two numbers and an operation."""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter the number of your chosen operation: ")
        if choice in ['1', '2', '3', '4']:
            return num1, num2, choice
        else:
            print("Invalid choice. Please choose a valid operation.")

def perform_operation(num1, num2, choice):
    """Perform the chosen mathematical operation."""
    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "Division"
        else:
            return "Error: Division by zero is not allowed."
    
    return f"{operation} result: {num1} {get_symbol(choice)} {num2} = {result}"

def get_symbol(choice):
    """Return the symbol for the chosen operation."""
    symbols = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/'
    }
    return symbols[choice]

def main():
    num1, num2, choice = get_user_input()
    result = perform_operation(num1, num2, choice)
    print(result)

if __name__ == "__main__":
    main()
