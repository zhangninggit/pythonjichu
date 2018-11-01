class Dog(object):
    
    __instaance = None

    def __new__(cls):
        if cls.__instaance == None:
            cls.__instaance = object.__new__(cls)
            return cls.__instaance
        else:
            return cls.__instaance


a = Dog()
print(id(a))
b = Dog()
print(id(b))
