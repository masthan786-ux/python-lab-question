Python

inventory = {
    "Laptop": {"price": 50000, "quantity": 10},
    "Mouse": {"price": 500, "quantity": 3},
    "Keyboard": {"price": 1000, "quantity": 7},
    "Monitor": {"price": 12000, "quantity": 4}
}

# Add a new product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    if name in inventory:
        print("Product already exists!")
    else:
        inventory[name] = {
            "price": price,
            "quantity": quantity
        }
        print("Product added successfully!")

# Update product quantity
def update_quantity():
    name = input("Enter product name: ")

    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name]["quantity"] = quantity
        print("Quantity updated successfully!")
    else:
        print("Product not found!")

# Search for a product
def search_product():
    name = input("Enter product name: ")

    if name in inventory:
        print(name, ":", inventory[name])
    else:
        print("Product not found!")

# Calculate total inventory value
def total_value():
    total = sum(
        item["price"] * item["quantity"]
        for item in inventory.values()
    )
    print("Total inventory value: Rs.", total)

# Display products with quantity below 5
def low_stock():
    print("Products with quantity below 5:")
    for name, item in inventory.items():
        if item["quantity"] < 5:
            print(name, item)

# Display products sorted by name
def sort_products():
    print("Products sorted by name:")
    for name in sorted(inventory):
        print(name, inventory[name])

# Main menu
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Total Inventory Value")
    print("5. Display Low Stock")
    print("6. Sort Products by Name")
    print("7. Display All Products")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        search_product()
    elif choice == "4":
        total_value()
    elif choice == "5":
        low_stock()
    elif choice == "6":
        sort_products()
    elif choice == "7":
        for name, item in inventory.items():
            print(name, item)
    elif choice == "8":
        print("Exiting Inventory Management System.")
        break
    else:
        print("Invalid choice! Try again.")
