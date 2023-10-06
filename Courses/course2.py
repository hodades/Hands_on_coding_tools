# -*- coding: utf-8 -*-
"""course2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ou_Amc2hpUvwwv7zk7OZuYfcCMURlR3B

Explanation of concepts: In this section, we have covered the following concepts:

The creation of a Boolean function defining the is_even() function.

This function is a Boolean function and returns true or false values if even or odd.
List to create a list of different elements called "items." It is created with [].

Methods are functions that apply to lists with the type (list). Unlike user-defined functions, methods modify and completely change the list.

The condition statement: it allows for creating specific conditions to perform an action, and here we use the keywords: if, elif, else.

A 'FOR' loop.

List comprehension (List Comprehension).

# Boolean

The creation of a Boolean function defining the is_even() function. This function is a Boolean function and returns true or false values if even or odd.
"""

def is_even(num):
    """
    Checks if a number is even.

    This function takes an input number `num` and returns True if the number is even, otherwise False.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    # "%" represents the remainder of a division
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result

# Usage examples
print(is_even(2))
# Expected result: True

print(is_even(3))
# Expected result: False

"""# List
the list are composed of different elements called items
"""

"""
This Python script includes examples and explanations of how to use lists in Python.
"""
# Create an empty list
l = []
# or
l = list()

# The type is a list
type([1, 2, 3, 4, 7])

# Assign l to a list
l = [1, 2, 3, 4, 7, 5]

# Check what the first value of l is
l[0]

# Let's change the third value to 1
l[2] = 1
l

# Observe the value of the last element
l[-1]

# Observe all elements before the last one
l[:-1]
l[0:-1]  # Galaad

# Observe all elements from the third position to the end
l[2:]

# Reverse the order of list l
l[::-1]

# Take the first 2 elements and reverse the order
l[0:2][::-1]
l[0:2:-1]  # Doesn't work as it first reverses the list
l[0:2:-1]

# Slice the list. Work only on the sublist from the first to the third position
l[0:2]  # From position 1 to position 2
l[0:3]  # From position 1 to position 3
[l[0], l[3]]  # Take only the values from position 1 and position 4

# Create a list with booleans, integers, decimals, and strings
new_list = [True, 1, 2.5, "abc"]
new_list

# Create a list of lists
even_odd_list = [1, 3, 5, 7, 2, 4, 6]
even_odd_list = [[1, 3, 5, 7], [2, 4, 6]]
# Retrieve the second element of the second list
even_odd_list[1][1]

new_list = [[1, 3, 5, 7], [2, 4, [1, 3, 5, 7], [2, 4, 6], 6], [2, 4, 6]]

"""
This Python script includes examples and explanations of how to use lists in Python.
"""

# Create a list
l = [1, 2, 3, 4, 7]

# Create a new list `new_l` by extracting elements from position 2 to the beginning of the list,
# with a reverse order.
new_l = l[2::-1]

# Print the new list
print(new_l)

"""
This Python script contains information about different areas of a house, along with their dimensions.
"""

# Dimensions of each area in the house
hall = 11.25  # Dimensions of the hallway in square meters
kit = 18.0  # Dimensions of the kitchen in square meters
liv = 20.0  # Dimensions of the living room in square meters
bed = 10.75  # Dimensions of the bedroom in square meters
bath = 9.50  # Dimensions of the bathroom in square meters

# List containing the names of the areas and their dimensions
areas = ["hallway", hall, "kitchen", kit, "living room", liv,
         "bedroom", bed, "bathroom", bath]

# Selecting the last 4 elements of the list (areas in the house)
areas[-4:]

# Selecting all elements of the list except the last 2 (names of the areas and their dimensions)
areas[:-2]

"""## Methods
Methods are functions that apply to lists with the type (list). Unlike user-defined functions, methods modify and completely change the list.


"""

"""

This Python script demonstrates the use of list methods to add, remove elements, and find the index of an element.
"""

# Create a new list `new_list2` containing elements
new_list2 = [1, 2, "e"]
print(new_list2)

# Add the element "Hello" to the list
new_list2.append("Hello")
print(new_list2)

# Remove the last added element from the list
new_list2.pop()
print(new_list2)

# Use the `index` method to find the position of the element "e" in the list
position_e = new_list2.index("e")
print("The position of 'e' in the list is:", position_e)

# To remove a specific element, let's remove the number 1 from the list
new_list2.remove(1)
print(new_list2)

"""#Conditional structures
With more than two options.

Conditional control structures (or simply conditions) allow us to execute different blocks of code depending on whether a specific condition is met or not.

We often use conditions with variables: based on the value stored in a variable, we want to execute one block of code rather than another.

Python provides us with the following conditional structures:

The if condition ("if");
The if...else condition ("if...else");
The if...elif...else condition ("if...else if... else").
"""

def calculate_room_area(room_name):
    """
    This function calculates the area of a room based on its name.

    Args:
        room_name (str): The name of the room (in lowercase).

    Returns:
        float or str: The area of the room if the name is valid, otherwise an error message.
    """

    # Using the if-elif-else control structure to determine the area based on the room name
    if room_name == "hallway":
        res = hall
    elif room_name == "kitchen":
        res = kit
    elif room_name == "living room":
        res = liv
    elif room_name == "bathroom":
        res = bath
    elif room_name == "bedroom":
        res = bed
    else:
        res = "Please try again with a valid room name"

    return res

# Examples of using the calculate_room_area function
print(calculate_room_area("bedroom"))
# Expected result: the area of the bedroom
print(calculate_room_area("BEDROOM"))
# Expected result: an error message

"""# The FOR Loop
The `for` loop is a control structure in programming that allows you to iterate (loop) over a collection of elements, such as a list, tuple, string, etc. It is commonly used to perform a repeated operation on each item within that collection. Here's a concise explanation of its usage:

1. **Iterating over a Sequence**: The `for` loop is primarily used for iterating over a sequence of elements. For example, a list of integers `[1, 2, 3, 4, 5]` or a string `"Python"`.

2. **Basic Syntax**: The basic syntax of a `for` loop in Python is as follows:

   ```python
   for element in sequence:
       # Code to be executed for each element
   ```

   - `element` is a temporary variable that takes on the value of each element in the sequence during each iteration.
   - `sequence` is the sequence you're iterating over, such as a list.

3. **Repeated Execution**: The code inside the `for` loop is executed for each element of the sequence. This allows you to perform operations on each element without manually repeating the code.

4. **Using `range`**: The `range` function is often used to generate a sequence of integers to iterate over. For example, `for i in range(5)` will iterate from 0 to 4 (inclusive).

5. **Manipulating Indices**: Sometimes, you may need to access the position (index) of each element within the sequence. You can use the `enumerate` function for that. For example:

   ```python
   for index, element in enumerate(sequence):
       # index contains the position of the element in the sequence
       # element contains the value of the element
   ```

6. **Early Exit**: You can use the `break` statement to exit the loop prematurely if a certain condition is met.

The `for` loop is a powerful tool for automating repetitive tasks and efficiently processing large amounts of data in programming. It is widely used for traversing lists, dictionaries, files, and many other types of data.
"""

"""
This Python script calculates the area of a room based on its name using a predefined list of room names.
"""

# List of room names
areas_name = ["hallway", "kitchen", "living room", "bedroom", "bathroom"]

def calculate_room_area(room_name):
    """
    Calculates the area of a room based on its name.

    Args:
        room_name (str): The name of the room (in lowercase).

    Returns:
        float or str: The area of the room if the name is valid, otherwise an error message.
    """

    # Convert the room name to lowercase to avoid case issues
    room_name = room_name.lower()

    # Using the if-elif-else control structure to determine the area based on the room name
    if room_name == "hallway":
        result = hall
    elif room_name == "kitchen":
        result = kit
    elif room_name == "living room":
        result = liv
    elif room_name == "bathroom":
        result = bath
    elif room_name == "bedroom":
        result = bed
    else:
        result = "Please try again with a valid room name"

    return result

# Calling the calculate_room_area function with different room names
calculate_room_area("hall")
calculate_room_area("kit")
calculate_room_area("liv")

# Using a for loop to calculate the area of all rooms in the areas_name list
for i in range(len(areas_name)):
    print(calculate_room_area(areas_name[i]))

"""## List Comprehension

List comprehension is a syntactic construct in Python that allows you to create lists in a concise and elegant way using a single line of code. It is commonly used to apply an operation to each element of a sequence (such as a list) and generate a new list based on the results of that operation. Here's a definition and a concise example:

**Definition:**

List comprehension is a concise way to create a new list in Python by applying an expression to each element of an existing sequence (like a list, tuple, etc.).

**Basic Syntax:**

The basic syntax of list comprehension is as follows:

```python
new_list = [expression for element in original_sequence]
```

- `new_list` is the new list you are creating.
- `expression` is the operation you want to perform on each element of the sequence.
- `element` is a temporary variable that takes on the value of each element in the original sequence.
- `original_sequence` is the sequence you are iterating over.

**Example of Usage:**

Suppose we have a list of numbers, and we want to create a new list that contains the square of each number. Here's how it can be done with list comprehension:

```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
```

In this example, `squares` will be equal to `[1, 4, 9, 16, 25]`, because the expression `x**2` is applied to each element `x` in the `numbers` list.

List comprehension is appreciated for its simplicity and readability, and it is often used to perform filtering, transformation, or data generation operations efficiently in Python. It helps avoid writing explicit `for` loops for simple tasks..
"""

'''
This Python script illustrates the use of list comprehension to create a new list containing the squares of numbers.
'''

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use list comprehension to create a new list containing the squares of the numbers
squares = [x**2 for x in numbers]

# Print the resulting list
print(squares)
# Expected result: [1, 4, 9, 16, 25]

"""
This Python script demonstrates the use of different operations on a list of room areas.
"""

# Create a list of room areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Add two new areas to the list
areas.append(24.5)
areas.append(15.45)

# Print the list of areas (including the additions)
print(areas)
# Expected result: [11.25, 18.0, 20.0, 10.75, 9.50, 24.5, 15.45]

# Print the list of areas in reverse order without modifying the original list
print(areas[::-1])
# Expected result: [15.45, 24.5, 9.50, 10.75, 20.0, 18.0, 11.25]

# The original list was not modified by the previous operation
print(areas)
# Still: [11.25, 18.0, 20.0, 10.75, 9.50, 24.5, 15.45]

# Reverse the list in place (modifies the original list)
areas.reverse()

# Print the list of areas after reversal
print(areas)
# Expected result: [15.45, 24.5, 9.50, 10.75, 20.0, 18.0, 11.25]