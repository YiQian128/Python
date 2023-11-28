import random
computer = random.randint(1 , 100)

flag = True
count = 0
while flag:
    player = int(input("请输入一个1-100的数字："))
    count += 1
    if player == computer:
        print(f"猜对了,您猜了{count}次")
        flag = False
    else:
        if player > computer:
            print("您猜的大了")
        else:
            print("您猜的小了")
