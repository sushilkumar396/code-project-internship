def calculate(num1, num2, operation):
    """Performs the arithmetic operation based on user choice."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero is undefined."
        return num1 / num2
    else:
        return "Error: Invalid operator choice."

def get_number(prompt):
    """Safely captures and validates float inputs from the user."""
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            return 'exit'
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit'.")

def main():
    print("=== Continuous Terminal Calculator ===")
    print("Type 'exit' at any prompt to close the application.\n")
    
    while True:
        # 1. Safely capture the first number
        num1 = get_number("Enter the first number: ")
        if num1 == 'exit':
            break
            
        # 2. Capture the operation choice
        operation = input("Choose an operation (+, -, *, /): ").strip()
        if operation.lower() == 'exit':
            break
            
        # 3. Safely capture the second number
        num2 = get_number("Enter the second number: ")
        if num2 == 'exit':
            break
            
        # 4. Process the math logic and display the output
        result = calculate(num1, num2, operation)
        
        print("\n------------------------------")
        if isinstance(result, str):
            print(result)
        else:
            print(f"Result: {num1} {operation} {num2} = {result}")
        print("------------------------------\n")

    print("Calculator closed. Have a great day!")

if __name__ == "__main__":
    main()
