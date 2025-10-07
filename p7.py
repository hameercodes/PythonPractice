# Define a Person class with name and age. Add a method to check if the person is an adult.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def adult(self):
        if(self.age>=18):
            print(f"{self.name} is a adult.")
        else:
            print(f"{self.name} is a child.")

p1 = Person("Harikrishna", 65)
p1.adult()
