class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hi", self.name, "your avg score is:", total/len(self.marks))  

si = Student("Qasim Shah", [99, 98, 97])  
si.get_avg()
si.name = "Raza"
si.get_avg()