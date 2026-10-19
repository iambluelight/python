
while True:
    bill_input = input(
        "Enter the bill amount (or type 'quit' to exit): ₦"
    )

    if bill_input.lower() == "quit":
        print("Thanks for using the Tip & Bill Splitter!")
        break

    try:
        bill = float(bill_input)

        if bill <= 0:
            print("The bill must be greater than zero. Try again.")
            continue

    except ValueError:
        print("Invalid amount. Please enter a number.")
        continue

    # Get a valid tip percentage
    while True:
        try:
            tip_percentage = float(input("Enter tip percentage: "))

            if tip_percentage < 0:
                print("Tip percentage cannot be negative.")
                continue

            break

        except ValueError:
            print("Invalid percentage. Please enter a number.")

    # Get a valid number of people
    while True:
        try:
            people = int(input("How many people are sharing the bill? "))

            if people <= 0:
                print("Enter at least 1 person.")
                continue

            break

        except ValueError:
            print("Please enter a whole number of people.")

    # Calculate the bill
    tip = bill * tip_percentage / 100
    total_bill = bill + tip
    amount_per_person = total_bill / people

    # Display the results
    print("\n----- BILL SUMMARY -----")
    print(f"Original bill: ₦{bill:.2f}")
    print(f"Tip amount: ₦{tip:.2f}")
    print(f"Total bill: ₦{total_bill:.2f}")
    print(f"Each person pays: ₦{amount_per_person:.2f}")

    again = input("Calculate another bill? (yes/no): ").lower().strip()

    if again in ("no", "n", "quit"):
        print("Thanks for using the Tip & Bill Splitter!")
        break

