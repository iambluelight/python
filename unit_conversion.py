
while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        kilometres = float(input("Enter distance in kilometres: "))
        miles = kilometres * 0.621371
        print(f"{kilometres} kilometres = {miles:.2f} miles")

    elif choice == "2":
        miles = float(input("Enter distance in miles: "))
        kilometres = miles * 1.609344
        print(f"{miles} miles = {kilometres:.2f} kilometres")

    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")

    elif choice == "4":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")

    elif choice == "5":
        print("Thank you for using the Unit Converter. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 5.")
