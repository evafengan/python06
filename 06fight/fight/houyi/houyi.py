"""
1.第二个角色houyi，继承了角色的hp，power
2. houyi_hp = hp + defense - enemy_power
"""
from game.game import Game


class HouYi(Game):
    def __init__(self, defense):
        super().__init__(1000, 100)
        self.defense = defense

    def houyi_fight(self, enemy_power, enemy_hp):
        while True:
            myhp = self.hp + self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(self.defense)
            print(enemy_power)
            print("我的血值：%d" % myhp)
            print("敌人血值：%d" % enemy_hp)
            if myhp > enemy_hp:
                print("我赢了")
                break
            elif myhp < enemy_hp:
                print("敌人赢了")
                break
            else:
                raise Exception("平局是异常")


enemy_hp = 2000
enemy_power = 222
defense = 20
houyi = HouYi(defense)
houyi.houyi_fight(enemy_power, enemy_hp)