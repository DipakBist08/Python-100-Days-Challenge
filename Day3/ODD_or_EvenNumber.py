num=int(input("Find a Number Even or Odd: "))
try:

    if num%2==0:
        print(f"The {num} is a Even Number.")
    else:
        print(f"The {num} is a Odd Number...!")
except ValueError:
    print("Input Valid Number")