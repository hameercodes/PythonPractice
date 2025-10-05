#Create a Car class with attributes brand and model. Create two objects and print their details.
class Car:
    #default constructor
    def __init__(self):
        pass
    #parameterized constructors
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("BMW", "Pickup")
c2 = Car("Mustang","Coupe")
print(c1.brand)
print(c1.model)
print(c2.brand)
print(c2.model)