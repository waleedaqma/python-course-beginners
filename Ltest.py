
name = input("what's your name? ")
age = int(input("your age is? "))
if not name.isalpha():
    print("Invalid name! Only alphabets (A–Z) allowed.")
    name = input("what's your name? ")

total_marks = int(input("total_marks? "))
obtain_marks = int(input("obtain_marks? "))

percentage = (obtain_marks / total_marks) *100 

print("n/=== results ===")
print("your name is:", name)
print("your age is:", age)
print("total_marks:", total_marks)
print("obtain_marks:", obtain_marks)
print("percentage:", percentage, "%")

          
if   percentage <= 50:
     print("fail") 
elif percentage <=50:
     print("exilent") 
else:
     print("sound's good")

