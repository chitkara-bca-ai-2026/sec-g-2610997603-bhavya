def write_note(note):
    with open("notes.txt", "w") as file:
        file.write(note)
    print("Note saved successfully.")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content:
                print("\nYour Note:")
                print(content)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

while True:
    print("\n===== STUDENT NOTES MANAGEMENT SYSTEM =====")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        note = input("Enter your note: ")
        write_note(note)

    elif choice == "2":
        read_notes()

    elif choice == "3":
        print("Thank you for using the Student Notes Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")