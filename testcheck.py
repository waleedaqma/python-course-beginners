def namealpha():
    name = input("what's your name? ")
    return name.isalpha()

if not namealpha():
    print("Invalid name! Only letters allowed.")
else:
    age = input("how old are you? ")
    total_marks = int(input("total_marks? "))