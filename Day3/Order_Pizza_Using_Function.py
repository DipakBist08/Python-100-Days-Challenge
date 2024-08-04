def get_pizza_size():
    while True:
        pizza_size = input("What size pizza do you want? S, M, L: ").lower()
        if pizza_size in ["s", "m", "l"]:
            return pizza_size
        else:
            print("Invalid size. Please enter 'S' for small, 'M' for medium, or 'L' for large.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ["y", "n"]:
            return answer
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

print("Order Your Pizza Now!!")

pizza_size = get_pizza_size()
add_pepperoni = get_yes_no("Do you want to add pepperoni? Y, N: ")
extra_cheese = get_yes_no("Do you want to add extra cheese? Y, N: ")

pizza_price = 0

if pizza_size == "s":
    pizza_price += 15
elif pizza_size == "m":
    pizza_price += 20
elif pizza_size == "l":
    pizza_price += 25

if add_pepperoni == "y":
    if pizza_size == "s":
        pizza_price += 2
    else:
        pizza_price += 3

if extra_cheese == "y":
    pizza_price += 1

print(f"Your final bill is: ${pizza_price}")
