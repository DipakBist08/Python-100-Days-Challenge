from Day5.Iterate_number_1_100 import number

Total_Sum=0
for number in range(1,101):
    if number % 2 == 0:
        Total_Sum+=number
print(f"Sum of even numbers 1 to 100 is :{Total_Sum}")