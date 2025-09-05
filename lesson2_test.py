print("=== School Result ===")

name = input("What's your name: ")
age = int(input("What's your age: "))
total_marks = int(input("Total Marks? "))
obtain_marks = int(input("Obtain Marks: "))

percentage = (obtain_marks / total_marks) * 100

print("\n=== Results ===")
print("Your name is:", name)
print("Your age is:", age)
print("Total Marks:", total_marks)
print("Obtained Marks:", obtain_marks)
print("Percentage:", percentage, "%")

if percentage < 20:
    print("Fail")
elif percentage < 30:
    print("Fail")
elif percentage < 50:
    print("Good")
elif percentage < 60:
    print("Good")
elif percentage < 70:
    print("Excellent")
elif percentage < 80:
    print("Excellent")
else:
    print("Sounds Good")
