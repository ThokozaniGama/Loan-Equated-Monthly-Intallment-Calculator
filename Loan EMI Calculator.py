'''
Loan Equated Monthly Installment (EMI) Calculator:

Developed by Thokozani Zwelihle Gama

Psuedo code:
START:
    The program is Modularized to avoid duplication
    
    define menu function:
        1. Loan EMI Caluculator
        2. Exit

    define get_valid_number function: # Takes prompt and data type as parameter
        This function loops until the user put a valid data type.
        Returns a validated value.
        
    define user input function: # Takes principal price, interest rate and number of months as parameter
        It passed its parameters to get_valid_number function by argument to hold each value.
        Returns the three paramenter values.

    def emiformula function: # Takes principal price, interest rate and number of months as parameter
        Use standard EMI formula to calculate the final EMI answer and returns it.

    def main function for the code execution
        As long as the boolean variable is True keeps the code running, stop if False.
        Display the menu function
        Allow the user to choose an option and validate the user input.

    Execute the main function
END:
'''


# Menu function used to display option to prompt a user.
def menu():
    print("\n-------Menu--------")
    print("1. Loan Equated Monthly Installment(EMI) Calculator\n2. Exit\n")

# Helper function to validate a single input independently
def get_valid_number(prompt, number_type):
    while True:
        try:
            value = number_type(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue    # Skip return
            return value  # Ends the entire loop
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main user input function
def user_input():
    # Pass by arguments to validate all the required user input
    principal_amount = get_valid_number("Enter the principal amount you borrowed initially: ", float)
    interest_rate_per_month = get_valid_number("Enter the interest rate per month(%): ", float)
    number_of_months = get_valid_number("Enter number of months to pay the loan: ", int)
    
    return principal_amount, interest_rate_per_month, number_of_months

# Implement the EMI formula and calculate the final answer
def emiformula(principal_amount, interest_rate_per_month, number_of_months):
    # Convert percentage to decimal
    r = interest_rate_per_month / 100
    # Apply the EMI formula: [P * R * (1 + R)^N] / [(1 + R)^N - 1]
    factor = (1 + r) ** number_of_months
    emi = (principal_amount * r * factor) / (factor - 1)
    
    return emi



# Main function for execution
def main():

    cont = True # Boolean variable
    while cont == True:
        # Display Menu
        menu()
        try:
            
            option = int(input("Enter your option: "))  # Accept user input option for the menu

            # Handle option input error
            while option != 1 and option != 2:
              option = int(input("\nEnter your option: "))  # Calls option itself to try again

            if option == 1:
                price, rate, months = user_input()

                # Calling the function and unpacking the 3 returned values
                emi_answer = emiformula(price, rate, months)
                print(f"The Loan EMI = \u20B9{emi_answer:.2f}")
            
            elif option == 2: 
                cont = False    # Boolean flag to end the outer loop
                print("Thanks Bye!")
            

        except ValueError:
            print("Choose the correct option:")


# Run/call/execute main function
if __name__ == "__main__":
    main()
