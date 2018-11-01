import random

player = int(input("请输入0石头,1剪刀,2布："))

if player == 0 or player == 1 or player == 2:
   
    computer = random.randint(0,2)

    if computer ==0:
        print("电脑玩家出的是:石头")
    elif computer ==1:
        print("电脑玩家出的是:剪刀")
    else:
        print("电脑玩家出的是:布")


    if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("哈哈，我赢了...")
    elif player == computer:
        print("emmm 打成了平局...")
    else:
        print("呜呜，输了不开心～～～")
        
else:    
    print("输入的数字有误，请重新输入...")
    exit()

