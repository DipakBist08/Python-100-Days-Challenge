print("Welcome to Rollercoster")
height=float(input("Enter Your Height: "))
if height>=120:
    print("You Can Ride Rollercoster.")
    age=int(input("Enter Your Age: "))
    if age<15:
        print("Pay $7")
    elif age<=25:
        print("You Pay:$12")
    else:
        print("You Pay:$15")
else:
    print("You a  re not allowed to ride rollercoster.")