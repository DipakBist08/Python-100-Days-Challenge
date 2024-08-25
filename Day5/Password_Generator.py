import string
import random
letters= string.ascii_letters
# print(letters)
numbers = string.digits
# print(numbers)
symbols = string.punctuation
# print(symbols)
password_combine = letters + numbers  + symbols
password_lenght= int(input("Enter Desired Password Lenght : "))
password= ''.join(random.choice(password_combine)for i in range(password_lenght))
print(f"Your Password is : {password}")




