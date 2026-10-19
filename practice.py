
bill = float(input("Enter the total bill amount: ₦"))
tip_percentage = float(input("Enter tip percentage: "))
people = int(input("How many people are sharing the bill? "))

tip = bill * tip_percentage / 100
total_bill = bill + tip
amount_per_person = total_bill / people

print("\n----- BILL SUMMARY -----")
print(f"Original bill: ₦{bill:.2f}")
print(f"Tip amount: ₦{tip:.2f}")
print(f"Total bill: ₦{total_bill:.2f}")
print(f"Each person pays: ₦{amount_per_person:.2f}")
