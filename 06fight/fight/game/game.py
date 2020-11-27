"""
一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp初始值1000，power初始值200
定义一个fight方法：
final_hp = hp - enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的人获胜
"""


class Game():
    #参数化传入hp, power
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, enemy_power, enemy_hp):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        print(final_hp)
        print(enemy_final_hp)
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

#将角色hp, power通过传参传入
hp = 1000
power = 200
game = Game(hp, power)
game.fight(300, 700)
