print("Welcome to Rollercoster")
height=int(input("Enter Your Height in CM: "))
bill=0
if height >=120:
    print("Welcome to Rollercoster,You can Buy a ticket")
    age=int(input("Enter Your Age: "))
    if age<12:
        bill=5
        print("You have to pay:$5")
    elif age<=18:
        bill = 7
        print("You have to pay:$7")

    else:
        bill=12
        print("You have to pay:$12")
    wants_photo= input("Do you want to photo? ")
    if wants_photo=="y":
        bill=bill+3
        print(f"Your Final Bill is:${bill}")
    else:
        print(f"Your Final Bill is :${bill} ")
else:
    print("Sorry,You can't ride rollercoster")