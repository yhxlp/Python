#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
����Ŀ�ģ�ͨ���Զ��庯����ʵ��RPSLS��Ϸ�����û�ͨ��������������һ��ѡ��ʯͷ/����/��/����/ʷ���ˣ���������Զ�����һ�����ѡ�񣬸���RPSLS���򣬲������յĽ��
�������ߣ���ʫӱ
2022.5.11
"""

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=="ʯͷ":
        print(0)

    elif name=="ʷ����":
        print(1)

    elif name=="ֽ":
        print(2)

    elif name=="����":
        print(3)

    elif name=="����":
        print(4)

"""
����Ϸ�����Ӧ����ͬ������
"""

def number_to_name(number):
    if number == 0:
        print("ʯͷ")
        return "ʯͷ"

    elif number==1:
        print("ʷ����")
        return "ʷ����"

    elif number==2:
        print("ֽ")
        return "ֽ"

    elif number==3:
        print("����")
        return "����"

    elif number==4:
        print("����")
        return "����"

"""
������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
"""

import random
def rpsls(player_choice):
    computer=random.randint(0, 4)
    print("�������ѡ��Ϊ:")
    number_to_name(computer)
    if player_choice == "ʯͷ" and computer == 3:
        print("��Ӯ��!")

    elif player_choice == "ʯͷ" and computer == 4:
        print("��Ӯ�ˣ�")

    elif player_choice == "ʯͷ" and computer == 0:
        print("���ͼ��������һ����")

    elif player_choice == "ʯͷ" and computer == 1:
        print("�����Ӯ�ˣ�")

    elif player_choice == "ʯͷ" and computer == 2:
        print("�����Ӯ�ˣ�")

    elif player_choice == "ʷ����" and computer == 0:
        print("��Ӯ�ˣ�")

    elif player_choice == "ʷ����" and computer == 4:
        print("��Ӯ�ˣ�")

    elif player_choice == "ʷ����" and computer == 1:
        print("���ͼ��������һ����")

    elif player_choice == "ʷ����" and computer == 2:
        print("�����Ӯ�ˣ�")

    elif player_choice == "ʷ����" and computer == 3:
        print("�����Ӯ�ˣ�")


    elif player_choice == "ʷ����" and computer == 0:
        print("��Ӯ�ˣ�")

    elif player_choice == "ֽ" and computer == 1:
        print("��Ӯ�ˣ�")

    elif player_choice == "ֽ" and computer == 2:
        print("���ͼ��������һ����")

    elif player_choice == "ֽ" and computer == 3:
        print("�����Ӯ�ˣ�")

    elif player_choice == "ֽ" and computer == 4:
        print("�����Ӯ�ˣ�")


    elif player_choice == "����" and computer == 1:
        print("��Ӯ�ˣ�")

    elif player_choice == "����" and computer == 2:
        print("��Ӯ�ˣ�")

    elif player_choice == "����" and computer == 3:
        print("���ͼ��������һ����")

    elif player_choice == "����" and computer == 0:
        print("�����Ӯ�ˣ�")

    elif player_choice == "����" and computer == 4:
        print("�����Ӯ�ˣ�")


    elif player_choice == "����" and computer == 2:
        print("��Ӯ�ˣ�")

    elif player_choice == "����" and computer == 3:
        print("��Ӯ�ˣ�")

    elif player_choice == "����" and computer == 4:
        print("���ͼ��������һ����")

    elif player_choice=="����" and computer ==0:
        print("�����Ӯ�ˣ�")

    elif player_choice=="����" and computer ==1:
        print("�����Ӯ�ˣ�")
    else:
        print("Error: No Correct Name")

"""
�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
"""

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")#�༭��Ϸ��ʼ��������
player_choice=input("")
rpsls(player_choice)


