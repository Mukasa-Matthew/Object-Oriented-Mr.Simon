


class Person:
    def __init__(self, Fname, christianname, other):
##self. name this changes to anything, its not fixed 
        self.name = christianname
        self.Familyname = Fname
        self.other = other





##book class with author title and year

class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

##create an instance of the book class
book1 = Book("John Doe", "The Great Gatsby", 1925)


