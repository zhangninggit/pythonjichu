class Dog(object):
    
    __instaance = None
    __init_flag = False
    def __new__(cls,name):
        if cls.__instaance == None:
            cls.__instaance = object.__new__(cls)
            return cls.__instaance
        else:
            return cls.__instaance
    
    def __init__(self,name):
        if self.__init_flag == False:
            self.name = name
            self.__init_flag = True    
a = Dog("旺财")
print(id(a))
print(a.name)

b = Dog("哮天犬")
print(id(b))
print(b.name)
