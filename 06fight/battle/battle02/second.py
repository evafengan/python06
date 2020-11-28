"""
1.第二个角色houyi，继承了角色的hp，power
2. houyi_hp = hp + defense - enemy_power
"""
from battle.battle01.first import first


class HouYi(first):
    def __init__(self, defense):
        super().__init__(self)
        self.defense = defense

    def second(self):
        myhp = self.hp + self.defense - self.enemy_power
        enemyhp = self.hp - self.my_power
        if myhp > enemyhp:
            print("我赢了")
        elif myhp < enemyhp:
            print("敌人赢了")
        else:
            print("平局")

houyi = HouYi(366)
houyi.second()