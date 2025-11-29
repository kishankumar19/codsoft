def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def modulus(a, b):
    """Return the remainder of two numbers."""
    if b == 0:
        raise ValueError("Cannot perform modulus by zero!")
    return a % b

def power(a, b):
    """Return the result of a raised to the power of b."""
    return a ** b

def calculator_menu():
    """Display menu"""
    print("\n==============================")
    print("      Python Calculator       ")
    print("==============================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Exit")
    print("==============================")

def main():
    """Main function to control the calculator flow."""
    while True:
        calculator_menu()

        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print(" Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 7:
            print("\nThank you for using the calculator. Goodbye! ")
            break

        if choice not in range(1, 7):
            print(" Invalid choice! Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
            elif choice == 5:
                result = modulus(num1, num2)
            elif choice == 6:
                result = power(num1, num2)

            print(f"\n✅ Result: {result}")

        except ValueError as e:
            print(f" Error: {e}")
        except Exception as e:
            print(f" Unexpected Error: {e}")

        input("\nPress Enter to continue...")
        
if __name__ == "__main__":
    main()
