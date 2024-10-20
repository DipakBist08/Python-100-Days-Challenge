#The number is divisiable by 1 and number itself 2, 3,5,7,11,13,17,19,23 and ....


def Prime_Num(number):
    is_prime=True
    for i in range(2,number):
        if number % i ==0:
            is_prime=False


    if is_prime:
        print("It's a prime number.")
    else:
        print("It's Not a Prime Number.")


n=int(input("Enter a Number to Check?: "))
Prime_Num(number=n)


