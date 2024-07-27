def splitBill():
    print("Split Bill With Family & Friends..")

    try:
        total_bill=float(input("Enter Your Total Bill Amount: "))
        tip_percentage=int(input("How May % Bill You wanna Tip: "))
        total_bill_payers=int(input("How Many People to Split This Bill: "))
        if total_bill_payers<=0:
            print("Atleast One Person Required to Pay Bill...")


        tip_amount=total_bill*tip_percentage/100
        grand_bill= total_bill + tip_amount
        individual_splited_bill= grand_bill / total_bill_payers
        # print(f"Total Bill:$ {total_bill:.2f}")
        # print(f"Tip Percentage:${tip_percentage}")
        # print(f"Total Bill Payers:{total_bill_payers}")
        print(f"Grand Bill:${grand_bill:.2f}")
        print(f"Each of the {total_bill_payers} person(s) needs to pay: ${individual_splited_bill}")
    except ValueError:
        print("Invalid Input.Try Again")


splitBill()



