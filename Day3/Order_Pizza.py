print("Order Your Pizza Now!!")
pizza_size = input("Select Your Pizza Size:S,M,L: ").upper()
add_pepperoni = input("Do You Want Add Pepproni? Y,N: ").upper()
extra_cheese = input("Do you Add Extra Cheese? Y,N: ").upper()
pizza_price=0
if pizza_size=="S":
    pizza_price+=15
elif pizza_size=="M":
    pizza_price+=20
elif pizza_size=="L":
    pizza_price+=25
else:
    print("Invalid size selected. Please choose S, M, or L: ")
    exit()
if add_pepperoni=="Y":
    if pizza_size=="S":
        pizza_price+=2
    else:
        pizza_price+=3
if extra_cheese =="Y":
    pizza_price+=1
print(f"Your  Final Bill is:${pizza_price}")

