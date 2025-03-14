class animal:
  def __init__(self,kind,name,age):
    self.kind=kind
    self.name=name
    self.age=age
  def happy(self):
    print(f"animal's kind is {self.kind}")
    print(f"animal's name is {self.name}")
    print(f"animal's age is {self.age}")
obj=animal("dog","max",5)
obj.happy()
