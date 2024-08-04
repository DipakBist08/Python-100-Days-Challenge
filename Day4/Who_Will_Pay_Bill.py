import random
users_names= input("Enter Names to Pay Bill (separated by commas): ")

names=users_names.split(", ")
# print(names)

num_item=len(names)
# print(num_item)

random_choice=random.randint(0,num_item-1)
who_will_pay_bill=names[random_choice]
print(who_will_pay_bill + " is going to pay bill.")