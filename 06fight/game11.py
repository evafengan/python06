"""
一个回合制游戏，每个角色都有hp和power，hp代表血量，power代表攻击力，hp初始值1000，power初始值200
定义一个fight方法：
final_hp = hp - enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的人获胜
"""

# class Game():
#     hp = 1000
#     power = 20
#
#
#     def fight(self,enemy_hp,enemy_power):
#         final_hp =  self.hp - enemy_power
#         enemy_final_hp = enemy_hp - self.power
#         if final_hp > enemy_final_hp:
#             print("我赢了")
#         elif final_hp < enemy_final_hp:
#             print("敌人赢了")
#         else:
#             print("平局")
#
#
# game = Game()
# game.fight(1000,300)

"""
优化
1.将角色hp, power通过传参传入
2.第二个角色houyi，继承了角色的hp，power
3. houyi_hp = hp + defense - enemy_power
"""


class Game():
    # 将角色hp,power通过传参传入
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        while True:
            if final_hp > enemy_final_hp:
                print("我赢了")
                break
            elif final_hp < enemy_final_hp:
                print("敌人赢了")
                break
            else:
                print("平局")

#继承game类
class HouYi(Game):

    #如果在子类中重新定义了__init__，那么父类的__init__会被覆盖
    def __init__(self):
        #把父类的__init__参数继承过来
        super().__init__(1000, 200)
        self.defense = 100

    def houyi_fight(self, enemy_hp, enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            #抛异常
            raise Exception("平局是异常")






# 传参给hp, power
hp = 1000
power = 200
game = Game(hp, power)

game.fight(1000,200)
