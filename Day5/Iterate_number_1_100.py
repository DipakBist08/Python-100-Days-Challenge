sum_of_evens = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum_of_evens += number
print(f"The sum of all even numbers from 1 to 100 is:{sum_of_evens}")
