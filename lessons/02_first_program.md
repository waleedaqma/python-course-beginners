# Lesson 2: Your First Interactive Python Program

## 🎯 What You'll Learn
- How to create variables to store information
- How to get input from users
- How to combine different types of data
- Basic string formatting

## 🔤 Variables: Storing Information

Variables are like containers that hold information. Think of them as labeled boxes where you can store things.

```python
# Creating variables
name = "Alice"
age = 25
height = 5.6
is_student = True

# Printing variables
print(name)
print(age)
print(height)
print(is_student)
```

## 📝 Variable Naming Rules

- **Letters, numbers, and underscores** are allowed
- **Must start with a letter or underscore**
- **Case sensitive** - `Name` and `name` are different
- **Use descriptive names** - `user_age` is better than `a`

```python
# Good variable names
first_name = "John"
last_name = "Doe"
user_age = 30
is_active = True

# Avoid these (not descriptive)
a = "John"
b = "Doe"
x = 30
```

## 🎯 Getting User Input

The `input()` function lets your program ask questions and wait for answers:

```python
# Basic input
name = input("What's your name? ")
print("Hello, " + name + "!")

# Input with numbers
age = input("How old are you? ")
print("You are " + age + " years old")
```

## ⚠️ Important: Input Always Returns Strings

When you use `input()`, Python always gives you text (a string), even if the user types a number:

```python
age = input("Enter your age: ")
print("Type of age:", type(age))  # This will show: <class 'str'>

# To convert to a number, use int() or float()
age_number = int(age)
print("Age as number:", age_number)
print("Type of age_number:", type(age_number))  # This will show: <class 'int'>
```

## 🔄 Type Conversion Functions

- `int()` - converts to whole number (integer)
- `float()` - converts to decimal number
- `str()` - converts to text (string)

```python
# Converting between types
text_number = "42"
actual_number = int(text_number)
decimal_number = float(text_number)

print("Text:", text_number, type(text_number))
print("Integer:", actual_number, type(actual_number))
print("Float:", decimal_number, type(decimal_number))
```

## 🚀 Building Your First Interactive Program

Let's create a program that asks for your name and age, then tells you something interesting:

```python
# Get user information
print("=== Personal Information Program ===")
name = input("What's your name? ")
age = input("How old are you? ")

# Convert age to number
age_number = int(age)

# Calculate some interesting facts
birth_year = 2024 - age_number
next_birthday = age_number + 1

# Display results
print("\n=== Results ===")
print("Hello, " + name + "!")
print("You are " + str(age_number) + " years old")
print("You were probably born around " + str(birth_year))
print("Next year you'll be " + str(next_birthday) + " years old")

# Add some fun facts
if age_number < 18:
    print("You're still a teenager!")
elif age_number < 65:
    print("You're in your prime working years!")
else:
    print("You're enjoying your golden years!")
```

## 🎨 String Formatting (Modern Way)

Python has a more elegant way to format strings using f-strings (formatted strings):

```python
name = "Alice"
age = 25

# Old way (concatenation)
print("Hello, " + name + "! You are " + str(age) + " years old")

# New way (f-strings) - much cleaner!
print(f"Hello, {name}! You are {age} years old")

# You can even do calculations inside f-strings
print(f"Next year you'll be {age + 1} years old")
```

## ✅ Practice Exercises

### Exercise 1: Personal Calculator
Create a program that:
1. Asks for the user's name
2. Asks for two numbers
3. Calculates and displays the sum, difference, product, and quotient

### Exercise 2: Temperature Converter
Create a program that:
1. Asks for a temperature in Celsius
2. Converts it to Fahrenheit (F = C × 9/5 + 32)
3. Displays both temperatures

### Exercise 3: Mad Libs
Create a program that:
1. Asks for various words (noun, verb, adjective)
2. Uses them in a funny sentence
3. Displays the complete story

## 🔍 Common Mistakes to Avoid

1. **Forgetting to convert input types**
   ```python
   # Wrong
   age = input("Age: ")
   next_age = age + 1  # Error! Can't add string and number
   
   # Right
   age = int(input("Age: "))
   next_age = age + 1  # Works!
   ```

2. **Using wrong variable names**
   ```python
   # Wrong
   Name = "John"  # Capital N
   print(name)    # lowercase n - will cause error
   
   # Right
   name = "John"
   print(name)
   ```

3. **Not handling invalid input**
   ```python
   # This will crash if user types letters instead of numbers
   age = int(input("Age: "))
   
   # Better approach (we'll learn this in later lessons)
   try:
       age = int(input("Age: "))
   except ValueError:
       print("Please enter a valid number!")
   ```

## 🎯 Key Concepts Summary

- **Variables** store different types of data
- **input()** gets information from users
- **Type conversion** changes data from one type to another
- **f-strings** make string formatting easy and readable
- **Comments** help explain your code

## 📚 What's Next?

In the next lesson, we'll explore:
- Different data types in detail
- Mathematical operations
- More complex calculations
- Working with text

## 💡 Pro Tips

- **Test your programs** with different inputs
- **Use meaningful variable names** - it makes code easier to read
- **Add comments** to explain what your code does
- **Practice with real examples** - try to solve problems you encounter

---

**🎉 Great job!** You've now created interactive programs that can respond to user input. You're building real applications!

**Next**: [Lesson 3: Variables and Data Types](../lessons/03_variables_data_types.md)
