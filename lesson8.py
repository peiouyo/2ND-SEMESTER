import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

filename = "message.txt"

try:
    file = open(filename, "x")
    print("File created successfully!")
    file.close()
except FileExistsError:
    print("✩ Error: File already exists ✩")

while True:
    clear_screen()
    print("╔═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╗")
    print("        WELCOME TO PLLI-CHAT     ")
    print("╚═══*.·:·.☽✧    ✦    ✧☾.·:·.*═══╝")
    print("\n 1. Send Message")
    print(" 2. View Messages")
    print(" 3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        clear_screen()
        message = input("Enter your message: ")
        try:
            with open(filename, "a") as file:
                file.write(message + "\n")
            print("Message sent!ᯓ★")
        except Exception as e:
            print("Error writing to file:", e)
        input("\nPress Enter to continue...")

    elif choice == "2":
        clear_screen()
        try:
            with open(filename, "r") as file:
                content = file.read()
                print(" .𖥔 ݁ ˖ MESSAGES ˖ ݁݁ 𖥔.")
                if content:
                    print(content)
                else:
                    print("No messages yet.")
        except Exception as e:
            print("Error finding file:", e)
        input("\nPress Enter to continue...")

    elif choice == "3":
        clear_screen()
        print("Goodbye!˚⟡˖")
        break

    else:
        print("Invalid choice! Please try again.")
        input("\nPress Enter to continue...")