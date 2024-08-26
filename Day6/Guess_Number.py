import  random
random_number=random.randint(1,11)
for numbers in range(1,11):
    user_input = int(input("Guess a number form 1 to 10: "))
    if user_input==random_number:
        print("Right")
        break
    else:
        print("Try again")
