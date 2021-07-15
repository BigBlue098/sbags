class PS:
    numPS = 0
    listOfStones = []
    def __init__(self,name):
        self.name = name
        PS.numPS += 1
        if PS.numPS<= 5:
            PS.listOfStones.append(self)
        else:
            del PS.listOfStones[0]
            PS.listOfStones.append(self)

    @staticmethod
    def displayPreciousStones():
        for stone in PS.listOfStones:
            print(stone.name, end = ' ')
        print()

stoneOne = PS("Ruby")
stoneTwo = PS("Diamond")
stoneThree = PS("Gold")
stoneFound = PS("Rock")
stoneFive = PS("Quartz")
stoneFive.displayPreciousStones()
stoneSix = PS("Aquamarine")
stoneSix.displayPreciousStones()
