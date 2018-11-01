#1.打印操作提示符
#print(50*"=")
#print("   名片管理系统 VB1.1")
#print("1.添加一个新名片:")
#print("2.修改一个名片:")
#print("3.删除一个名片:")
#print("4.查找一个名片:")
#print("5.显示所有名片:")
#print("6.退出系统")
#print(50*"=")
#2.获取用户输入

idcard_infors = []
while True:
    print(50*"=")
    print("   名片管理系统 VB1.1")
    print("1.添加一个新名片:")
    print("2.修改一个名片:")
    print("3.删除一个名片:")
    print("4.查找一个名片:")
    print("5.显示所有名片:")
    print("6.退出系统")
    print(50*"=")
    num = int(input("请输入操作项:"))

#3.更具用户输入执行相应功能

    if num == 1:
       idcard = {}
       new_name = input("输入姓名:")
       new_qq = input("输入qq:")
       new_weixin = input("输入微信:")
       new_addr = input("输入地址:")
       idcard["name"] = new_name
       idcard["qq"] = new_qq
       idcard["weixin"] = new_weixin
       idcard["addr"] = new_addr
       idcard_infors.append(idcard)
       print(idcard_infors)
      # print("姓名 \t qq \t 微信 \t 地址 \t")
      # print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
    elif num == 2:
       alt_name = input("请输入被修改者姓名:")
       for temp in idcard_infors:
           if alt_name == temp["name"]:
               print(50*"*")
               print("修改提示")
               print("1.修改姓名:")
               print("2.修改qq:")
               print("3.修改微信:")
               print("4.修改地址:")
               print(50*"*")
               alt_num =  int(input("请输入需要被修改的项:"))
               if alt_num == 1:
                   alt_last_name = input("请输入被修改后的名字:")
                   temp["name"] = alt_last_name
                  # print(idcard_infors)
                   print("姓名 \t qq \t 微信 \t 地址 \t")
                   print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
               elif alt_num == 2:
                   alt_last_qq = input("请输入被修改后的qq:")
                   temp["qq"] = alt_last_qq
                  # print(idcard_infors)
                   print("姓名 \t qq \t 微信 \t 地址 \t")
                   print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
                   
               elif alt_num == 3:
                   alt_last_weixin = input("请输入被修改后的微信:")
                   temp["weixin"] = alt_last_weixin
                   print("姓名 \t qq \t 微信 \t 地址 \t")
                   print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
               elif alt_num == 4:
                   alt_last_addr = input("请输入被修改后的地址:")
                   temp["addr"] = alt_last_addr
                  # print(idcard_infors)
                   print("姓名 \t qq \t 微信 \t 地址 \t")
                   print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
               else:
                   print("输入有误，请重新输入:")
    elif num == 3:
        del_name = input("请输入被删除者姓名:")
        for temp in idcard_infors:
            if del_name == temp["name"]:
                idcard_infors.remove(temp)
                print(idcard_infors)
               # print("姓名 \t qq \t 微信 \t 地址 \t")
               # print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
    elif num == 4:
        sel_flag = 0
        sel_name = input("请输入被查找者姓名:")
        for temp in idcard_infors:
            if sel_name == temp["name"]:
                 print("姓名 \t qq \t 微信 \t 地址 \t")
                 print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
                 sel_flag = 1
        if sel_flag == 0:
            print("查无此人")


    elif num == 5:
        print("姓名 \t qq \t 微信 \t 地址 \t")
        for temp in idcard_infors:
         print("%s \t %s \t %s \t %s \t"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))


    elif num == 6:
        break
    else:
        print("输入有误，请重新输入...")
    print(" ")
