#Inheritance

class Jedi():
    def __init__(self, s, a, n):
        self.sex = s
        self.age = a
        self.name = n

    def force_push(self):
        print("I know how to use Force-Push.")
    
    def shii_cho(self):
        print("I know Form 1 of lightsaber combat.")
  
   

class Padawan(Jedi):
    def shii_cho(self): 
        #This method will override the method in the Jedi class.
        print("I surpassed my peers in this form!")
    

my_padawan = Padawan("male", 15, "Anakin")

print("My name is", my_padawan.name)
my_padawan.force_push()
my_padawan.shii_cho()

