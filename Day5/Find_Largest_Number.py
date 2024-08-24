# Find the Largest Number:
# Create a program that iterates through a list of numbers and finds the largest number.
# Output: 89
from Day5.Sum_Of_Numbe_In_List import numbers

# numbers = [3, 56, 23, 89, 15]
# max_number=numbers[0]
# for number in numbers:
#     if number>max_number:
#         max_number=number
# print(f"The Largest Number is : {max_number}")

numbers_list = [3, 56, 23, 89, 15,88,90,101]
largest_num= numbers_list[0]
for num in numbers_list:
    if num>largest_num:
        largest_num=num
print(f"The Largest Number is :{largest_num}")