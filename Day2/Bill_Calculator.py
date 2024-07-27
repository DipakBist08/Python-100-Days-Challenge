print("Split Bill With Friends & Family...")

total_bill=float(input("Enter Your Total Bill: "))
tip_percentage=float(input("What Percentage Tip You Wanna Give? "))
total_bill_payers=int(input("How Many People to Split the Bill?: "))
tip_amount=total_bill*tip_percentage/100
grand_bill=total_bill+tip_amount
Individual_Bill= grand_bill/ total_bill_payers
print(f"Each Person Has to Pay :{Individual_Bill:.2f}") # .2f will roundup to two digits after decimal point.