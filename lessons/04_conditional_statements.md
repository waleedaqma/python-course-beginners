# Lesson 4: Conditional Statements (if/else)

## 🎯 What You'll Learn
- How to make decisions in your programs
- Using if, elif, and else statements
- Comparison operators
- Logical operators
- Building complex decision trees

## 🧠 Making Decisions in Programs

Conditional statements allow your program to make decisions based on certain conditions. Think of them as "if this happens, then do that" instructions.

## 🔍 Comparison Operators

First, let's learn how to compare values:

```python
# Equal to
x == y        # True if x equals y

# Not equal to
x != y        # True if x does NOT equal y

# Greater than
x > y         # True if x is greater than y

# Less than
x < y         # True if x is less than y

# Greater than or equal to
x >= y        # True if x is greater than or equal to y

# Less than or equal to
x <= y        # True if x is less than or equal to y
```

## 📝 Basic if Statement

The simplest form of conditional statement:

```python
age = 18

if age >= 18:
    print("You are an adult!")
    print("You can vote!")
    print("You can drive!")

print("This always runs, regardless of age")
```

**Important**: Notice the colon `:` after the condition and the indentation (spaces) for the code block.

## 🔀 if-else Statement

When you want to handle both cases:

```python
age = 16

if age >= 18:
    print("You are an adult!")
    print("You can vote and drive!")
else:
    print("You are a minor!")
    print("You need to wait a bit longer!")

print("This always runs!")
```

## 🚦 if-elif-else Statement

For multiple conditions:

```python
score = 85

if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Good job!")
elif score >= 70:
    print("Grade: C")
    print("Satisfactory!")
elif score >= 60:
    print("Grade: D")
    print("Needs improvement!")
else:
    print("Grade: F")
    print("Failed!")
```

## 🔗 Logical Operators

Combine multiple conditions:

```python
age = 25
has_license = True
has_car = False

# AND operator - both conditions must be True
if age >= 18 and has_license:
    print("You can drive legally!")

# OR operator - at least one condition must be True
if has_license or has_car:
    print("You have some transportation options!")

# NOT operator - inverts the condition
if not has_car:
    print("You don't have a car yet!")

# Complex conditions
if (age >= 18 and has_license) or has_car:
    print("You can get around!")
```

## 🎯 Practical Examples

### Example 1: Age Checker
```python
print("=== Age Checker ===")
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age! Age cannot be negative.")
elif age < 13:
    print("You're a child!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're a senior!")
```

### Example 2: Password Checker
```python
print("=== Password Checker ===")
password = input("Enter your password: ")

# Check password strength
if len(password) < 6:
    print("Password is too short! Must be at least 6 characters.")
elif len(password) < 10:
    print("Password is okay, but could be stronger.")
elif len(password) < 15:
    print("Good password strength!")
else:
    print("Excellent password strength!")

# Check for common patterns
if password.lower() == "password":
    print("Warning: 'password' is too common!")
elif password.lower() == "123456":
    print("Warning: '123456' is too common!")
```

### Example 3: Weather Advisor
```python
print("=== Weather Advisor ===")
temperature = float(input("Enter temperature (°C): "))
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"

if temperature < 0:
    print("It's freezing! Bundle up!")
    if is_raining:
        print("And it's raining - be careful of ice!")
elif temperature < 15:
    print("It's cold! Wear a jacket!")
    if is_raining:
        print("Don't forget your umbrella!")
elif temperature < 25:
    print("Nice weather! Enjoy your day!")
    if is_raining:
        print("Light rain - maybe bring a light jacket!")
else:
    print("It's warm! Stay hydrated!")
    if is_raining:
        print("Warm rain - perfect for a refreshing walk!")
```

## 🎮 Nested if Statements

You can put if statements inside other if statements:

```python
age = 25
has_license = True
has_car = True

if age >= 18:
    print("You're old enough to drive!")
    
    if has_license:
        print("Great! You have a license!")
        
        if has_car:
            print("Perfect! You can drive your car!")
        else:
            print("You can drive, but you need a car!")
    else:
        print("You need to get a license first!")
else:
    print("You're too young to drive!")
```

## ✅ Practice Exercises

### Exercise 1: Grade Calculator
Create a program that:
1. Asks for a test score (0-100)
2. Assigns a letter grade (A, B, C, D, F)
3. Gives specific feedback for each grade range

### Exercise 2: Shopping Discount
Create a program that:
1. Asks for the purchase amount
2. Applies different discount rates based on amount:
   - $0-$50: 5% discount
   - $51-$100: 10% discount
   - $101+: 15% discount
3. Shows the final price

### Exercise 3: Movie Rating
Create a program that:
1. Asks for the user's age
2. Asks for the movie rating (G, PG, PG-13, R)
3. Tells them if they can watch the movie
4. Gives appropriate warnings

## 🔍 Common Mistakes to Avoid

1. **Missing colons**
   ```python
   # Wrong
   if age >= 18
       print("Adult!")
   
   # Right
   if age >= 18:
       print("Adult!")
   ```

2. **Wrong indentation**
   ```python
   # Wrong - this will cause an error
   if age >= 18:
   print("Adult!")
   
   # Right
   if age >= 18:
       print("Adult!")
   ```

3. **Using = instead of ==**
   ```python
   # Wrong - this assigns, doesn't compare
   if age = 18:
       print("Adult!")
   
   # Right
   if age == 18:
       print("Adult!")
   ```

4. **Forgetting else clauses**
   ```python
   # This might miss some cases
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   # What about scores below 80?
   ```

## 🎯 Key Concepts Summary

- **if statements** make decisions based on conditions
- **elif** handles multiple specific conditions
- **else** catches all other cases
- **Comparison operators** compare values
- **Logical operators** combine conditions
- **Indentation** is crucial for code blocks
- **Nested ifs** allow complex decision trees

## 📚 What's Next?

In the next lesson, we'll explore:
- Loops (for and while)
- Repeating actions
- Iterating through data
- Building more dynamic programs

## 💡 Pro Tips

- **Use meaningful variable names** for conditions
- **Keep conditions simple** - break complex logic into smaller parts
- **Test edge cases** - what happens with boundary values?
- **Use comments** to explain complex logic
- **Think about the user experience** - what should happen in unexpected cases?

---

**🎉 Fantastic!** You now know how to make your programs intelligent and responsive. Your code can now make decisions and handle different situations!

**Next**: [Lesson 5: Loops](../lessons/05_loops.md)
