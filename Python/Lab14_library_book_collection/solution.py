books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2022", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {"Programming", "AI", "Software Engineering"}

student_wishlist = {
    "AI",
    "Cloud Computing",
    "Cybersecurity",
    "Machine Learning",
    "Robotics"
}

while True:
    print("\n" + "=" * 60)
    print("           LIBRARY BOOK & CATEGORY MANAGER")
    print("=" * 60)
    print("Select an operation:")
    print("1. View Catalogued Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\n=== Current Library Catalog (Fixed Records) ===")
        for i, (title, author, year, category) in enumerate(books, 1):
            print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')
        print(f"Total Books: {len(books)}")

    elif choice == "2":
        print("\n=== Add New Book Record ===")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        if title and author and year and category:
            new_book = (title, author, year, category)
            books.append(new_book)
            library_categories.add(category)

            print(f'\n[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')
        else:
            print("[ERROR] All fields are required.")

    elif choice == "3":
        print("\n=== Unique Categories Available in Library (Set) ===")
        for category in sorted(library_categories):
            print(f"- {category}")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == "4":
        print("\n=== Add to Student Wishlist ===")
        category = input("Enter requested category: ")

        if category:
            student_wishlist.add(category)
            print(f'[SUCCESS] "{category}" added to student wishlist.')
        else:
            print("[ERROR] Category cannot be empty.")

    elif choice == "5":
        print("\n" + "=" * 60)
        print("                  CATEGORY GAP ANALYSIS")
        print("=" * 60)

        print(f"Library Holdings (Set): {sorted(library_categories)}")
        print(f"Student Wishlist (Set): {sorted(student_wishlist)}")
        print("-" * 60)

        intersection = library_categories.intersection(student_wishlist)
        difference = student_wishlist.difference(library_categories)
        union = library_categories.union(student_wishlist)

        print("\n1. Already in Stock (Intersection ∩):")
        print(sorted(intersection))

        print("\n2. Purchase Order Needed (Difference -):")
        print(sorted(difference))

        print("\n3. Full Combined Genre Coverage (Union ∪):")
        print(sorted(union))

        print("=" * 60)

    elif choice == "6":
        print("\nThank you for using the Library Manager. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 6.")