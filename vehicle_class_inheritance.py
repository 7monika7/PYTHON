class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def mona(self):
      print(f"Brand: {self.brand}, Model: {self.model}")
class bike(Vehicle):
  def __init__(self, brand, model):
    super().__init__(brand, model)
  def mouna(self):
    super().mona()
    print(f"Seats: {self.seats}")
obj= bike("DUKE 360",2020)
obj.mona()
