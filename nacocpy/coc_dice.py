import random as rm


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


class CocDice:
    """
    coc_dice.CocDice()
    此类包含了不同类型的骰子，并且能够监控每个骰子的使用次数
    This is a class contain different dices, and record using time of each dices

    使用骰子之前传入QQid参数以便生成个人日志
    Before use this dice, pass your QQ id into the dice_user(str) to avoid one
    user have more than one dice logger.

    Args:
        dice_user(str): 骰子用户，与qq-bot api 适应 / The user of dice, to fit qq-bot api
        dice_time(class DiceTime): 使用次数类 / The class of using time of dices
    """

    dice_user = DiceTime()

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


def random_divide(divide_num, divide_part):
    if type(divide_num) == int and type(divide_part) == int \
            and divide_num >= 0 and divide_part >= 0 and divide_num <= divide_part:
        return AttributeError
    else:
        divide_list = []
        for i in range(divide_part):
            divide_list += [1]
            print(divide_list)
        divide_num -= divide_part
        for i in range(divide_part - 1):
            rand = rm.randint(0, divide_part - 1)
            divide_list[rand] += 1
            print(divide_list)
