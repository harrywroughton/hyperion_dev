# All global mathematical functions are defined straight away as they will be utilised in the calculator function below.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulus(x, y):
    return x % y

def exponentiation(x, y):
    return x ** y

# User greeted with the calculator application, in which they are directed to select the mathematical function they want (by number):

print("Hello, welcome to the calculator app! Please select an operation: \n 1. + (addition),\n 2. - (subtraction),\n 3. * (multiplication),\n / 4. (division),\n 5. % (modulus),\n 6. ** (exponentiation)\n")

# calculator defined as its own function

def calculator():

    # calculator operation set within a while loop, and the input is defined by the mathematical function the use wants to use

    while True:
        choice = input("Enter choice (1 / 2 / 3 / 4 / 5 / 6): ")

        # if the user selects one of the given mathematical functions, they will have to select which numbers they want to set within the mathematical operation
        # Then they will be directed within the if loop to which operation they've chosen. 

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num_1 = float(input("Please enter your first number: "))
                num_2 = float(input("Please enter your second number: ")) 

                # As with all mathematical functions, once the calculation has been performed, the user's calculation will be soted in a txt file to access in the second function
                # (calculator_reader())
                # Example below:

                # If user choice equal to 1, output will print num_1 input, display the addition symbol, as well as num_2 input and give the answer by recalling on the global addition
                # function. It will then save this calculation to the txt file by writing the calculation in an f string.
                if choice == '1':
                    print(num_1, "+", num_2, "=", add(num_1, num_2))
                    with open("calculations.txt", "w") as w_f:
                        w_f.write(f"{num_1} {add} {num_2} = {add(num_1, num_2)}")

                elif choice == '2':
                    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
                    with open("calculations.txt", "w") as w_f:
                        w_f.write(f"{num_1} {subtract} {num_2} = {subtract(num_1, num_2)}")

                elif choice == '3':
                    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
                    with open("calculations.txt", "w") as w_f:
                        w_f.write(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")

                elif choice == "4":
                    print(num_1, "/", num_2, "=", divide(num_1, num_2))
                    with open("calculations.txt", "w") as w_f:
                        w_f.write(f"{num_1} {divide} {num_2} = {divide(num_1, num_2)}")

                elif choice == "5":
                    print(num_1, "%", num_2, "=", modulus(num_1, num_2))
                    with open("calculations.txt", "w") as w_f:
                        w_f.write(f"{num_1} {modulus} {num_2} = {modulus(num_1, num_2)}")

                elif choice == "6":
                    print(num_1, "**", num_2, "=", exponentiation(num_1, num_2))
                    with open("calculations.txt", "w") as w_f:
                        w_f.write(f"{num_1} {exponentiation} {num_2} = {exponentiation(num_1, num_2)}")

                # Should the user not give a given option, they will be redirected back to the choice 

                else:
                    print("Invalid input.")

                # Once the user has performed their calculation, they will be given the option to perform another calculation. If they select no (as capitals or not with the
                # .lower function), they will break out of the calculator() function, and be directed to the calculator_reader() function. Otherwise, they will be redirected
                # back to the while loop

                next_calculation = input("Would you like to perform another calculation? Type yes/no: ")
                if next_calculation.lower != "no":
                    break

                else:
                    continue

                # To ensure the code doesn't crash, two except functions are added: one for an invalid input that is 1, 2, 3, 4, 5, or 6; and one for dividing by zero. 
                # Both of which will redirect the user back to the while loop start.

            except ValueError:
                print("Invalid input.")
                continue

            except ZeroDivisionError:
                print("Sorry, I cannot divide by zero! Please try again:")
                continue

        # If the user doesn't enter 1 - 6, they will be informed on an invalid input and redirected back to the input.

        else:
            print("Sorry, you have entered an invalid input. Please try again")

calculator()

# new function defined as calculator_reader()

def calculator_reader():
    user_choice = input("Welcome to calulator app! Please select the following options: \n 1. Perform a calculation \n 2. Read previous calculations \n Please enter either 1 or 2: ")

    # To ensure the code doesn't crash, if a user enters an input that isn't 1 or 2, it will raise an exception as an invalid input, and redirect the user back to the original input above
    if user_choice not in ["1", "2"]:
        raise Exception("Sorry, you have entered an invalid input. Please try again.")
    
    # If the user selects 2, the output will display the contents of the previously created 'calculation.txt. file (with all previous calculations), however, should no previous calculations
    # exist, the user will be directed back to the if statement above.

    if user_choice == "2":
        try:
            with open("calculations.txt", "r") as f:
                previous_calculations = f.read()
                print(previous_calculations)
        except FileNotFoundError:
            print("No previous calculations found.")

    # Should the user select one, they will be redirected back to the calculator function

    elif user_choice == "1":
        calculator()

# Call the calculator_reader() function

calculator_reader()
