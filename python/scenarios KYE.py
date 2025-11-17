def PRS():
    patient_name = input("what is your name")
    patient_age = input("what is your age")
    patient_height = input("what is your height")
    
    print("your name is", patient_name, "you are", patient_age, "years old and are", patient_height, "tall")

def BMI():
    patient_weight = input("what is your weight in KG")
    patient_hight = input ("what is your height in M")
    patient_BMI = int(patient_weight) // int(patient_hight) * int(patient_hight)
    print(patient_BMI)

def MDT():
    max_dosage = 100
    min_dosage = 25
    patient_dosage = input("what is your average dosage")
    if min_dosage <= patient_dosage <= max_dosage:
        print("your average dosage is correct")

def HBS():
    days_stayed = input("how many days have you stayed")
    room_cost = 500
    total_room_cost = (room_cost * days_stayed)
    treatments = 1500
    consultations = 800
