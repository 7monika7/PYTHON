class circle:
  def __init__(self,radious):
    self.radious=radious
  def area(self):
    return 3.14*self.radious*self.radious
obj=circle(4)
print("area of circle is ",obj.area())
