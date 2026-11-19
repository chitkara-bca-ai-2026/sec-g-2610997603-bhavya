import os

FILE_NAME = "daily_log.txt"

def add_log_entry():
    entry = input("Enter log entry: ")

    with open(FILE_NAME, "a") as file:
        file.write(entry + "\n")

    print("Log entry added successfully.")

def display_complete_log():
    if not os.path.exists(FILE_NAME):
        print("No log entries found.")
        return

    with open(FILE_NAME, "r") as file:
        content = file.read()

    if content:
        print("\n===== DAILY LOG =====")
        print(content)
        print("Total entries:", len(content.strip().splitlines()))
    else:
        print("No log entries found.")

while True:
    print("\n===== OFFICE DAILY LOG BOOK =====")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        add_log_entry()

    elif choice == "2":
        display_complete_log()

    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")