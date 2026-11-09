

# 1. What is a variable in Python?
from tkinter.font import names
from wsgiref import types


print("A variable is a named container used to store data values in memory so they can be referenced and manipulated throughout a program.")

# 2. Can a variable name start with a number? Why or why not?
print("Python variable names cannot start with a number because the interpreter would confuse it with a numeric literal (like `123var`), making syntax parsing ambiguous. Variable names must start with a letter or an underscore (`_`).")

# 3. What is the difference between assigning a value and comparing a value?
print("Assignment (`=`):** Stores a value into a variable (e.g., `x = 5`).")
print("Comparison (`==`):** Checks if two values are equal, evaluating to `True` or `False` (e.g., `x == 5`).")

# 4. If you assign a variable a new value, what happens to the old value?
print("The old value is replaced in the variable. If no other variables or data structures reference that old value, Python's automated garbage collector frees up the memory it occupied.")

#5. Why is it important to give a variable a meaningful name?
print("Meaningful names (e.g., `user_age` instead of `x`) make code self-documenting, readable, and much easier to maintain, understand, and debug for yourself and other developers.")

# 6. What are the 4 main data types in Python?
print("Integers (`int`), Floats (`float`), Strings (`str`),Booleans (`bool`) ")

# 7. What is the difference between an integer and a float?
print("Q7:", "An interger is a whole number while a float is a decimal number")

# 8. What data type is used to store True or False?
print("The Boolean data type (`bool`).")

### 9. What is the difference between a string and a character?
print("Python does not have a distinct character data type. A single character is simply treated as a string of length 1. A string (`str`) is a sequence of zero or more characters.")

# # 10. What happens when you try to add a number and a string together?
# print("Python raises a `TypeError` because it cannot implicitly convert between incompatible data types (e.g., `5 + "hello"`).")

# 11. What is a list in Python?
print("Q11:", "A list is an array  assigned to a variable using bracket []")

# 12. What is the difference between a list and a variable that holds one value?
print("A standard variable holds a single value at a time, whereas a list can hold a collection of multiple values (elements) indexed sequentially.")

# 13. What is an index in a list? What is the index of the first item?
print("An index is the numerical position of an item within a list. Python uses zero-based indexing, so the index of the first item is `0`.")

# 14. Can a list hold different data types at the same time? Explain.
print("Yes. Python lists are heterogeneous, meaning a single list can contain integers, strings, floats, booleans, and even other lists simultaneously (e.g., `[1, apple, 3.5, True]`).")

# 15. What is the difference between adding an item to a list and removing an item from a list?
print("Adding:** Increases the list size by inserting a new element (e.g., using `.append()`).")
print("Removing:** Decreases the list size by deleting an existing element (e.g., using `.remove()` or `.pop()`).")

# 16. What is an operator in Python?
print("A special symbol or keyword used to perform operations on values and variables (such as arithmetic, comparison, or logical evaluation).")

### 17. What is the difference between the assignment operator and the equality operator?
print("Q17:", "Assignment operator is used to assign a value to a variable while equality operator is used to compare values if see they are equal")


# 18. Name 3 arithmetic operators and what they do.
print("Addition (`+`): Adds two operands.")
print("Subtraction (`-`): Subtracts the right operand from the left.")
print("Multiplication (`*`): Multiplies two operands.")

### 19. What is the difference between division and floor division?
print("Division (`/`):** Performs true division, returning a float result (e.g., `5 / 2 = 2.5`).")
print("Floor Division (`//`):** Divides and rounds down to the nearest integer, discarding any fractional remainder (e.g., `5 // 2 = 2`).")

# 20. What does the modulus operator do? Give an example in words.
print("The modulus operator (`%`) returns the remainder of a division operation. For example, `10 % 3` results in `1` because 3 fits into 10 three times with a remainder of 1.")

# 21. What is the purpose of input in Python?
print("To allow a program to pause execution and accept data entered by the user via the console/command line.")

# 22. When a user types a number using input, what data type does Python treat it as by default?
print("A string (`str`).")

# 23. Why do we need to convert input before doing calculations with it?
print("Because `input()` returns data as a string, Python cannot perform arithmetic on it directly. You must explicitly convert it to a numeric type (like `int` or `float`) to avoid a `TypeError`.")

# 24. What happens if you ask for input but the user types nothing and presses enter?
print("Python returns an empty string (`""`) without throwing an error.")

# 25. What is the difference between input and print?
print("* `input()` takes data *from* the user.")
print("* `print()` sends data *to* the user's screen.")

# 26. What is the purpose of if else in Python?
print("To allow conditional execution of code blocks, enabling a program to make decisions and execute different code paths based on whether specific conditions evaluate to true or false.")

# 27. What is a condition? Give an example in words.
print("An expression that evaluates to a boolean value (`True` or `False`).")

# 28. What is the difference between if and elif?
print("* An `if` statement initiates a new conditional check.")
print("* An `elif` short for else if checks an alternative condition only if all preceding `if` and `elif` conditions evaluated to `False`.")

# 29. What happens if none of the conditions in an if-elif-else statement are true?
print("If an `else` block is present, its code block executes. If there is no `else` block, the entire conditional structure is skipped, and execution continues with the next statement outside the structure.")

### 30. Why is indentation very important in if else statements?
print("Python uses whitespace (indentation) instead of curly braces or keywords to define code blocks. Incorrect indentation will cause an `IndentationError` or result in flawed logic where code runs outside its intended conditional block.")