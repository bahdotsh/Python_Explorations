# A class is like a blueprint for creating objects. 
# An object has properties and methods (functions) assosiated with it. Almost everything in python is an object.


# Create Class

class User:
    def __init__(self,name):
        self.name = name


# Init user object

heisenberg = User('Heisenberg')

print(heisenberg.name)