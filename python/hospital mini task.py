def unitchange():
    MGDL_RATE = 0.0555
    MMOLL_RATE = 18.018
    print("Was your test glucose or cholesterol")
    typechecker = input("Enter your decision here: ")
    result = input("what was the result")
    def convert():
        unit = input("was your test in mg/dl or mmol/L")
        if unit.lower() == "mg/dl":
            conversion = float(result) * MGDL_RATE
            return conversion
        elif unit.lower() == "mmol/L":
            conversion = float(result) * MMOLL_RATE
            return conversion
        else:
            print("please enter a valid number")
            convert()
    conversion = convert()
    print(conversion)


temp_1 = float(input("Enter temperature 1"))
temp_2 = float(input("Enter temperature 2"))
temp_3 = float(input("Enter temperature 3"))
total_temp = (temp_1 + temp_2 + temp_3)
average = (total_temp / 3)
print("your average temperature is", average)