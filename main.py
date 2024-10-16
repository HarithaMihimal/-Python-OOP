class Microwave:
    def __init__(self,brand:str,power_rating:str)->None:
        self.brand=brand
        self.power_rating=power_rating

        

smeg:Microwave= Microwave(brand="Smeg",power_rating="1000W")

print(smeg)
print(smeg.brand)
print(smeg.power_rating)
