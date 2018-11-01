#coding=utf-8
def test(a,b,func):
    result = func(a,b)
    return result

func_new = input("请输入一个匿名函数:")

num = test(11,22,func_new)
print(num)
