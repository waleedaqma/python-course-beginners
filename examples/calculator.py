# Simple Calculator - Learn Variables and Math Operations
# This program shows how to get input from users and perform calculations

print("=== Simple Calculator ===")
print("Let's do some math together!")

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division carefully (avoid division by zero)
if num2 != 0:
    division = num1 / num2
    division_result = f"{num1} ÷ {num2} = {division}"
else:
    division_result = "Cannot divide by zero!"

# Show results
print("\n=== Results ===")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} × {num2} = {multiplication}")
print(division_result)

# Show some additional operations
print(f"\n=== Bonus Operations ===")
print(f"Power: {num1} ^ {num2} = {num1 ** num2}")
print(f"Remainder: {num1} % {num2} = {num1 % num2}")
print(f"Average: ({num1} + {num2}) ÷ 2 = {(num1 + num2) / 2}")

# Give some fun facts
print(f"\n=== Fun Facts ===")
if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("Both numbers are equal!")

if (num1 + num2) % 2 == 0:
    print("The sum is an even number!")
else:
    print("The sum is an odd number!")

print("\n🎉 Great job using the calculator!")
print("Try running it again with different numbers!")
