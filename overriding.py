class parent:
  def hello(self):
    print("i'm base class")
class child(parent):
  def hello(self):
    print("i'm derived class")
obj=child()
obj.hello()
