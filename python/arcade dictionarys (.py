arcade = (
    "games": {
        "pinball wizard": {"catagory": "racing", "status": "working"},
        "retro racer": {"catagory": "racing", "status": "needs service"}
    }
    )

option = int(input("1. view machines, 2. add machine, 3. update machine status, 4. delete machine"))
if option == 1:
    print("place holder")
elif option == 2:
    name = input("enter the machine name here")
    catagory = input("enter the machine catagory here")
    status = input("enter the machine status here")