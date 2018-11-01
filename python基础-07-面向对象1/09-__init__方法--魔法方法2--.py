class Cat:
    #属性

    #方法
    #初始化对象
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age

    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝可乐...")

    def introduce(self):
        print("%s的年龄是:%d"%(self.name,self.age))


#创建一个对象

tom = Cat("汤姆",44)
tom.eat()
tom.drink()
#tom.name = "汤姆"
#tom.age = 40
tom.introduce()

lanmao = Cat("懒猫",20)
#lanmao.name = "蓝猫"
#lanmao.age = 15
lanmao.introduce()

