import os #to allow clearing the screen for neater user interface & it looks better when the user is interacting with the program

class ShoppingCart:

    def __init__(self):
        self.items = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def add_item(self, item):
        self.items.append(item)
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    def view_cart(self):
        if len(self.items) == 0:
            print("Your cart is empty. :<")
        else:
            print("\n₊⊹Shopping Cart₊⊹")
            print("  ⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹ ")
            print("| No | Item           |")
            print("──────────୨ৎ──────────")

            for i, item in enumerate(self.items, 1): # enumerate() helps number the items in the table
                print(f"| {i:<2} | {item:<14} |")

            print("  ⊹₊˚‧︵‿₊୨ᰔ୧₊‿︵‧˚₊⊹")

    def checkout(self):
        print("Checking out...")
        print("Items bought:", self.items)


cart = ShoppingCart()

while True:
    cart.clear_screen()

    print("=== SHOPPING CART ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        cart.add_item(item)
        input("Press Enter to continue...")

    elif choice == "2":
        item = input("Enter item to remove: ")
        cart.remove_item(item)
        input("Press Enter to continue...")

    elif choice == "3":
        cart.view_cart()
        input("Press Enter to continue...")

    elif choice == "4":
        cart.checkout()
        input("Press Enter to continue...")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
        input("Press Enter to continue...")