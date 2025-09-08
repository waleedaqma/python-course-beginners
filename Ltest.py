name = input("what's your name? ")
age = input("how old are you? ")
total_marks = int(input("total_marks? "))
obtain_marks = int(input("obtain_marks "))

percentage = (obtain_marks / total_marks) *100 

print("n/=== results ===")
print("your name is:", name)
print("your age is:", age )
print("total_marks:", total_marks)
print("obtain_marks:", obtain_marks)
print("percentage:", percentage, "%")

if   percentage <= 20:
     print("fail")
elif percentage <=50:
     print("grade") 
else:
     print("goood")  