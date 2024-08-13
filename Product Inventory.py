class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def get_total_value(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Product with ID {product.product_id} already exists. Updating quantity instead.")
            self.update_quantity(product.product_id, product.quantity)
        else:
            self.products[product.product_id] = product
            print(f"Product {product.name} added to inventory.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product ID {product_id} removed from inventory.")
        else:
            print(f"No product found with ID {product_id}.")

    def update_quantity(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
            print(f"Updated quantity for Product ID {product_id}. New Quantity: {self.products[product_id].quantity}")
        else:
            print(f"No product found with ID {product_id}.")

    def inventory_value(self):
        total_value = sum(product.get_total_value() for product in self.products.values())
        return total_value

    def view_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products.values():
                print(product)

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Remove Product")
        print("5. View Total Inventory Value")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                product = Product(product_id, name, price, quantity)
                inventory.add_product(product)
            except ValueError:
                print("Invalid input. Please enter numeric values for ID, price, and quantity.")
        elif choice == '2':
            print("\nCurrent Inventory:")
            inventory.view_inventory()
        elif choice == '3':
            try:
                product_id = int(input("Enter product ID to update quantity: "))
                quantity = int(input("Enter quantity to add: "))
                inventory.update_quantity(product_id, quantity)
            except ValueError:
                print("Invalid input. Please enter numeric values for product ID and quantity.")
        elif choice == '4':
            try:
                product_id = int(input("Enter product ID to remove: "))
                inventory.remove_product(product_id)
            except ValueError:
                print("Invalid input. Please enter a numeric product ID.")
        elif choice == '5':
            total_value = inventory.inventory_value()
            print(f"\nTotal Inventory Value: ${total_value:.2f}")
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()