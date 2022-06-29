class Hero:
    def __init__(self, name, healt):
        self.name = name
        self.healt = healt
        
    def defend(self, damage):
        self.healt -= damage
        
        if self.healt <= 0:
            self.healt = 0
            return f"{self.name} was defeated"
        
    
    def heal(self, amout):
        self.healt += amout
       
    


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

                    
                    
                    
                    
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     