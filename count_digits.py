def count_digits(n):
    return len(str(abs(n)))

num = int(input("Enter an integer: "))
print(f"The number of digits in {num} is: {count_digits(num)}")
