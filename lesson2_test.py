# First try
name = input("Please enter your name: ")

if not name.isalpha():
            print("Invalid name entered too many times. Exiting...")
else:
    print("Name", name)

age = int(input("Enter your age: "))
total_marks = 100
marks_obtained = int(input("Enter the marks obtained: "))

percentage = (marks_obtained / total_marks) * 100

print("---")
print("Name:", name)
print("Age:", age)
print("Percentage:", percentage, "%")

if percentage <= 30:
    print("Fail")
elif percentage <= 50:
    print("Pass")
elif percentage <= 60:
    print("Good")
elif percentage <= 80:
    print("Excellent")
else:
    print("Sounds Good")
