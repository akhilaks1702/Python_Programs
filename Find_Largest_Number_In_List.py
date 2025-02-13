numbers = [2, 8, 13, 8888, 21]
big = numbers[0]
for number in numbers:
    if number > big:
        big = number
print(f"Largest number in the list: {big}")