class Cat:
    #属性

    #方法
    #初始化对象
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
        
    def __str__(self):
        return "%s的年龄是：%d"%(self.name,self.age)

    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝可乐...")

    def introduce(self):
        print("%s的年龄是:%d"%(self.name,self.age))


#创建一个对象

tom = Cat("汤姆",44)
lanmao = Cat("懒猫",20)

print(tom)
print(lanmao)
