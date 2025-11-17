def MENU():
    print("type 1 for MSR")
    print("type 2 for FCA")
    print("type 3 for STA")
    safety = int(input("what would you like to do"))
    if safety == 1:
        MSR()
    elif safety == 2:
        FCA()
    elif safety == 3:
        STA()
    else:
        MENU()


    def MSR():
        age = input("what is your age")
        weight = input("what is your weight")
        if int(age) > 12 and int(weight) > 40:
            print("Safe to give")
        else:
            print("Not safe")


    def FCA():
        age = input("what is your age")
        if int(age) > 18:
            print("access granted")
        else:
            med_clear = input("do you have medical clearance, 1 for yes 2 for no :")
            if int(med_clear) == 1:
                print("access granted")
            else:
                print("access denied")


    def STA():
        sleep_status = input("are you asleep, 1 for yes 2 for no :")
        heart_rate = int(input("what is your heartrate"))
        if sleep_status == 2 and heart_rate > 100:
            print("WAKE UP")