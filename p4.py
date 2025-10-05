#Create a Student class with attributes name and marks (list). Add a method to compute the average marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        i=0
        ttl = 0
        for i in range(len(self.marks)):
            ttl = ttl + self.marks[i]
        avg = ttl/len(self.marks)
        print(f"{self.name} has {avg} average marks.")
s1 = Student("Ravi",[45,22,46,11,25])
s1.average()
s2 = Student("Santosh",[35,44,24,33,29])
s2.average()
#Abstraction --> what mechanism or data you have inside a class is hidden from outside the class.
