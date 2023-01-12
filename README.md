# Zombie Dice Bots

## A series of bots used to play the Zombie Dice game Built with Python using the zombiedice module installed with pip and Python's Standard Library random module

1. A bot that, after the first roll, randomly decides if it will continue
or stop
2. A bot that stops rolling after it has rolled two brains
3. A bot that stops rolling after it has rolled two shotguns
4. A bot that initially decides it’ll roll the dice one to four times, but will
stop early if it rolls two shotguns
5. A bot that stops rolling after it has rolled more shotguns than brains

### About the Game

Zombie Dice is a quick, fun dice game from Steve Jackson Games. The
players are zombies trying to eat as many human brains as possible without
getting shot three times. There is a cup of 13 dice with brains, footsteps,
and shotgun icons on their faces. The dice icons are colored, and each
color has a different likelihood of each event occurring. Every die has two
sides with footsteps, but dice with green icons have more sides with brains,
red-icon dice have more shotguns, and yellow-icon dice have an even split of
brains and shotguns.

### Rules of the Game

1. Place all 13 dice in the cup. The player randomly draws three dice from
the cup and then rolls them. Players always roll exactly three dice.
2. They set aside and count up any brains (humans whose brains were
eaten) and shotguns (humans who fought back). Accumulating three
shotguns automatically ends a player’s turn with zero points (regardless
of how many brains they had). If they have between zero and two shotguns, they may continue rolling if they want. They may also choose to
end their turn and collect one point per brain.
3. If the player decides to keep rolling, they must reroll all dice with
footsteps. Remember that the player must always roll three dice; they
must draw more dice out of the cup if they have fewer than three footsteps to roll. A player may keep rolling dice until either they get three
shotguns—losing everything—or all 13 dice have been rolled. A player
may not reroll only one or two dice, and may not stop mid-reroll.
4. When someone reaches 13 brains, the rest of the players finish out the
round. The person with the most brains wins. If there’s a tie, the tied
players play one last tiebreaker round.