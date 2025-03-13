def find(numbers):
    return min(numbers), max(numbers)
numbers = [10, 5, 8, 3, 15]
smallest, largest = find(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
