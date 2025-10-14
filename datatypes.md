# Python Data Types

Python provides various data types to define the type of data a variable can hold. Below are some commonly used data types:

## 1. **String (`str`)**
- Represents text data.
- Enclosed in single, double, or triple quotes.
- Example:
    ```python
    name = "John"
    greeting = 'Hello'
    paragraph = """This is a multi-line string."""
    ```

## 2. **Integer (`int`)**
- Represents whole numbers (positive or negative).
- Example:
    ```python
    age = 25
    temperature = -10
    ```

## 3. **Float (`float`)**
- Represents decimal numbers.
- Example:
    ```python
    pi = 3.14
    height = 5.9
    ```

## 4. **Decimal (`decimal.Decimal`)**
- Provides higher precision for decimal numbers.
- Requires importing the `decimal` module.
- Example:
    ```python
    from decimal import Decimal
    price = Decimal('19.99')
    ```

## 5. **Fraction (`fractions.Fraction`)**
- Represents rational numbers as fractions.
- Requires importing the `fractions` module.
- Example:
    ```python
    from fractions import Fraction
    ratio = Fraction(3, 4)  # Represents 3/4
    ```

## 6. **Boolean (`bool`)**
- Represents `True` or `False` values.
- Example:
    ```python
    is_active = True
    has_permission = False
    ```

## 7. **List (`list`)**
- Represents an ordered collection of items.
- Mutable and can contain mixed data types.
- Example:
    ```python
    fruits = ["apple", "banana", "cherry"]
    numbers = [1, 2, 3, 4]
    ```

## 8. **Tuple (`tuple`)**
- Represents an ordered collection of items.
- Immutable and can contain mixed data types.
- Example:
    ```python
    coordinates = (10, 20)
    colors = ("red", "green", "blue")

## 9. **Set (`set`)**
- Represents an unordered collection of unique items.
- Example:
    ```python
    unique_numbers = {1, 2, 3, 4}
    ```

## 10. **Dictionary (`dict`)**
- Represents a collection of key-value pairs.
- Example:
    ```python
    person = {"name": "Alice", "age": 30}
    ```

    ## File Handling in Python

    Python provides built-in functions to work with files, allowing you to read, write, and manipulate file data. Below are some common file operations:

    ### Opening a File
    - Use the `open()` function to open a file.
    - Modes:
        - `'r'`: Read (default mode).
        - `'w'`: Write (overwrites the file if it exists).
        - `'a'`: Append (adds content to the end of the file).
        - `'rb'`, `'wb'`: Binary modes for reading/writing binary files.

    Example:
    ```python
    file = open("example.txt", "r")  # Opens a file in read mode
    ```

    ### Reading a File
    - Use `read()`, `readline()`, or `readlines()` to read file content.

    Example:
    ```python
    with open("example.txt", "r") as file:
            content = file.read()
            print(content)
    ```

    ### Writing to a File
    - Use `write()` or `writelines()` to write data to a file.

    Example:
    ```python
    with open("example.txt", "w") as file:
            file.write("Hello, World!")
    ```

    ### Appending to a File
    - Use the `'a'` mode to add content without overwriting.

    Example:
    ```python
    with open("example.txt", "a") as file:
            file.write("\nAppended text.")
    ```

    ### Closing a File
    - Always close a file after use to free up system resources.
    - Use `with` statements to handle files automatically.

    Example:
    ```python
    file = open("example.txt", "r")
    file.close()
    ```

    ### Checking if a File Exists
    - Use the `os` module to check for file existence.

    Example:
    ```python
    import os
    if os.path.exists("example.txt"):
            print("File exists.")
    else:
            print("File does not exist.")
    ```

    File handling is essential for working with data stored in files, enabling efficient data management in Python.

These data types allow Python to handle a wide range of data efficiently.

advance : decorators ,genrators , iterators , comprehensions , context managers , metaprogramming 
