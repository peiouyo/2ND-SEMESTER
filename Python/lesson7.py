import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


print("· · ───•⋅⊰ ꥟ ⊱⋅•─── · ·")
print("MONEY WITHDRAWAL SYSTEM")
print("-----------------------")

while True:
    try:
        balance = float(input("Enter your starting balance: "))
        if balance < 0:
            print("Balance cannot be negative.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a number.")


while True:
    clear_screen()

    print("· · ───•⋅⊰ ꥟ ⊱⋅•─── · ·")
    print("MONEY WITHDRAWAL SYSTEM")
    print("-----------------------")

    print("\n1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    try:
        if choice == "1":
            amount = float(input("Enter amount to withdraw: "))

            if amount > balance:
                print("\nInsufficient funds!")

                while True:
                    print("\nOptions:")
                    print("1. Re-enter amount")
                    print("2. Check balance")
                    print("3. Exit")

                    option = input("Choose an option: ")

                    if option == "1":
                        try:
                            amount = float(input("Enter amount to withdraw: "))
                            if amount <= balance:
                                balance -= amount
                                print("Withdrawal successful!")
                                print("Remaining balance:", balance)
                                input("\nPress Enter to continue...")
                                break
                            else:
                                print("Still insufficient funds!")
                        except ValueError:
                            print("Uh Oh! Invalid input! Please enter a number.")

                    elif option == "2":
                        print("Current balance:", balance)
                        input("\nPress Enter to continue...")

                    elif option == "3":
                        print("Exiting program...")
                        exit()

                    else:
                        print("Invalid option.")

            else:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", balance)
                input("\nPress Enter to continue...")

        elif choice == "2":
            print("Current balance:", balance)
            input("\nPress Enter to continue...")

        elif choice == "3":
            print("Thank you! Goodbye.")
            break

        else:
            print("Invalid choice.")
            input("\nPress Enter to continue...")

    except ValueError:
        print("Invalid input! Please enter a number.")
        input("\nPress Enter to continue...")