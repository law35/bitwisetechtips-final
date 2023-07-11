#Class

class Wizard:
    def __int__(self, n, bp, mp, hp):
       self.name = n
       self.health = hp
       self.mana = mp
       self.power = bp


newCharacter = Wizard()

newCharacter.name = "Gandalf"
newCharacter.mana = 1000
newCharacter.health = 800
newCharacter.power = 500

print("Name:", newCharacter.name)
print("Health:", newCharacter.health)
print("Mana:", newCharacter.mana)
print("Base Power:", newCharacter.power)


#Class Variables

class Wizard:
    health = 150
    mana = 200
    power = 98
 
    def __int__(self, n):
        self.name = n


newCharacter = Wizard()

print("Health:", newCharacter.health)


#Class Method

class Wizard:
    health = 150
    mana = 200
    power = 98
 
    def __int__(self, n):
        self.name = n
  
    def telekinetic_blast(self):
        print("50 damage dealt!")


newCharacter = Wizard()

newCharacter.telekinetic_blast()