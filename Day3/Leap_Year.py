year=int(input("Which Year do you want to check? "))
if year%4==0:
    print("Leap Year")
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("No Leap Year")
    else:
        print("Leap Year")
else:
    print(f"{year} is not leap year")
