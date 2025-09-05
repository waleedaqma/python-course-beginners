# A simple program to calculate percentage and grade based on marks obtained
name = input("Enter your name: ")
# Student Information
age = int(input("Enter your age: "))
# Marks Information
total_marks = 1200
# Get marks obtained from user
marks_obtained = int(input("Enter the marks obtained: "))
# Calculate percentage
percentage = (marks_obtained / total_marks) * 100
# Display percentage
print("Percentage:", percentage) 
# Display grade
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
else:
    print("Grade: D")
