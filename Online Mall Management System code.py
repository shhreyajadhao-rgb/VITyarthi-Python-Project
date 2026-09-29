import json
# ================= INVENTORY =================

initial_inventory = {
    "fruits": {
        "apple": {"price": 10, "qty": 50},
        "banana": {"price": 5, "qty": 100},
        "strawberry": {"price": 20, "qty": 30},
        "grapes": {"price": 30, "qty": 40},
        "mango": {"price": 25, "qty": 20},
        "watermelon": {"price": 80, "qty": 10}
    },

    "vegetables": {
        "carrot": {"price": 8, "qty": 60},
        "spinach": {"price": 12, "qty": 40},
        "tomato": {"price": 15, "qty": 70},
        "potato": {"price": 20, "qty": 60},
        "onion": {"price": 18, "qty": 70},
        "cabbage": {"price": 22, "qty": 50}
    },

    "dairy": {
        "milk": {"price": 25, "qty": 30},
        "cheese": {"price": 50, "qty": 20},
        "yogurt": {"price": 30, "qty": 25},
        "butter": {"price": 40, "qty": 15},
        "cream": {"price": 35, "qty": 10},
        "ice cream": {"price": 60, "qty": 5}
    }
}

# ================= JSON FUNCTIONS =================

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

# Create inventory.json if it does not exist
file = open("inventory.json", "a")
file.close()

with open("inventory.json", "r") as file:
    data = file.read()

if data == "":
    inventory = initial_inventory.copy()
    save_inventory(inventory)

else:
    with open("inventory.json", "r") as file:
        inventory = json.load(file)

    # Add missing categories and items
    for category, items in initial_inventory.items():

        if category not in inventory:
            inventory[category] = items

        else:
            for item, details in items.items():

                if item not in inventory[category]:
                    inventory[category][item] = details

    save_inventory(inventory)

# ================= DISPLAY FUNCTIONS =================

def show_categories(inventory):
    print("\nAvailable Categories:")

    for i, category in enumerate(inventory, 1):
        print(f"{i}. {category.title()}")

def choose_category(inventory):
    categories = list(inventory.keys())
    show_categories(inventory)

    choice = int(input("Enter category number: "))

    if 1 <= choice <= len(categories):
        return categories[choice - 1]

    else:
        print("Invalid category number.")
        return None

def show_items(items):
    print("\nItems:")

    for name, details in items.items():
        print(
            f"- {name.title()}: "
            f"₹{details['price']} | Qty: {details['qty']}"
        )

# ================= CART FUNCTIONS =================

def show_cart(cart):
    print("\n========== YOUR CART ==========")

    if len(cart) == 0:
        print("Your cart is empty.")
        return

    total = 0

    for item in cart:
        item_total = item["price"] * item["qty"]

        print(
            f"{item['name'].title()} | "
            f"Qty: {item['qty']} | "
            f"Price: ₹{item['price']} | "
            f"Total: ₹{item_total}"
        )

        total += item_total

    print("-------------------------------")
    print(f"Cart Total: ₹{total}")

def add_to_cart(cart, category, name, price, quantity):
    cart.append({
        "category": category,
        "name": name,
        "price": price,
        "qty": quantity
    })

    print(f"\n{quantity} {name}(s) added to cart.")

def remove_from_cart(cart):
    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    show_cart(cart)

    name = input("\nEnter item to remove: ").lower()

    for item in cart:

        if item["name"] == name:

            quantity = int(
                input("Enter quantity to remove: ")
            )

            if quantity >= item["qty"]:
                cart.remove(item)
                print(f"{name.title()} removed from cart.")

            else:
                item["qty"] -= quantity
                print(
                    f"{quantity} {name}(s) removed from cart."
                )

            return

    print("Item not found in cart.")

# ================= CUSTOMER =================

def customer_menu(inventory):
    cart = []

    while True:

        print("\n========== CUSTOMER MENU ==========")
        print("1. Browse categories")
        print("2. View cart")
        print("3. Remove from cart")
        print("4. Checkout")
        print("5. Return to Main Menu")

        choice = input("Enter your choice: ")

        # Browse categories
        if choice == "1":

            category = choose_category(inventory)

            if category:

                show_items(inventory[category])

                name = input(
                    "\nEnter item name to buy: "
                ).lower()

                if name not in inventory[category]:
                    print("Item not found.")
                    continue

                quantity = int(
                    input("Enter quantity: ")
                )

                available = inventory[category][name]["qty"]

                if quantity <= 0:
                    print("Quantity must be greater than 0.")

                elif quantity > available:
                    print(
                        f"Not enough stock. "
                        f"Only {available} available."
                    )

                else:

                    price = inventory[category][name]["price"]

                    add_to_cart(
                        cart,
                        category,
                        name,
                        price,
                        quantity
                    )

        # View cart
        elif choice == "2":
            show_cart(cart)

        # Remove from cart
        elif choice == "3":
            remove_from_cart(cart)

        # Checkout
        elif choice == "4":

            if len(cart) == 0:
                print("\nYour cart is empty.")
                continue

            show_cart(cart)

            confirm = input(
                "\nDo you want to checkout? (y/n): "
            ).lower()

            if confirm != "y":
                continue

            enough_stock = True

            # Check stock again
            for item in cart:

                available = inventory[
                    item["category"]
                ][item["name"]]["qty"]

                if item["qty"] > available:

                    enough_stock = False

                    print(
                        f"Not enough {item['name']} in stock."
                    )

            if enough_stock:

                # Subtract purchased quantity
                for item in cart:

                    inventory[
                        item["category"]
                    ][item["name"]]["qty"] -= item["qty"]

                save_inventory(inventory)
                cart.clear()

                print("\nPurchase successful!")

                break

        # Return to main menu
        elif choice == "5":

            print("\nReturning to main menu...")
            break

        else:
            print("Invalid choice.")

# ================= OWNER =================

def refill_item(inventory):

    category = choose_category(inventory)

    if not category:
        return

    show_items(inventory[category])

    name = input(
        "\nEnter item name to refill: "
    ).lower()

    if name not in inventory[category]:
        print("Item not found.")
        return

    quantity = int(
        input("Enter quantity to add: ")
    )

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    inventory[category][name]["qty"] += quantity

    save_inventory(inventory)

    print(
        f"Updated {name} quantity to "
        f"{inventory[category][name]['qty']}"
    )

def add_new_item(inventory):

    category = choose_category(inventory)

    if not category:
        return

    name = input(
        "Enter new item name: "
    ).lower()

    if name in inventory[category]:
        print("Item already exists.")
        return

    price = float(
        input("Enter price: ")
    )

    quantity = int(
        input("Enter starting quantity: ")
    )

    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return

    inventory[category][name] = {
        "price": price,
        "qty": quantity
    }

    save_inventory(inventory)

    print(
        f"Added {name} to {category}."
    )

def add_new_category(inventory):

    category = input(
        "Enter new category name: "
    ).strip().lower()

    if category == "":
        print("Category name cannot be empty.")
        return

    if category in inventory:
        print("Category already exists.")
        return

    inventory[category] = {}

    save_inventory(inventory)

    print(
        f"Category '{category}' added successfully."
    )

def owner_menu(inventory):

    while True:

        print("\n========== OWNER MENU ==========")
        print("1. View inventory")
        print("2. Refill existing item")
        print("3. Add new item")
        print("4. Add new category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            category = choose_category(inventory)

            if category:
                show_items(inventory[category])

        elif choice == "2":
            refill_item(inventory)

        elif choice == "3":
            add_new_item(inventory)

        elif choice == "4":
            add_new_category(inventory)

        elif choice == "5":

            print("\nReturning to main menu...")
            break

        else:
            print("Invalid choice.")

# ================= MAIN =================

def main():

    while True:

        print("\n================================")
        print("       WELCOME TO ONLINE MALL")
        print("================================")

        print("1. Customer")
        print("2. Owner")
        print("3. Exit")

        role = input("Choose your role: ")

        if role == "1":
            customer_menu(inventory)

        elif role == "2":
            owner_menu(inventory)

        elif role == "3":

            print("\nThank you for using Online Mall!")
            break

        else:
            print("Invalid choice.")
main()
