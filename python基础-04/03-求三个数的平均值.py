def three_sum(a,b,c):
    result = a+b+c
    #print("%d + %d +%d = %d"%(a,b,c,result))
    return result

def average_three(a1,b1,c1):
    result = three_sum(a1,b1,c1)
    result = result/3
    print("三个数的平均值是:%d"%result)

num1 = int(input("请输入第1个数："))
num2 = int(input("请输入第2个数："))
num3 = int(input("请输入第3个数："))

#three_sum(num1,num2,num3)
average_three(num1,num2,num3)
