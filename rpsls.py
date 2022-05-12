#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
程序目的：通过自定义函数，实现RPSLS游戏，即用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克），计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果
程序作者：严诗颖
2022.5.11
"""

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    if name=="石头":
        print(0)

    elif name=="史波克":
        print(1)

    elif name=="纸":
        print(2)

    elif name=="蜥蜴":
        print(3)

    elif name=="剪刀":
        print(4)

"""
将游戏对象对应到不同的整数
"""

def number_to_name(number):
    if number == 0:
        print("石头")
        return "石头"

    elif number==1:
        print("史波克")
        return "史波克"

    elif number==2:
        print("纸")
        return "纸"

    elif number==3:
        print("蜥蜴")
        return "蜥蜴"

    elif number==4:
        print("剪刀")
        return "剪刀"

"""
将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
"""

import random
def rpsls(player_choice):
    computer=random.randint(0, 4)
    print("计算机的选择为:")
    number_to_name(computer)
    if player_choice == "石头" and computer == 3:
        print("您赢了!")

    elif player_choice == "石头" and computer == 4:
        print("您赢了！")

    elif player_choice == "石头" and computer == 0:
        print("您和计算机出的一样呢")

    elif player_choice == "石头" and computer == 1:
        print("计算机赢了！")

    elif player_choice == "石头" and computer == 2:
        print("计算机赢了！")

    elif player_choice == "史波克" and computer == 0:
        print("您赢了！")

    elif player_choice == "史波克" and computer == 4:
        print("您赢了！")

    elif player_choice == "史波克" and computer == 1:
        print("您和计算机出的一样呢")

    elif player_choice == "史波克" and computer == 2:
        print("计算机赢了！")

    elif player_choice == "史波克" and computer == 3:
        print("计算机赢了！")


    elif player_choice == "史波克" and computer == 0:
        print("您赢了！")

    elif player_choice == "纸" and computer == 1:
        print("您赢了！")

    elif player_choice == "纸" and computer == 2:
        print("您和计算机出的一样呢")

    elif player_choice == "纸" and computer == 3:
        print("计算机赢了！")

    elif player_choice == "纸" and computer == 4:
        print("计算机赢了！")


    elif player_choice == "蜥蜴" and computer == 1:
        print("您赢了！")

    elif player_choice == "蜥蜴" and computer == 2:
        print("您赢了！")

    elif player_choice == "蜥蜴" and computer == 3:
        print("您和计算机出的一样呢")

    elif player_choice == "蜥蜴" and computer == 0:
        print("计算机赢了！")

    elif player_choice == "蜥蜴" and computer == 4:
        print("计算机赢了！")


    elif player_choice == "剪刀" and computer == 2:
        print("您赢了！")

    elif player_choice == "剪刀" and computer == 3:
        print("您赢了！")

    elif player_choice == "剪刀" and computer == 4:
        print("您和计算机出的一样呢")

    elif player_choice=="剪刀" and computer ==0:
        print("计算机赢了！")

    elif player_choice=="剪刀" and computer ==1:
        print("计算机赢了！")
    else:
        print("Error: No Correct Name")

"""
用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
"""

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")#编辑游戏开始背景文字
player_choice=input("")
rpsls(player_choice)


