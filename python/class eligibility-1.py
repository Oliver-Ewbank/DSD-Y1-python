age = int(input("what  is your age"))
income_check = input("Enter '1' if you are a low income participant, enter '2' if not")
past_eligibility = input("Enter '1' if you have had a free class in the last 30 days, enter '2' if not")

if age > 16 and age < 25 and income_check == 1 and past_eligibility == 1:
    eligible = True
if past_eligibility == 2:
    eligible = False
if income_check == 2:
    eligible = False
if age < 16 or age > 25:
    eligible = False

if eligible == True:
    print("you are eligible for a free class")
elif eligible == False:
    print("you are not eligible for a free class")