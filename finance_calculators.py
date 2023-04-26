import math

# user given clear defintions of their choices
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay back on a home loan")

# once decided, user inputs which they want to select
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# .lower ensures any input (caps, mixed or lowercase) is accepted
user_input = user_input.lower()

# to ensure clarity, if user enters invalid output, the below will redirect to intructions
if user_input != "investment" and user_input != "bond":
    print("Sorry, you have not entered a valid input. Please enter either 'investment' or 'bond.")

else:
# if user enters investment, the below will if statement will guide through:
    if user_input == "investment":
    # decimal numbers accepted as this might be required from user input
        P = float(input("Please enter how much you intend to deposit here:  ")) 
    # next input asks for interest rate as just a number
        r = float(input("Please enter the interest rate as a number, excluding the '%' symbol: "))
    # r variable is divided by 100 to ensure it is the correct decimal, e.g. 0.08
        r = r / 100 
    # user finally enters number of years to invest money over
        t = float(input("Please enter the number of years you would you like your money to be invested over: ")) 
    # once P, r and t variables stored, the user selects either of the statements in the print below, which has been 
    # cast as a string input
        interest = str(input("Please enter either 'simple' or 'compound' as your preferred interest: "))
    # .lower ensures any input (caps, mixed or lowercase) is accepted
        interest = interest.lower
    # if and else are set - python then goes through mathmatical function to determine output
        if interest == "simple":
        # simple interest formula is set from previously stored variables
            A = P * (1 + r * t) 
        # A (amount) is added to print string below to give result of simple interest
            print("Your total simple interest is: " + str(A) + ".") 
        else:
        # same again for compound interest formula
            A = P * math.pow((1 + r), t)
            print("Your total compound interest is: " + str(A) + ".")

# should the user type 'bond', the above if statement will be ignored, and else will be passed through:
    else:
        if user_input == "bond": 
        # user enters value of house (cast as decimal number), stored as variable 'P'
            P = float(input("Please enter the present value of the house: "))
        # user enters monthly interest without % to stick to float value
            i = float(input("Please enter the monthly interest rate as a number, excluding the '%' symbol: "))
        # input of i is then divided by 100, and then by 12, and stored as such
            i = (i / 100)/12
        # finally, the user enters number of months bond repaid over - stored as 'n' variable
            n = float(input("Please enter the number of months over which the bond will be repaid: "))
        # bond formula is set below
            bond_repayment = (i * P)/(1 - (1 + i) ** (-n))
        # bond_repayment added to string to give result:
            print("The amount you will have to repay monthly is:" + str(bond_repayment) + ".")


