lane_status = {
    "Lane_1": "unoccupied",
    "Lane_2": "unoccupied",
    "Lane_3": "unoccupied",
    "Lane_4": "unoccupied",
    "Lane_5": "unoccupied"
}
def lane_booking():
    print("welcome to the bowling alley")
    print("the current status of the lanes is as follows:")
    for lane, status in lane_status.items():
        print(f"{lane}: {status}")
    lane_choice = int(input("which lane would you like to book today"))
    if lane_choice == 1:
        if lane_status["Lane_1"] == "unoccupied":
            print("Lane 1 is now occupied")
        else:
            lane_status["lane_1"] == "occupied"
            print("Lane 1 is already occupied")
        return hours_chosen()
    elif lane_choice == 2:
        if lane_status["Lane_2"] == "unoccupied":
            print("Lane 2 is now occupied")
        else:
            lane_status["Lane_2"] == "occupied"
            print("Lane 2 is already occupied")
        return hours_chosen()
    elif lane_choice == 3:
        if lane_status["Lane_3"] == "unoccupied":
            print("Lane 3 is now occupied")
        else:
            lane_status["Lane_3"] == "occupied"
            print("Lane 3 is already occupied")
        return hours_chosen()
    elif lane_choice == 4:
        if lane_status["Lane_4"] == "unoccupied":
            print("Lane 4 is now occupied")
        else:
            lane_status["Lane_4"] == "occupied"
            print("Lane 4 is already occupied")
        return hours_chosen()
    elif lane_choice == 5:
        if lane_status["Lane_5"] == "unoccupied":
            print("Lane 5 is now occupied")
        else:
            lane_status["Lane_5"] == "occupied"
            print("Lane 5 is already occupied")
            return lane_booking()
    else:
        print("Invalid lane choice. Please choose a lane between 1 and 5.")

def hours_chosen():
    print("You have chosen a lane")
    print("Please choose how many hours you would like to book the lane for")
    print("The cost is $10 per hour")
    print("chose 1 for 1 hour, 2 for 2 hours, 3 for 3 hours, or 4 for 4 hours")
    hours = int(input("How many hours would you like to book the lane for? "))
    if hours in [1, 2, 3, 4]:
        total_cost = hours * 10
        print(f"You have booked the lane for {hours} hour(s). The total cost is ${total_cost}.")
    else:
        print("Invalid number of hours. Please choose between 1 and 4 hours.")
        return hours_chosen()

def cafe_orders():
    print("Welcome to the cafe!")
    print("Here are the available items:")
    print("1. Coffee - $3")
    print("2. Tea - $2")
    print("3. Soft Drink - $1.5")
    print("4. Snack - $2.5")
    order = input("Please enter the item number you would like to order: ")
    if order == "1":
        print("You have ordered a Coffee.")
        if input("would you like to order anything else? yes or no") == "yes":
            return cafe_orders()
        else:
            print("Thank you for your order!")
            return 3
    elif order == "2":
        print("You have ordered a Tea.")
        if input("would you like to order anything else? yes or no") == "yes":
            return cafe_orders()
        else:
            print("Thank you for your order!")
            return 2
    elif order == "3":
        print("You have ordered a Soft Drink.")
        if input("would you like to order anything else? yes or no") == "yes":
            return cafe_orders()
        else:
            print("Thank you for your order!")
            return 1.5
    elif order == "4":
        print("You have ordered a Snack.")
        if input("would you like to order anything else? yes or no") == "yes":
            return cafe_orders()
        else:
            print("Thank you for your order!")
            return 2.5
    else:
        print("Invalid choice, please try again.")
        return cafe_orders()
price_1 = cafe_orders()
if price_1 == 3:
    print("Your total cafe order is $3.")
elif price_1 == 2:
    print("Your total cafe order is $2.")  
elif price_1 == 1.5:
    print("Your total cafe order is $1.5.")
elif price_1 == 2.5:
    print("Your total cafe order is $2.5.")