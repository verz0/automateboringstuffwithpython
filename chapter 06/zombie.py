import zombiedice

class MyZombie:
    def __init__(self, name):

        self.name = name

    def turn(self, gameState):


        diceRollResults = zombiedice.roll() 

        
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() 
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    
)


zombiedice.runWebGui(zombies=zombies, numGames=1000)