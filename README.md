Project title: Online Mall Management System
Author: Shreya Jadhao 
Registration no.: 26BCE10273 
Department: Btech cse core 
Institution: vellore istitute of technology (VIT), bhopal

## Overview

The Online Mall Management System is a Python-based console application that
simulates the basic operations of an online shopping mall.

The system provides two roles: Customer and Owner.

Customers can browse products by category, add products to their cart, remove
products from their cart, view their cart, and complete purchases.

Owners can view the inventory, refill existing products, add new products, and
create new product categories.

The system uses a JSON file to store inventory data so that changes in product
quantities and newly added products/categories are preserved between program
executions.

## Objectives

- To develop a simple online shopping system using Python.
- To implement product and inventory management.
- To provide customers with basic shopping cart and checkout functionality.
- To maintain inventory data using JSON file storage.
- To apply Python programming concepts such as functions, loops, conditional
  statements, lists, dictionaries, and file handling.

## Features

### Customer Features

- Browse product categories
- View available products, prices, and quantities
- Add products to the shopping cart
- View the shopping cart
- Remove products from the shopping cart
- Check product availability
- Checkout and complete a purchase

### Owner Features

- View inventory
- Refill existing products
- Add new products
- Add new product categories
- Update inventory quantities

### Inventory Features

- Products are organized into categories
- Each product has a price and quantity
- Inventory is stored in `inventory.json`
- Inventory is updated after successful purchases
- New products and categories can be added by the owner

## Major Functional Modules

The project contains the following major functional areas:

1. **Inventory Management**
   - Maintains product categories, prices, and quantities.
   - Updates inventory after purchases and refilling.

2. **Customer Shopping**
   - Allows customers to browse products and purchase items.

3. **Shopping Cart**
   - Allows customers to add, view, and remove products.
   - Calculates individual item totals and the overall cart total.

4. **Checkout**
   - Checks stock availability.
   - Updates inventory after a successful purchase.

5. **Owner Management**
   - Allows the owner to view and modify inventory.
   - Allows new products and categories to be added.

6. **Data Storage**
   - Uses JSON file handling to save and load inventory data.

## Technologies Used

- Python
- JSON
- File Handling
- Lists
- Dictionaries
- Functions
- Conditional Statements
- Loops
- String Formatting

## Data Storage

The project uses a JSON file named `inventory.json` to store inventory data.

The inventory contains different categories such as:

- Fruits
- Vegetables
- Dairy

Each product contains:

- Product name
- Price
- Quantity

The inventory is loaded when the program starts and saved whenever changes
are made.

## Input and Output

### Input

The application accepts user input for:

- User role
- Category selection
- Product selection
- Product quantity
- Cart operations
- Checkout confirmation
- Owner inventory operations

### Output

The application displays:

- Available categories
- Available products
- Product prices and quantities
- Shopping cart contents
- Cart total
- Inventory updates
- Purchase confirmation
- Validation and error messages

## System Workflow

1. Start the application.
2. Select a role:
   - Customer
   - Owner
   - Exit
3. Customer can:
   - Browse categories
   - Select products
   - Add products to the cart
   - View or remove products from the cart
   - Checkout
4. Owner can:
   - View inventory
   - Refill products
   - Add new products
   - Add new categories
5. Inventory changes are saved to `inventory.json`.
6. The application continues until the user chooses to exit.

## Installation

1. Install Python 3.
2. Download or clone this repository.
3. Keep the Python file and `inventory.json` in the same folder.
4. Open the project folder in a terminal or Python IDE.

## How to Run

Run the Python program using:

    python <your_python_file_name>.py

Make sure `inventory.json` is present in the same folder.

## Testing

The following operations can be tested:

- Select Customer mode.
- Browse product categories.
- Select a product.
- Add a product to the cart.
- View the cart.
- Remove a product from the cart.
- Attempt to purchase more products than available.
- Complete a purchase.
- Check whether inventory quantity decreases.
- Select Owner mode.
- Refill an existing product.
- Add a new product.
- Add a new category.
- Restart the program and verify that inventory changes are preserved.

## Validation and Error Handling

The application includes validation for:

- Invalid category selection
- Invalid product selection
- Quantity less than or equal to zero
- Insufficient product stock
- Empty shopping cart during checkout
- Duplicate products
- Duplicate categories
- Negative prices and quantities
- Empty category names

## Project Structure

The current project consists of two main files:

    Online-Mall/
    |
    |-- <your_python_file_name>.py
    |
    `-- inventory.json

The Python file contains the application logic, including customer operations,
shopping cart operations, checkout, owner operations, and inventory handling.

The `inventory.json` file provides persistent storage for the inventory.

## Non-Functional Requirements

### Usability
The system provides a simple menu-driven interface that allows users to
select operations through numbered options.

### Reliability
Inventory changes are saved to a JSON file so that updated quantities can
be retained between program executions.

### Maintainability
The application uses separate functions for major operations such as
customer management, cart management, inventory management, and owner
operations.

### Resource Efficiency
The application is a lightweight console-based Python program and uses a
JSON file for local data storage.

## Future Enhancements

Possible future improvements include:

- Graphical user interface
- Customer login and registration
- Customer accounts
- Order history
- Product search
- Product ratings and reviews
- Discount and coupon system
- Multiple payment methods
- Database integration
- Online deployment
