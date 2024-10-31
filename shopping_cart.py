class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item_name, price, quantity=1):
        """Add an item to the cart or update its quantity and price."""
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} {item_name}(s) to the cart.")

    def remove_item(self, item_name, quantity=None):
        """Remove a specified quantity of an item or the item completely from the cart."""
        if item_name in self.cart:
            if quantity is None or quantity >= self.cart[item_name]['quantity']:
                del self.cart[item_name]
                print(f"Removed {item_name} from the cart.")
            else:
                self.cart[item_name]['quantity'] -= quantity
                print(f"Removed {quantity} {item_name}(s) from the cart.")
        else:
            print(f"{item_name} is not in the cart.")

    def view_cart(self):
        """Display the items in the cart."""
        if not self.cart:
            print("The cart is empty.")
        else:
            print("\n--- Shopping Cart ---")
            for item_name, details in self.cart.items():
                print(
                    f"{item_name} - ${details['price']} x {details['quantity']} = ${details['price'] * details['quantity']}")
            print("---------------------")

    def calculate_total(self):
        """Calculate the total cost of items in the cart."""
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        print(f"Total: ${total:.2f}")
        return total


def main():
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Calculate total")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter the item name: ")
            price = float(input(f"Enter the price of {item_name}: "))
            quantity = int(input(f"Enter the quantity of {item_name}: "))
            cart.add_item(item_name, price, quantity)

        elif choice == '2':
            item_name = input("Enter the item name to remove: ")
            quantity = input(f"Enter the quantity to remove (or press Enter to remove all of {item_name}): ")
            quantity = int(quantity) if quantity else None
            cart.remove_item(item_name, quantity)

        elif choice == '3':
            cart.view_cart()

        elif choice == '4':
            cart.calculate_total()

        elif choice == '5':
            print("Exiting the Shopping Cart. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
