print("=" * 55)
print("           CALENDAR VERIFICATION SYSTEM")
print("=" * 55)

year = int(input("Enter year: "))


if year <= 0:
    print("Error: Please enter a positive year.")
else:
    
    if year % 400 == 0:
        leap_year = True
        reason = "Century year divisible by 400"
    elif year % 100 == 0:
        leap_year = False
        reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        leap_year = True
        reason = "Divisible by 4 and not a century year"
    else:
        leap_year = False
        reason = "Not divisible by 4"

    
    if leap_year:
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_february = 29
    else:
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_february = 28

    
    print("\n" + "-" * 55)
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", days_in_year, "days")
    print("Days in February:", days_in_february, "days")
    print("Reason:", reason)
    print("-" * 55)