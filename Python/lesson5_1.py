import os

user = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_users(user):
    if len(user) == 0:
        print("No users found.")
        return

    print("\n{:<5} {:<15} {:<5}".format("ID", "Name", "Age"))
    print("-" * 27)

    for i, u in enumerate(user, 1):
        print("{:<5} {:<15} {:<5}".format(i, u["name"], u["age"]))

while True:
    clear()

    print(" ｡:˖𓆩˖° ☆ °˖𓆪˖: ｡ ")
    print("MANAGEMENT SYSTEM")
    print(" ｡:˖𓆩˖° ☆ °˖𓆪˖: ｡ ")

    print("\n1. Add user")
    print("2. View users")
    print("3. Update user")
    print("4. Delete user")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        clear()
        name = input("Enter name: ")
        age = input("Enter age: ")
        user.append({"name": name, "age": age})
        print("User added successfully!")
        input("\nPress Enter to continue...")

    elif choice == "2":
        clear()
        display_users(user)
        input("\nPress Enter to continue...")

    elif choice == "3":
        clear()
        display_users(user)

        try:
            index = int(input("\nEnter user ID to update: ")) - 1

            if 0 <= index < len(user):
                name = input("Enter new name: ")
                age = input("Enter new age: ")
                
                user[index]["name"] = name
                user[index]["age"] = age
                print("User updated!")
            else:
                print("Invalid ID.")

        except:
            print("Invalid input.")

        input("\nPress Enter to continue...")

    elif choice == "4":
        clear()
        display_users(user)

        try:
            index = int(input("\nEnter user ID to delete: ")) - 1

            if 0 <= index < len(user):
                user.pop(index)
                print("User deleted!")
            else:
                print("Invalid ID.")

        except:
            print("Invalid input.")

        input("\nPress Enter to continue...")

    elif choice == "5":
        clear()
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
        input("\nPress Enter to continue...")