print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Calculation
bill_with_tip = bill + (bill * tip / 100)
amount_per_person = bill_with_tip / people

# Output
print(f"Total bill with tip: ${bill_with_tip}")
print(f"Each person should pay: ${amount_per_person:.2f}")
