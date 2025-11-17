day_screen_time = int(input("what is your day screen time in minutes"))
night_screen_time = int(input("what is your night screen time in minutes"))
daily_steps = int(input("how many steps have you taken today"))

if day_screen_time > 240 and daily_steps < 5000:
    flagged = True
elif night_screen_time > 60:
    flagged =True
else:
    flagged = False
if flagged == False:
    print("you  have not been flagged")
elif flagged == True:
    print("you have been flagged")