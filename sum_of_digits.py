def sum_of_digits(n):
 return sum(int(digit) for digit in str(abs(n)))
num=12345
print(sum_of_digits(num))
