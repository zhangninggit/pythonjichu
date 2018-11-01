class Dog:
    
    def __init__(self,new_name):
        self.name = new_name
        self.__age = 0 #定义了一个私有的属性，属性名为__age

    def set_age(self,new_age):
        if new_age >0 and new_age <=100:
             self.__age = new_age
        else:
            self.__age = 0
    
    def get_age(self):
        return self.__age


dog = Dog("小白")

dog.set_age(-10)
age = dog.get_age()
print(age)


#print(dog.__age)

#dog.get_age()
