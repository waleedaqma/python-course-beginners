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