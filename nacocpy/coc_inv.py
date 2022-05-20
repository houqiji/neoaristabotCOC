import coc_dice as cdi
import math


class Investigator:
    class Attribute:
        def __init__(self, STR=0, CON=0, SIZ=0, DEX=0, APP=0, INT=0, POW=0, EDU=0, DAM=0, PHY=0, MOV=0, lucky=0,
                     health=0):
            self.STR = STR
            self.CON = CON
            self.SIZ = SIZ
            self.DEX = DEX
            self.APP = APP
            self.INT = INT
            self.POW = POW
            self.EDU = EDU
            self.DAM = DAM
            self.PHY = PHY
            self.MOV = MOV
            self.lucky = lucky
            self.health = health

    class Occupation:
        def __init__(self, a):
            self.a = a

    def __init__(self, user_id, difficult, age, Attr=Attribute()):
        self.user_id = user_id
        self.Attr = Attr
        self.dice = cdi.CocDice(user_id)
        self.difficult = difficult
        self.age = age

    def roll_attribute(self):
        # change with difficult
        if self.difficult == 0:
            d = 1
        elif self.difficult == 1:
            d = 0.5
        elif self.difficult == 2:
            d = 0.2
        # STR       3D6*5
        self.Attr.STR = math.floor((self.dice.d6() + self.dice.d6() + self.dice.d6()) * 5 * d)
        # CON       3D6*5
        self.Attr.CON = math.floor((self.dice.d6() + self.dice.d6() + self.dice.d6()) * 5 * d)
        # SIZ       2D6+6*5
        self.Attr.SIZ = math.floor((self.dice.d6() + self.dice.d6() + 6) * 5 * d)
        # DEX       3D6*5
        self.Attr.DEX = math.floor((self.dice.d6() + self.dice.d6() + self.dice.d6()) * 5 * d)
        # APP       3D6*5
        self.Attr.APP = math.floor((self.dice.d6() + self.dice.d6() + self.dice.d6()) * 5 * d)
        # INT       2D6+6*5
        self.Attr.INT = math.floor((self.dice.d6() + self.dice.d6() + 6) * 5 * d)
        # POW       3D6*5
        self.Attr.POW = math.floor((self.dice.d6() + self.dice.d6() + self.dice.d6()) * 5 * d)
        # EDU       2D6+6*5
        self.Attr.EDU = math.floor((self.dice.d6() + self.dice.d6() + 6) * 5 * d)
        # lucky     3D6*5
        self.Attr.lucky = math.floor((self.dice.d6() + self.dice.d6() + self.dice.d6()) * 5 * d)
        # DAM and PHY
        if self.Attr.SIZ + self.Attr.STR <= 64:
            self.Attr.DAM = -2
            self.Attr.PHY = -2
        elif self.Attr.SIZ + self.Attr.STR <= 84:
            self.Attr.DAM = -1
            self.Attr.PHY = -1
        elif self.Attr.SIZ + self.Attr.STR <= 124:
            self.Attr.DAM = 0
            self.Attr.PHY = 0
        elif self.Attr.SIZ + self.Attr.STR <= 164:
            self.Attr.DAM = self.dice.d4()
            self.Attr.PHY = 1
        elif self.Attr.SIZ + self.Attr.STR <= 204:
            self.Attr.DAM = self.dice.d6()
            self.Attr.PHY = 2
        elif self.Attr.SIZ + self.Attr.STR <= 284:
            self.Attr.DAM = self.dice.d6() + self.dice.d6()
            self.Attr.PHY = 3
        elif self.Attr.SIZ + self.Attr.STR <= 364:
            self.Attr.DAM = self.dice.d6() + self.dice.d6() + self.dice.d6()
            self.Attr.PHY = 4
        elif self.Attr.SIZ + self.Attr.STR <= 444:
            self.Attr.DAM = self.dice.d6() + self.dice.d6() + self.dice.d6() + self.dice.d6()
            self.Attr.PHY = 5
        else:
            self.Attr.DAM = self.dice.d6() + self.dice.d6() + self.dice.d6() + self.dice.d6() + self.dice.d6()
            self.Attr.PHY = 6
        # MOV
        if self.Attr.DEX < self.Attr.SIZ and self.Attr.STR < self.Attr.SIZ:
            self.Attr.MOV = 7
        elif self.Attr.DEX >= self.Attr.SIZ or self.Attr.STR >= self.Attr.SIZ:
            self.Attr.MOV = 8
        else:
            self.Attr.MOV = 9

        if 49 > self.age > 39:
            self.Attr.MOV -= 1
        elif 59 > self.age:
            self.Attr.MOV -= 2
        elif 69 > self.age:
            self.Attr.MOV -= 3
        elif 79 > self.age:
            self.Attr.MOV -= 4
        elif 89 > self.age:
            self.Attr.MOV -= 5


inv = Investigator('10000000', 0, 28)
inv.roll_attribute()

print('STR', inv.Attr.STR)
print('CON', inv.Attr.CON)
print('SIZ', inv.Attr.SIZ)
print('DEX', inv.Attr.DEX)
print('APP', inv.Attr.APP)
print('INT', inv.Attr.INT)
print('POW', inv.Attr.POW)
print('EDU', inv.Attr.EDU)
print('DAM', inv.Attr.DAM)
print('PHY', inv.Attr.PHY)
print('MOV', inv.Attr.MOV)
print('lucky', inv.Attr.lucky)
print('health', inv.Attr.health)
print('age', inv.age)
