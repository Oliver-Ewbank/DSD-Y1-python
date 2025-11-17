weight_kg = float(input("what is your weight in kg"))
height_m = float(input("what is your height in M"))

bmi = weight_kg / (height_m * 2)

if bmi < 18.5:
    print("you are underweight")
elif bmi > 18.5 and bmi < 25:
    print("you are healthy")
elif bmi > 25 and bmi < 30:
    print("you are overweight")
elif bmi > 30:
    print("you are obese")