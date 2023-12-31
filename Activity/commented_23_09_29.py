#Last_Activity

# Define a list of dictionaries, each representing client information and their purchases.
clients = [{'name': 'Tony Stark', 'item_bought': 'Orange', 'price': 1, 'payment_method': 'Debit Card'},
{'name': 'Mary Jane Watson', 'item_bought': 'Bread', 'price': 7, 'payment_method': 'Credit Card'},
{'name': 'Pepper Potts', 'item_bought': 'Eggs', 'price': 10, 'payment_method': 'Debit Card'},
{'name': 'Lois Lane', 'item_bought': 'Banana', 'price': 3, 'payment_method': 'Debit Card'},
{'name': 'Tony Stark', 'item_bought': 'Milk', 'price': 8, 'payment_method': 'Debit Card'},
{'name': 'Thor', 'item_bought': 'Butter', 'price': 1, 'payment_method': 'Credit Card'},
{'name': 'Bruce Wayne', 'item_bought': 'Grape', 'price': 3, 'payment_method': 'Cash'},
{'name': 'Mary Jane Watson', 'item_bought': 'Orange', 'price': 1, 'payment_method': 'Cash'},
{'name': 'Peggy Carter', 'item_bought': 'Sugar', 'price': 6, 'payment_method': 'Credit Card'},
{'name': 'Peggy Carter', 'item_bought': 'Bread', 'price': 3, 'payment_method': 'Debit Card'},
{'name': 'Lois Lane', 'item_bought': 'Coffee', 'price': 5, 'payment_method': 'Credit Card'},
{'name': 'Peter Parker', 'item_bought': 'Pepper', 'price': 1, 'payment_method': 'Cash'},
{'name': 'Peter Parker', 'item_bought': 'Eggs', 'price': 9, 'payment_method': 'Credit Card'},
{'name': 'Lois Lane', 'item_bought': 'Eggs', 'price': 7, 'payment_method': 'Credit Card'}
]
def add_client(name, item_bought, price, payment_method):
    """
    Add a new client's information to a list of clients.

    Parameters:
    - 'name' (str): The name of the client.
    - 'item_bought' (str): The item purchased by the client.
    - 'price' (float): The price of the item.
    - 'payment_method' (str): The method of payment used by the client.

    Returns:
    None

    This function creates a dictionary called 'client' containing the client's
    information and appends it to a list of clients. Each client dictionary
    contains the following keys and values:
    - 'name': The client's name.
    - 'item_bought': The item purchased by the client.
    - 'price': The price of the item.
    - 'payment_method': The method of payment used.

    Example:
    add_client("Karl Akpovi", "Laptop", 1000, "Credit Card")
    """
    client = {
        'name': name,
        'item_bought': item_bought,
        'price': price,
        'payment_method': payment_method
    }
    # Append the 'client' dictionary to a list called 'clients'.
    clients.append(client)

# Call the 'add_client' function four times with different client information.
add_client(name='Tina Turner', item_bought='Banana', price=3, payment_method='Credit Card')
add_client(name='Thérèse Raquin', item_bought='Sugar', price=6, payment_method='Debit Card')
add_client(name='Tony Stark', item_bought='Milk', price=1, payment_method='Cash')
add_client(name='Lois Lane', item_bought='Banana', price=2, payment_method='Cash')

# Print the 'clients' list, which now contains information about all the clients.
print(clients)
# Initialize a variable 'total_revenue' to keep track of the total revenue generated from all clients.
total_revenue = 0

# Iterate through each 'client' in the 'clients' list.
for client in clients:
    # Add the 'price' of the current 'client' to the 'total_revenue'.
    total_revenue += client['price']

# Print the 'total_revenue' to display the total revenue generated.
print(total_revenue)

# Calculate the average purchase amount per client.
# Count the number of distinct clients by extracting their names into a set.
nb_client = len(set(client["name"] for client in clients))

# Calculate the 'average_amount' by dividing the 'total_revenue' by the number of distinct clients.
average_amount = total_revenue / nb_client

# Print the 'average_amount' to display the average purchase amount per client.
print(average_amount)

# Initialize an empty dictionary 'items' to keep track of the count of each item purchased.
items = {}

# Iterate through each 'client' in the 'clients' list.
for client in clients:
    # Extract the 'item_bought' from the current 'client'.
    item_name = client['item_bought']

    # Check if the 'item_name' is already in the 'items' dictionary.
    if item_name in items:
        # If it exists, increment the quantity of the item.
        items[item_name] += 1
    else:
        # If it doesn't exist, initialize it with a count of 1.
        items[item_name] = 1

# Find and print the most popular item purchased by finding the item with the maximum count.
most_popular_item = max(items, key=items.get)
print("Most popular item purchased:", most_popular_item)

# Initialize variables to keep track of the client who spent the most money and their total spending.
most_spending_client = ""
max_spending = 0

## 6 Who is the client that spends the most money?
# Create a dictionary to track the expenses of each customer
customer_expenses = {}

# Iterate through the list of clients
for client in clients:
    name = client['name']
    price = client['price']

    # If the customer already exists in the dictionary, add the price to their expenses
    if name in customer_expenses:
        customer_expenses[name] += price
    else:
        # Otherwise, initialize the customer's expenses
        customer_expenses[name] = price

# Display the expenses of each customer
for customer, expenses in customer_expenses.items():
    print(f"{customer} has spent a total of {expenses} dollars.")
