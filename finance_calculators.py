import math

# To start of the program
print("Choose a calculation:")
print("investment - to calculate the amount of interest you will earn on your investment")
print("bond - to calculate the amount you will have to pay on a home loan")
choice = input("Eneter either 'investment' or 'bond' from menu above to proceed: ").lower()

# processing the users choice
if choice == "investment":
    # To get user input for investment calculation 
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100 # Convert to decimal
    t = float(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter the type of interest ('simple' or 'compound'): ").lower()

    # Canculating the total amount for investment
    if interest_type == "simple":
        total_amount = P * (1 + r * t)
    elif interest_type == "compound":
        total_amount = P * math.pow((1 + r), t)
    else:
        print("Invalid interest type entered.")
        total_amount = None
    
    # Outputting the result
    if total_amount is not None:
        print(f"The total amount after {t} years: {total_amount: .2f}")

elif choice == "bond":
    # To get user input for bond calculation 
    P = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the interest rate (as a percentage): ")) / 100 # Convert to decimal
    i = annual_rate / 12 # Monthley interest rate
    n = float(input("Enter the number of months you plan to take to repay the bond: "))

    # Calculating the monthly repayment for bond
    monthly_repayment = (i * P) / (1 - math.pow((1 + i), -n))

    # Outputting the result
    print(f"Your monthly bond repayment will be: {monthly_repayment: .2f}")

else:
    print("Invalid choice entered. Please enter 'investment' or 'bond'.")
