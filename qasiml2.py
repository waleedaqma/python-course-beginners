file = open("qasiml2.py", "r")
data = file.read()
print(data)

with open("qasiml2.py", "r") as file:
    for line in file:
        print(line.strip()) 
with open("qasiml2.py", "r") as file:
    lines = file.readlines()

print(lines)  