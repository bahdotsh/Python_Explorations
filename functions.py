# A function is a block of code which only runs when it is called. In python we donot use curly braces, we use indendation with tabs or spaces

# Create function

def sayHello(name):
    print(f'Hello {name}')

sayHello('John Wick')

# Return values

def getSum(num1, num2):
    x = num1+num2
    return x

a = getSum(1, 3)
print(a)



# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression. 

getSome = lambda num1, num2 : num1 + num2

b = getSome(1, 3)
print(b)