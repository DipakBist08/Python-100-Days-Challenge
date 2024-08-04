import random
users_name=input("Enter Users Name to Pay Bll: ")
names=users_name.split(", ")

person_will_pay_bill=random.choice(names)
print(person_will_pay_bill)

#This is short hand method as compare to who_will_pay_bill.py module

