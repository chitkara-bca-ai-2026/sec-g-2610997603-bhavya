def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def power(a, b):
    return a ** b

def display_history(history):
    if not history:
        print("No calculation history available.")
    else:
        print("\nCalculation History:")
        for item in history:
            print(item)

history = []

while True:
    print("\n===== UTILITY CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. View Calculation History")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 8:
            print("Exiting calculator...")
            break

        if choice == 7:
            display_history(history)
            continue

        if choice not in range(1, 7):
            print("Invalid choice. Please try again.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            result = add(a, b)
            operation = f"{a} + {b}"

        elif choice == 2:
            result = subtract(a, b)
            operation = f"{a} - {b}"

        elif choice == 3:
            result = multiply(a, b)
            operation = f"{a} * {b}"

        elif choice == 4:
            result = divide(a, b)
            operation = f"{a} / {b}"

        elif choice == 5:
            result = modulus(a, b)
            operation = f"{a} % {b}"

        elif choice == 6:
            result = power(a, b)
            operation = f"{a} ** {b}"

        print("Result:", result)

        history.append(f"{operation} = {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print("Error:", e)