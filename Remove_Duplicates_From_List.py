numbers = [3, 7, 9, 3, 8, 7]
uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)