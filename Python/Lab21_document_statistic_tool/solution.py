def get_document_statistics():
    filename = "document.txt"

    try:
        with open(filename, "r") as file:
            content = file.read()

        lines = content.splitlines()
        line_count = len(lines)
        word_count = len(content.split())
        char_count = len(content)

        return line_count, word_count, char_count

    except FileNotFoundError:
        print("File not found.")
        return 0, 0, 0


def display_document():
    try:
        with open("document.txt", "r") as file:
            content = file.read()

        print("\n===== DOCUMENT CONTENT =====")
        print(content)

    except FileNotFoundError:
        print("File not found.")


while True:
    print("\n===== DOCUMENT STATISTICS ANALYSIS =====")
    print("1. Calculate Document Statistics")
    print("2. Display Document Contents")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        line_count, word_count, char_count = get_document_statistics()

        if line_count == 0 and word_count == 0 and char_count == 0:
            continue

        print("\n===== DOCUMENT REPORT =====")
        print("Target File     : document.txt")
        print("Total Lines     :", line_count)
        print("Total Words     :", word_count)
        print("Total Characters:", char_count)

    elif choice == "2":
        display_document()

    elif choice == "3":
        print("Thank you for using the Document Statistics Analysis Tool. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")