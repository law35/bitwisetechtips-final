#Encapsulation

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l
    
    def area(self):
        print(self.width * self.length)
        

myrectangle = Rectangle(25, 50)

print("The area of the rectangle is:")
myrectangle.area()



#Encapsulation 

class NumberList:
    def __init__(self):
        self.numbers = [2, 4, 6, 8, 10]
        
    def change_data(self, index, n):
        self.numbers[index] = n
        

new_num = NumberList()
new_num.numbers[0] = 1

#print out altered list
print(new_num.numbers)

new_num = NumberList()
new_num.change_data(0, 2)

#print out restored list
print(new_num.numbers)



#Private variables and methods vs. Public variables and methods

class PublicVsPrivate:
    def __init__(self):
        self.public = "safe to use"
        self._private = "not safe to use"
        
    def public_method(self):
        #This is ok to use
        print("It's cool; You can use this.")
        
    def _private_method(self):
        #Not ok to use
        print("Um dude, didn't I said not to use this method?")
        

myprogram = PublicVsPrivate()

myprogram.public_method()