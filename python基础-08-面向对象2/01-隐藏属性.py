class Dog:
    
    def set_age(self,new_age):
        if new_age >0 and new_age <=100:
             self.age = new_age
        else:
            self.age = 0
    def get_age(self):
        print(self.age)


dog = Dog()

dog.set_age(-10)

dog.get_age()
