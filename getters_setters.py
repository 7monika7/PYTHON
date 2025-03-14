class Person:
    def __init__(self, name, age):
        self._name = name 
        self._age = age  
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name  
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        if new_age > 0: 
            self._age = new_age
        else:
            print("Age must be positive")
p = Person("Alice", 25)
print(p.get_age())
p.set_name("Bob") 
p.set_age(30)   
print(p.get_name())  
print(p.get_age())   
