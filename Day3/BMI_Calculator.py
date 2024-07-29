# BMI Calculation Formula: BMI = weight / (height ** 2)


weight = float(input("Enter Your Weight in KG: "))
height = float(input("Enter Your Height in meters: "))


BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f}. You are underweight.")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI:.2f}. You have a normal weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI:.2f}. You are overweight.")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI:.2f}. You are obese.")
else:
    print(f"Your BMI is {BMI:.2f}. You are clinically obese.")
