"""
一个回合制游戏，2个角色都有hp和power
myhp = hp - enemy_power
enemyhp = hp - my_power

"""


class First():
    hp = 2000

    def __init__(self, enemy_power, my_power):
        self.enemy_power = enemy_power
        self.my_power = my_power


    def first_battle(self):
        for i in range(1, 10):

            myhp = self.hp - self.enemy_power
            enemyhp = self.hp - self.my_power
            if myhp > enemyhp:
                print("我赢了！！\n我的血值：%d,\n敌人的血值：%d" % (myhp, enemyhp))
            elif myhp < enemyhp:
                print("敌人赢了\n我的血值：%d,\n敌人的血值：%d" % (myhp, enemyhp))
            else:
                raise Exception("平局异常")

enemy_power = int(input("请输入敌人的攻击力："))
my_power = int(input("请输入我的攻击力："))
first = First(enemy_power, my_power)
first.first_battle()