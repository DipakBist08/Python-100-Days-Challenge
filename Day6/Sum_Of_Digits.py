User_Input = int(input("Enter Any Number from 0 to 9 to get sum: "))
Digits_sum = 0
while User_Input > 0:
    digit=User_Input %10
    Digits_sum+=digit
    User_Input//=10
print(f"The sum of digits is : {Digits_sum}")