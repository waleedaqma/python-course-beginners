name = input("Enter your name: ")
age = int(input("Enter your age: "))
total_marks = 1200
marks_obtained = int(input("Enter the marks obtained: "))
percentage = (marks_obtained / total_marks) * 100
print("Percentage:", percentage) 

if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
else:
    print("Grade: D")
