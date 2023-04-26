# Task:  to calculate a user's holiday cost including the
#   plane cost, hotel cost, and car rental cost

# Three inputs are given:
#   The first asks the user to enter their destination by referring to it's assinged number. This is then stored as the value for city_flight. /n's have been included for a neater output.
city_flight = input("Welcome to Python Travel! Please choose from the following destinations for your exciting, upcoming holiday: \n1. London City Airport \n2. Barcelona INT \n3. Lisbon INT \n4. Paris Charles do Gaulle Airport \n5. Amsterdam Airport Schiphol  \nPlease enter the number of your chosen destination: ")

#   The second stores the nnumber of nights as an integer value.
num_nights = int(input("Please enter the number of nights you would like to stay at your hotel: "))

#   The third stores the number of days required for the rental car also as an integer value.
rental_days = int(input("Finally, please enter the number of days you like like to hire a car for: "))

# Our first function (defined as hotel_cost) takes num_nights as its argument, and returns the value of num_nights when times by 150 (which is the hotel cost). This is then stored to be called up later
#   in the program.
def hotel_cost(num_nights):
    return num_nights * 150

# Our second function, plane_cost, uses the city_flight input as its argument. The variable ticket is assigned to an integer of 0 (otherwise empty), as this will be used to determine the price of the ticket
#   depending on the user's choice of destination (stored in the input city_flight). So, should the user enter 1 (London), the variable ticket will now be assigned a value of (£)100. The function will then
#   return ticket, therefore the output of this function will be £100.
# Should the user give an input not equal to the destination numbers, the function will run through else, informing the user of their invalid input.
def plane_cost(city_flight):
    ticket = 0
    if city_flight == "1":
        ticket = 100

    elif city_flight == "2":
        ticket = 150

    elif city_flight == "3":
        ticket = 140

    elif city_flight == "4":
        ticket = 120

    elif city_flight == "5":
        ticket = 130

    else:
        print("Sorry, you haven't entered from the given destinations. Please enter again.")

    return ticket

# Our third function, car_rental, uses the user's input (or number of days they intend to have the rental car) and simply times it by the cost of the car hire per day (in this case, £80).
#   It will then return the answer to be stored as its value.
def car_rental(rental_days):
    return rental_days * 80

# The final function calls all the inputs together which are assigned to their functions that are all explained above. Essentially, this totals up the entire cost of the holiday (number
#   nights at the hotel, the flight and the number of car rental days). It takes these as its argument and returns the total sum as seen in line 56.
def holiday_cost(num_nights, city_flight, rental_days):
    num_nights = hotel_cost(num_nights)
    city_flight = plane_cost(city_flight)
    rental_days = car_rental(rental_days)
    return num_nights + city_flight + rental_days

# The below variables are there to ensure the user can get a breakdown of each individual cost of each element of the holiday. These variables will be called into the final output of the user's 
#   holiday costs.
total_hotel_cost = hotel_cost(num_nights)
total_flight_cost = plane_cost(city_flight)
total_car_rental_cost = car_rental(rental_days)

# As calling in a function within the f string below will not display the correct output, the total cost function (holiday_cost) is assigned to its own variable, as this will display the correct data
#   within the final output.
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

# Finally, the f string printed below allows the implementation of the variables mentioned previously, as they will display the final cost, and individual costs, of the user's holiday.
#   Each variable added, to ensure it displays its value correctly, has been assigned as a string with the str function, as well as \n to separate the individual costs, for a more pleasing
#   output.
#   The output should display:

# Your total cost for your holiday package comes to: £1150
#   Your hotel cost: £750
#   Your flight cost: £0
#   Your car rental cost: £400
# Thank you for booking your holiday with Python Travel!
print(f"Your total cost for your holiday package comes to: £" + str(total_holiday_cost) + "\n Your hotel cost: £" + str(total_hotel_cost) + "\n Your flight cost: £" + str(total_flight_cost) + "\n Your car rental cost: £" + str(total_car_rental_cost) + "\nThank you for booking your holiday with Python Travel!")