class NegativeNumberError(Exception):
  pass
  def cp(number):
    if number < 0:
      raise NegativeNumberError("Negative number entered.")
try:
  num = int(input("Enter a positive number: "))
  cp(num)
  print("You entered a positive number.")
except NegativeNumberError as e:
  print(e)
