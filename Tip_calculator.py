print("welcone to the tip calculator")

total_bill=float(input("What's the total bill?\n"))
tip=int(input("How much tip would you like to give? 10,12 or 15? "))
percentage_tip=int(input("How many people will split the bill?"))


bill_with_tip=total_bill*(1+tip/100)

print(bill_with_tip)
