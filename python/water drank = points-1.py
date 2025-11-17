water_drank = int(input("how much water have you drank today"))

points = water_drank / 250
if water_drank > 2000:
    points = points + 5

print("you have a total of", points, "points")