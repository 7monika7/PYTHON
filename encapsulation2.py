class car:
  def __init__(self,brand,model,color):
    self.brand=brand
    self.model=model
    self.color=color
  def happy(self):
    print(f"car's brand is {self.brand}")
    print(f"car's model is {self.model}")
    print(f"car's color is {self.color}")
obj=car("audi","a6","black")
obj.happy()
  
