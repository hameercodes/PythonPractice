#Make a Book class with attributes title, author, and pages. Add a method to display book details.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    @staticmethod  #decorators 
    def info():    #static function 
        print("The H Central Library.")

    def display(self):
        print(f"The Author of book named {self.title} is {self.author} and it has {self.pages} pages.")

b1 = Book("Karnali Blues","Buddhisagar",235)
b1.info()
b1.display()

b2 = Book("Munamadan","Laxmi Prasad Devkota", 134)
b2.info()
b2.display()