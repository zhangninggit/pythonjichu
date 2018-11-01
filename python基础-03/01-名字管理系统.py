#1.打印功能提示
print(50*"=")
print("    名字管理系统 VB1.1")
print("1:添加一个新名字")
print("2:删除一个名字")
print("3:修改一个名字")
print("4:查询一个名字")
print("5:退出")
print(50*"=")

#2.获取用户选择
names =[]
while True:
    num = int(input("请输入想要执行的操作项："))

    if num == 1:
        new_name = input("请输入添加的名字:")
        names.append(new_name)
        print(names)
    elif num == 2:
        del_name = input("请输入想要删除的名字:")
        names.remove(del_name)
        print(names)
    elif num == 3:
        old_name = input("请输入被修改的名字:")
        if old_name in names:
           a = len(names)  #获取原列表长度
           idx_name = names.index(old_name,0,a+1)#查找出被修改名字在原列表中的索引
           alt_name = input("输入新名字：")#输入新名字替换掉被修改名字
           names[idx_name] = alt_name
           print(names)
        else:
            print("此人不存在，无法删除！")
    elif num == 4:
        sel_name = input("请输入想要查找的名字:")
        if sel_name in names:
            print("名字已存在系统中...")
        else:
            print("查无此人")
    elif num == 5:
        break
    else:
        print("输入有误，请重新输入...")


#3.根据用户选择，执行相应功能

