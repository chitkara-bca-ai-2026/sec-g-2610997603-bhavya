inventory = ["Notebook", "Pen", "Eraser", "Marker"]

while True:
    print("\n" + "=" * 40)
    print("       INVENTORY CONTROL SYSTEM")
    print("=" * 40)

    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n--- Current Inventory ---")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

    elif choice == "2":
        item = input("Enter item name to add: ")
        inventory.append(item)
        print(f"[SUCCESS] '{item}' added to inventory.")

    elif choice == "3":
        item = input("Enter item name to remove: ")
        if item in inventory:
            inventory.remove(item)
            print(f"[SUCCESS] '{item}' removed from inventory.")
        else:
            print("[ERROR] Item not found in inventory.")

    elif choice == "4":
        inventory.sort()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("\n--- Sorted Inventory ---")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

    elif choice == "5":
        print("\nThank you for using the Inventory Control System!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 5.")