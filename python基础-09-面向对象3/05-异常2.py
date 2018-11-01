try:
    #11/0
    #open("xxx.txt")
    #print(num)
    print("-----1------")

except (NameError,FileNotFoundError):
    #print("捕获到异常：")
    print("异异常统一按照如下方式处理")
except Exception as ret:
    print("如果用了Exception，之前没有捕获到的异常，在这个except中一定会捕获到...")
    print(ret)
finally:
    print("无论之前的代码有没有产生异常都会执行finally")
#else:
   # print("没有异常时打印该语句")
#except FileNotFoundError:
   # print("文件不存在.....")
print("---2------")

