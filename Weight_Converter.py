weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit=='l' or unit=='L':
    conversion = float(weight) * 0.453592
    print(f"You are {conversion} kg")
elif unit=='k' or unit=='K':
    conversion = float(weight) * 2.20462
    print(f"You are {conversion} pounds")
else:
    print("Invalid unit. Please enter 'l or L' for pounds or 'k or K' for kilograms.")

