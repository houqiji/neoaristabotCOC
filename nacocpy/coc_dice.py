import random as rm


class CocDice:
    """
    This is a class contain different dices, and record using time of each dices

    Before use this dice, pass your QQ id into the dice_user(str) to avoid one
    user have more than one dice logger.

    Args:
        dice_user(str): The user of dice, to fit qq-bot api
        dice_time(class DiceTime): The class of using time of dices
    """

    class DiceTime:
        """
        This is a class record using time of dices

        Args:
            td4(int):   use time of D4 dice
            td5(int):   use time of D5 dice
            td6(int):   use time of D6 dice
            td8(int):   use time of D8 dice
            td10(int):  use time of D10 dice
            td12(int):  use time of D12 dice
            td20(int):  use time of D20 dice
            td30(int):  use time of D30 dice
            td100(int): use time of D100 dice
        """

        def __init__(self, td4=0, td5=0, td6=0, td8=0, td10=0, td12=0, td20=0, td30=0, td100=0):
            self.td4 = td4
            self.td5 = td5
            self.td6 = td6
            self.td8 = td8
            self.td10 = td10
            self.td12 = td12
            self.td20 = td20
            self.td30 = td30
            self.td100 = td100

    def __init__(self, dice_user, dice_time=DiceTime()):
        self.dice_time = dice_time
        self.dice_user = dice_user

    def d4(self):
        self.dice_time.td4 += 1  # Dice time recorder
        return rm.randint(1, 4)  # Pick a random integer in [1,4]

    def d5(self):
        self.dice_time.td5 += 1
        return rm.randint(1, 5)

    def d6(self):
        self.dice_time.td6 += 1
        return rm.randint(1, 6)

    def d8(self):
        self.dice_time.td8 += 1
        return rm.randint(1, 8)

    def d10(self):
        self.dice_time.td10 += 1
        return rm.randint(1, 10)

    def d12(self):
        self.dice_time.td12 += 1
        return rm.randint(1, 12)

    def d20(self):
        self.dice_time.td20 += 1
        return rm.randint(1, 20)

    def d30(self):
        self.dice_time.td30 += 1
        return rm.randint(1, 30)

    def d100(self):
        self.dice_time.td100 += 1
        return rm.randint(1, 100)
