swimming = int(input("Please enter your swimming time in minutes: "))
cycling  = int(input("Please enter your cycling time in minutes: "))
running = int(input("Please enter your running time in minutes: ")) 

# The user is required to enter three separate numbers (swim, cycle and run) which 
# will be stored as values.

total_triathlon_time = swimming + cycling + running 

#All the above values are now added together and are assigned to a new 
# variable: total_triathlon_time

if total_triathlon_time <= 100:
    print("Well done! You have been awarded Provincial Colours.")

# Here, our first if condition is declared. If the user enters a number 
# that is less than or equal to 100, they have been awarded Provincial Colours.

elif total_triathlon_time <= 105:
    print("Great work! You have been awarded Provincial Half Colours.")

# If the user enters a number higher than the first if condition (100), python will
# pass into the elif. If the combined number is equal to or less than 105, the user will be
# awarded Provincial Half Colours.

elif total_triathlon_time <= 110:
    print("Good effort! You have been awarded Provincial Scroll.")

#As above, the combined number is higher than the first if and elif, but less than
# 110, the user will receive (the output) Provincial Scroll.

else:
    print("Good attempt! Unfortunately, you have not receieved an award.")

# If the user has entered a number higher than 110 (minutes), each condition will be skipped 
# resulting in the else condition. The user receives no award.
