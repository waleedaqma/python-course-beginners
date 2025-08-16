# Project 1: Advanced Calculator
# This project combines everything you've learned so far:
# - Variables and data types
# - User input and type conversion
# - Conditional statements
# - Error handling
# - String formatting

print("🧮 Welcome to the Advanced Calculator!")
print("=" * 40)

def main():
    while True:
        print("\n📋 Available Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Percentage (%)")
        print("8. Exit")
        
        try:
            choice = input("\nChoose an operation (1-8): ")
            
            if choice == '8':
                print("👋 Thanks for using the Advanced Calculator!")
                break
            elif choice in ['1', '2', '3', '4', '5', '7']:
                # Get two numbers for most operations
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = num1 + num2
                    operation = "+"
                elif choice == '2':
                    result = num1 - num2
                    operation = "-"
                elif choice == '3':
                    result = num1 * num2
                    operation = "×"
                elif choice == '4':
                    if num2 == 0:
                        print("❌ Error: Cannot divide by zero!")
                        continue
                    result = num1 / num2
                    operation = "÷"
                elif choice == '5':
                    result = num1 ** num2
                    operation = "^"
                elif choice == '7':
                    result = (num1 * num2) / 100
                    operation = "% of"
                
                print(f"\n📊 Result: {num1} {operation} {num2} = {result}")
                
            elif choice == '6':
                # Square root only needs one number
                num = float(input("Enter a number: "))
                if num < 0:
                    print("❌ Error: Cannot calculate square root of negative number!")
                    continue
                result = num ** 0.5
                print(f"\n📊 Result: √{num} = {result}")
                
            else:
                print("❌ Invalid choice! Please select 1-8.")
                continue
            
            # Ask if user wants to continue
            continue_calc = input("\n🔢 Calculate something else? (yes/no): ").lower()
            if continue_calc not in ['yes', 'y', 'yeah', 'sure']:
                print("👋 Thanks for using the Advanced Calculator!")
                break
                
        except ValueError:
            print("❌ Error: Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n👋 Goodbye! Thanks for using the Advanced Calculator!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

def show_calculator_info():
    print("\nℹ️  Calculator Information:")
    print("• This calculator supports basic and advanced operations")
    print("• All calculations are performed with high precision")
    print("• Error handling prevents crashes from invalid input")
    print("• You can perform multiple calculations in one session")

if __name__ == "__main__":
    show_calculator_info()
    main()
