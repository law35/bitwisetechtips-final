#Polymorphism in a class

class SuperMan():
    def bio(self):
        print("Superman is a hero from krypton and sworn protector of Earth.")
    
    def location(self):
        print("Location:", "Metropolis")
    
    def powers_and_abilities(self):
        print("Powers and Abilities:",
            "Super strength", 
            "speed,", 
            "endurance,", 
            "hearing,", 
            "heat vision,", 
            "flight")
 
    def hero_type(self):
        print("Alien")
        
   

class BatMan():
    def bio(self):
        print("Batman wages a neverending war on crime in the name of his murdered parents.")
    
    def location(self):
        print("Location:", "Gotham City")
   
    def powers_and_abilities(self):
        print("Powers and Abilities:", 
            "Peak physical condition,",
            "Master hand-to-hand combatant,",
            "Genius level intellect,",
            "Detective skills,",
            "Expert tactician,",
            "Escape artist,",
            "Billionaire Tech Business-man")
    
    def hero_type(self):
        print("Vigilante")
        

the_boyscout = SuperMan()
the_bat = BatMan()

for hero in (the_boyscout, the_bat):
    hero.bio()
    hero.location()
    hero.powers_and_abilities()
