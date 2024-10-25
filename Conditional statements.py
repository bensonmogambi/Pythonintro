# If you fulfill the condition there ss going to be an output

#if......else.... statement
votes = 90000
if votes > 50000:
    print("you elected as prezo")
    print("starting 2040 to 2080")
else:
    print("you are not elected as prezo")


marks = 89
if marks > 80:
    print("you have a grade A")
else:
    print ("you have a grade B")


marks = 20
if marks > 80 and marks <= 100:
    print("you have a grade A")
elif marks > 70 and marks <= 80:
    print ("you have a grade B")
elif marks > 60 and marks <= 70:
    print ("you have a grade C")
elif marks > 50 and marks <= 60:
    print ("you have a grade D")
elif marks > 40 and marks <= 50:
    print ("you have a grade E")
elif marks > 0 and marks <= 40:
    print ("you have a grade FAIL")
else:
    print ("enter a value between 0 and 100")



# create an atm machine that awards discounts to users depending on their
# withdrawal amount and display the total amount inclusive of the discounts.
# Withdrawal above 10,000 award a discount of 15%, withdrawal above 5000 give
# a discount of 10% and lastly a withdrawal of above 2000 give a discount of
# 5%

# Function to handle the ATM withdrawal and discount calculation
def atm_machine():
    try:
        # Get the withdrawal amount from the user
        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

        # Initialize discount
        discount = 0

        # Apply discount based on the withdrawal amount
        if withdrawal_amount > 10000:
            discount = 0.15  # 15% discount
        elif withdrawal_amount > 5000 and withdrawal_amount <= 10000:
            discount = 0.10  # 10% discount
        elif withdrawal_amount > 2000 and withdrawal_amount <= 5000:
            discount = 0.05  # 5% discount

        # Calculate discount amount and final total
        discount_amount = withdrawal_amount * discount
        total_amount = withdrawal_amount - discount_amount

        # Display results
        if discount > 0:
            print(f"Discount applied: {discount * 100:.0f}%")
        else:
            print("No discount applied.")

        print(f"Total amount after discount: {total_amount:.2f}")

    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter a valid number.")


# Run the ATM machine function
atm_machine()


























