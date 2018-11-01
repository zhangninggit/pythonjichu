class Dog(object):
    def print_self(self):
        print("大家好，我是XXX,希望以后大家多多关照")

class Xiaotq(Dog):
    def print_self(self):
        print("hello everybody, 我是你们的老大，我是xxxx")

def introduce(temp):   #单独写个自我介绍函数
    temp.print_self()



dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)

