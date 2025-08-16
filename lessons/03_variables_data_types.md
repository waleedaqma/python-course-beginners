# Lesson 3: Variables and Data Types

## 🎯 What You'll Learn
- Understanding different data types in Python
- How to work with numbers (integers and floats)
- String operations and methods
- Boolean values and type checking
- How to convert between data types

## 🔢 Numbers: Integers and Floats

Python has two main types of numbers:

### Integers (int)
Whole numbers without decimal points:
```python
age = 25
year = 2024
temperature = -5
population = 8000000000
```

### Floats (float)
Numbers with decimal points:
```python
height = 5.8
pi = 3.14159
price = 19.99
temperature = 98.6
```

## 🧮 Mathematical Operations

Python can perform all basic mathematical operations:

```python
# Addition
a = 10 + 5        # Result: 15

# Subtraction
b = 10 - 5        # Result: 5

# Multiplication
c = 10 * 5        # Result: 50

# Division (always returns float)
d = 10 / 5        # Result: 2.0

# Floor Division (returns integer)
e = 10 // 3       # Result: 3

# Modulo (remainder)
f = 10 % 3        # Result: 1

# Exponentiation (power)
g = 2 ** 3        # Result: 8

# Negative numbers
h = -5
i = abs(-5)       # Absolute value: 5
```

## 📝 Strings: Working with Text

Strings are sequences of characters (letters, numbers, symbols):

```python
# Creating strings
name = "Alice"
message = 'Hello, World!'
long_text = """This is a
multi-line string
that spans several lines"""

# String length
print(len(name))  # Output: 5

# Accessing characters (indexing starts at 0)
first_letter = name[0]    # 'A'
last_letter = name[-1]    # 'e'
```

## 🔤 String Methods

Strings come with many useful methods:

```python
text = "  Hello, World!  "

# Case conversion
print(text.upper())        # "  HELLO, WORLD!  "
print(text.lower())        # "  hello, world!  "
print(text.title())        # "  Hello, World!  "

# Removing whitespace
print(text.strip())        # "Hello, World!"
print(text.lstrip())       # "Hello, World!  "
print(text.rstrip())       # "  Hello, World!"

# Finding and replacing
print(text.find("World"))  # 8 (position of "World")
print(text.replace("World", "Python"))  # "  Hello, Python!  "

# Checking content
print(text.startswith("  Hello"))  # True
print(text.endswith("!  "))        # True
print("Hello" in text)             # True
```

## 🔗 String Concatenation and Formatting

```python
first_name = "John"
last_name = "Doe"
age = 30

# Method 1: Using + operator
full_name = first_name + " " + last_name

# Method 2: Using f-strings (recommended)
message = f"My name is {first_name} {last_name} and I am {age} years old"

# Method 3: Using .format() method
message2 = "My name is {} {} and I am {} years old".format(first_name, last_name, age)

# Method 4: Using % operator (older style)
message3 = "My name is %s %s and I am %d years old" % (first_name, last_name, age)
```

## ✅ Boolean Values (True/False)

Booleans represent truth values:

```python
is_student = True
is_working = False

# Comparison operators return booleans
age = 25
is_adult = age >= 18        # True
is_teenager = 13 <= age <= 19  # False

# Logical operators
has_permission = True
is_logged_in = False

# AND operator (both must be True)
can_access = has_permission and is_logged_in  # False

# OR operator (at least one must be True)
can_view = has_permission or is_logged_in     # True

# NOT operator (inverts the value)
cannot_access = not has_permission            # False
```

## 🔍 Type Checking and Conversion

### Checking Data Types
```python
name = "Alice"
age = 25
height = 5.6
is_student = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

### Type Conversion
```python
# String to number
text_number = "42"
number = int(text_number)      # 42
decimal = float(text_number)   # 42.0

# Number to string
age = 25
age_text = str(age)           # "25"

# Float to integer (truncates decimal part)
price = 19.99
whole_price = int(price)      # 19

# Boolean conversion
print(bool(1))                # True
print(bool(0))                # False
print(bool("Hello"))          # True
print(bool(""))               # False
```

## 🚀 Practical Examples

### Example 1: Calculator
```python
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} × {num2} = {num1 * num2}")
print(f"Division: {num1} ÷ {num2} = {num1 / num2}")
print(f"Power: {num1} ^ {num2} = {num1 ** num2}")
```

### Example 2: String Manipulation
```python
print("=== String Playground ===")
sentence = input("Enter a sentence: ")

print(f"Original: {sentence}")
print(f"Length: {len(sentence)} characters")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Title case: {sentence.title()}")
print(f"Words count: {len(sentence.split())}")
```

### Example 3: Type Detective
```python
print("=== Type Detective ===")
value = input("Enter any value: ")

# Try to determine the type
if value.lower() in ['true', 'false']:
    print("This looks like a boolean!")
elif value.replace('.', '').replace('-', '').isdigit():
    if '.' in value:
        print("This looks like a float!")
    else:
        print("This looks like an integer!")
else:
    print("This looks like a string!")
```

## ✅ Practice Exercises

### Exercise 1: Number Analyzer
Create a program that:
1. Asks for a number
2. Tells you if it's positive, negative, or zero
3. Tells you if it's even or odd
4. Shows its square and cube

### Exercise 2: Text Transformer
Create a program that:
1. Asks for a word or phrase
2. Shows it in different cases (upper, lower, title)
3. Counts the characters and words
4. Reverses the text

### Exercise 3: Smart Calculator
Create a program that:
1. Asks for two numbers
2. Performs all basic operations
3. Shows the results with proper formatting
4. Handles division by zero gracefully

## 🔍 Common Mistakes to Avoid

1. **Mixing types without conversion**
   ```python
   # Wrong
   age = "25"
   next_age = age + 1  # Error!
   
   # Right
   age = int("25")
   next_age = age + 1  # Works!
   ```

2. **Forgetting that division returns float**
   ```python
   result = 10 / 2  # This is 5.0, not 5
   ```

3. **String indexing out of bounds**
   ```python
   text = "Hello"
   print(text[10])  # Error! String only has 5 characters
   ```

## 🎯 Key Concepts Summary

- **Integers** are whole numbers
- **Floats** are decimal numbers
- **Strings** are text (use quotes)
- **Booleans** are True/False values
- **Type conversion** changes data types
- **String methods** help manipulate text
- **Mathematical operations** work as expected

## 📚 What's Next?

In the next lesson, we'll explore:
- Conditional statements (if/else)
- Making decisions in programs
- Comparing values
- Building more complex logic

## 💡 Pro Tips

- **Use f-strings** for string formatting - they're cleaner and more readable
- **Check types** when debugging - `print(type(variable))` is your friend
- **Practice with real data** - try different inputs to test your programs
- **Use meaningful variable names** - it makes code self-documenting

---

**🎉 Excellent work!** You now understand the fundamental building blocks of Python programming. You can work with numbers, text, and make basic calculations!

**Next**: [Lesson 4: Conditional Statements](../lessons/04_conditional_statements.md)
