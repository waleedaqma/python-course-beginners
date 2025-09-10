name = input("Enter your name: ")
assert name.isalpha()

age = int(input("Enter your age: "))
total_marks = 100
marks_obtained = int(input("Enter the marks obtained: "))
percentage = (marks_obtained / total_marks) * 100
print("Percentage:", percentage, "%") 

print("Name: ", name)
print("Age: ", age)

if percentage <= 30:
    print("Fail")
elif percentage <= 50:
    print("pass")
elif percentage <= 60:
    print("Good")
elif percentage <= 80:
    print("Excellent")
else:
    print("Sounds Good")