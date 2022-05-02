# Craps is a game played with a pair of dice. In the game of craps, the shooter (the player with the dice) rolls a pair 
# of dice and the number of spots showing on the two upward faces are added up. If the opening roll (called the 'coming out roll') is a 7 or 11, 
# the shooter wins the game. If the opening roll results in a 2 (snake eyes), 3 or 12 (box cars), the shooter loses, otherwise known as 'crapping out'.
#  If the shooter rolls a 4, 5, 6, 8, 9 or 10 on the opening roll, then he or she must roll the same number before rolling a 7 to win the game. 
# For example, if the shooter rolls a 6 on the come out roll, a 10 on the second roll and a 7 on the third roll, the shooter loses since he
#  rolled a 7 before rolling another 6. If, however, he rolled a 6 on the third roll, he wins the game.

import random


class Dice:
    def rool(self):
        return random.randint(1, 6)


class Checker:

    def check(self, history: list[int]) -> int:
        """1: Shooter won, -1: Shooter loose, 0: Ask for another round"""

        if len(history) == 0:
            return 0

        first_shoot = history[0]
        last_shoot = history[-1]

        if first_shoot in (7,11):
            return 1
        if first_shoot in (2, 3, 12):
            return -1
        if len(history) == 1:
            return 0
        if last_shoot == first_shoot:
            return 1
        if last_shoot == 7:
            return -1
        return 0


class Craps:
    def __init__(self) -> None:
        self.dice = Dice()
        self._checker = Checker()
        self._rows = []
    
    def shoot(self):
       row = self.dice.rool() + self.dice.rool()
       self._rows.append(row)
       self._check_round()

    def new_game(self):
        self._rows = []

    def _check_round(self):
        result = self._checker.check(self._rows)
        print(f"Last row sum was {self._rows[-1]}")

        if (result == 0):
            print("Shoot again")
        if (result == -1):
            print("You loose.")
        if (result == 1):
            print("You win!")
        