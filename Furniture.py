class Furniture:
    def __init__(self):
        self._typeOfWood = "Teakwood"

class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.__numberOfLegs = 4
    def changeWood(self, typeOfWood):
        self._typeOfWood = typeOfWood
    def displayChairSpecification(self):
        print("This chair is made of {} and has {} legs.".format(self._typeOfWood, self.__numberOfLegs))
chair = Chair()
print("Would you like to chang the type of wood from Teakwood? Y/N")
userChoice = input()
if userChoice == "Y":
    print("Enter the type of wood you would like.")
    wood = input()
    chair.changeWood(wood)
chair.displayChairSpecification()
