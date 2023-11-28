import random
computer = random.randint(0,2)

player = int(input("请输入一个数据"))

if computer == 0:
    if player == 0:
        print("都是剪刀，平局")
    elif player == 1:
        print("电脑剪刀，玩家石头，玩家赢")
    else:
        print("电脑剪刀，玩家布，电脑赢")
elif computer == 1:
    if player == 0:
        print("电脑石头，玩家剪刀，电脑赢")
    elif player == 1:
        print("电脑石头，玩家石头，平局")
    else:
        print("电脑石头，玩家布，玩家赢")
elif computer == 2:
    if player == 0:
        print("电脑布，玩家剪刀，玩家赢")
    elif player == 1:
        print("电脑布，玩家石头，电脑赢")
    else:
        print("电脑布，玩家布，平局")
else:
    print()

