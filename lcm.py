def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
