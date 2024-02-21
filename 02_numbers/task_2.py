def calculate_acres(square_meters):
    acres = square_meters / 4047
    return acres


square_meters = float(input("Enter total square meters: "))
acres = calculate_acres(square_meters)


print(f"Number of acres on a piece of land is {acres:.3f}")
