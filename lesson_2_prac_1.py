name = input("What is your name? ")
print("Hello", name, "welcome to your personal calculator!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2

print("\nHere are your results, " + name + ":")
print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Quotient", quot)