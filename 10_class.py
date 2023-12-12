class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("喵"*self.age)
        
class CuteCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        print("喵~"*self.age)
    
    def name():
        return super().name
        
c = CuteCat("miaomiao", 18)
print(c.name)
c.speak()
