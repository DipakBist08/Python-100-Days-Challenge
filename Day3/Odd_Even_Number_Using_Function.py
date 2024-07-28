def check_even_odd_number():
    try:
        num=int(input("Enter a Number: "))
        if num % 2 ==0:
            print(f"The {num} is a Even Number")
        else:
            print(f"The {num} is a Odd Number.")
    except ValueError:
        print("Input Valid Number.!!!")

check_even_odd_number()
