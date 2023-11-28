import random

player = int(input("请输入：剪刀（0），石头（1），布（2）："))
computer = random.randint(0,2)

if player ==0: # 如果我是剪刀的话
    if computer==0:
        print("平局哦，我是剪刀")
    elif computer==1:
        print("你输了哦，我是石头")
    else:
        print("你赢了哦，我是布")

elif player==1: # 如果我是石头的话
    if computer==0:
        print("你赢了哦，我是剪刀")
    elif computer==1:
        print("平局哦，我是石头")
    else:
        print("你输了哦，我是布")


elif player==2 : # 如果我是布的话
    if computer== 0:
        print("你输了哦，我是剪刀")
    elif computer==1:
        print("你赢了哦,我是石头")
    else:
        print("平局哦，我是布")


else:
    print("请输入规定的数字哦")