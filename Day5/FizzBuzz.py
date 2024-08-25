from Day5.sum_of_even_numbers_1_100 import number

for numbers in range(0,101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fuzz")
    elif numbers % 5 == 0:
        print("Buzz")
    # else:
    #     print("Invalid Input!!!!")


