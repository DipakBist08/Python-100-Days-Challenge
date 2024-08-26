def calculator():
    def additon( num1, num2):
        return num1 +num2
    def subtraction(num1,num2):
        return num1- num2
    def multiplication(num1, num2):
        return num1*num2
    def divison(num1,num2):
        if num2 !=0:
            return num1/num2
        else:
            return "Division by zero is not allowed."

    print("Select Operation: ")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")

    user_choice =input("Select operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if user_choice =="1":
        print(f"The result is :{additon(num1,num2)}")
    elif user_choice =="2":
        print(f"The result is : {subtraction(num1,num2)}")
    elif user_choice=="3":
        print(f"The result is: {multiplication(num1,num2)}")
    elif user_choice=="4":
        print(f"The result is : {divison(num1, num2)}")
    else:
        print("Please Valid Input!!!!")
calculator()


