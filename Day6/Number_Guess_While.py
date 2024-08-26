import random
random_num= random.randint(1,11)
user_guess= None

while user_guess !=random_num:
    try:
        user_guess = int(input("Guess a number between 1 to 10: "))
        if user_guess==random_num:
            print("Congrats!! You Got it..")

        else:
            print("Try Again")
    except ValueError:
        print("Invalid Input!! Please Enter a number form 1 to 10.!!!")