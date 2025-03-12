def sum_of_evens(start, end):
    return sum(num for num in range(start, end + 1) if num % 2 == 0)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Sum of even numbers from {start} to {end}: {sum_of_evens(start, end)}")
