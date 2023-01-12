import zombiedice
from random import choice

class MyZombie():
    """Represents a zombie bot that stops continues rolling until the number of brains reaches 2"""

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        dice_roll_results = zombiedice.roll()

        brains = 0

        while not(dice_roll_results == None):
            brains += dice_roll_results['brains']

            if brains < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break

choices = ('y', 'n')

class MyRandomZombie():
    """Represents a zombie that continues rolling based randomly"""
    
    def __init__(self, name):
        # Initialise the zombies name attribute
        self.name = name

    def turn(self, gameState):
        # The zombie plays
        dice_roll_results = zombiedice.roll()

        keep_rolling = choice(choices)

        while not(dice_roll_results == None):
            if keep_rolling == 'y':
                dice_roll_results = zombiedice.roll()
                keep_rolling = choice(choices)
            else:
                break

class MyTwoBrainZombie():
    """Represents a zombie that stops rolling after eating two brains"""

    def __init__(self, name):
        # Initialise the zombie's name
        self.name = name

    def turn(self, gameState):
        # The zombie plays bot the game
        dice_roll_results = zombiedice.roll()

        brains = 0

        while not(dice_roll_results == None):
            brains += dice_roll_results['brains']

            if brains < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break

class MyTwoShotsZombie():
    """Represents a zombie that stops rolling after getting 2 shotguns"""

    def __init__(self, name):
        # Initialise the zombie's name
        self.name = name

    def turn(self, gameState):
        # The zombie bot plays it's turn

        dice_roll_results = zombiedice.roll()

        shotguns = 0

        while not(dice_roll_results == None) and (shotguns < 2):
            shotguns += dice_roll_results['shotgun']

            # if shotgun < 2:
            dice_roll_results = zombiedice.roll()
            # else:
            #     break

class MyWiseZombie():
    """Represents a zombie that will roll the dice 1 to 4 times but stops if it gets 2 shotguns"""

    def __init__(self, name):
        # Initialise the zombie's name attribute
        self.name = name

    def turn(self, gameState):
        # Simulates the zombie playing
        count = 0
        shotguns = 0
        dice_roll_results = {'shotgun': 0}

        while not(dice_roll_results == None) and (shotguns < 2) and (count < 4):
            # keep counting the number of times the zombie has rolled and checking if its has 2 shotguns yet
            dice_roll_results = zombiedice.roll()
            shotguns += dice_roll_results['shotgun']
            count += 1


class TacticsZombie(MyZombie):
    """Represents a zombie that rolls until the number of shotguns accumulated is more than the number of brains"""

    def __init__(self, name):
        # Initialises the zombies name from the parent class
        super().__init__(name)
    
    def turn(self, gameState):
        # Simulates the zombie playing it's turn
        dice_roll_results = zombiedice.roll()
        shotguns = 0
        brains = 0

        while not(dice_roll_results == None) and (brains >= shotguns):
            # stop rolling if the num of shotguns is greater than num of brains
            shotguns += dice_roll_results['shotgun']
            brains += dice_roll_results['brains']
            dice_roll_results = zombiedice.roll()


zombies = (
 zombiedice.examples.RandomCoinFlipZombie(name='Random'),
 zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
 zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
 zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
 MyRandomZombie('Zombozo'),
 MyTwoBrainZombie('Toolie'),
 MyTwoShotsZombie('Termay'),
 MyWiseZombie('WisBrain'),
 TacticsZombie('Sabinus')
)

#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)