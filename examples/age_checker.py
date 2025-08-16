# Age Checker - Learn Conditional Statements
# This program demonstrates if/elif/else statements and user input

print("=== Age Checker ===")
print("Let's find out what stage of life you're in!")

# Get the user's age
try:
    age = int(input("Enter your age: "))
    
    # Check if age is valid
    if age < 0:
        print("❌ Invalid age! Age cannot be negative.")
    elif age > 150:
        print("❌ That seems like an unrealistic age!")
    else:
        # Determine life stage
        if age < 1:
            print("👶 You're a baby!")
        elif age < 3:
            print("🧒 You're a toddler!")
        elif age < 13:
            print("👦 You're a child!")
        elif age < 20:
            print("👨‍🎓 You're a teenager!")
        elif age < 30:
            print("👨‍💼 You're a young adult!")
        elif age < 50:
            print("👨‍💻 You're in your prime working years!")
        elif age < 65:
            print("👨‍🏫 You're a mature adult!")
        else:
            print("👴 You're a senior citizen!")
        
        # Additional information based on age
        print(f"\n=== Age Facts ===")
        print(f"You are {age} years old")
        
        # Calculate some interesting facts
        birth_year = 2024 - age
        next_birthday = age + 1
        
        print(f"You were probably born around {birth_year}")
        print(f"Next year you'll be {next_birthday} years old")
        
        # Legal status
        if age >= 18:
            print("✅ You are legally an adult!")
            if age >= 21:
                print("✅ You can drink alcohol (in most countries)")
            if age >= 25:
                print("✅ You can rent a car (in most places)")
        else:
            years_to_adult = 18 - age
            print(f"⏳ You'll be an adult in {years_to_adult} years")
        
        # School status
        if age < 5:
            print("🏠 You're too young for school")
        elif age < 18:
            print("🏫 You're in school age")
        elif age < 25:
            print("🎓 You're in college age")
        else:
            print("💼 You're in working age")
            
        # Fun facts
        print(f"\n=== Fun Facts ===")
        if age % 10 == 0:
            print("🎉 You have a milestone birthday this year!")
        
        if age < 18:
            print("🌟 You have your whole life ahead of you!")
        elif age < 30:
            print("🚀 You're building your future!")
        elif age < 50:
            print("💪 You're in your most productive years!")
        else:
            print("🎯 You have wisdom and experience!")
            
except ValueError:
    print("❌ Please enter a valid number for your age!")
except KeyboardInterrupt:
    print("\n👋 Goodbye! Thanks for using the Age Checker!")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

print("\n🎉 Thanks for using the Age Checker!")
print("Come back anytime to check your age status!")
