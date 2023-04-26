# Menu defined as a list below, with food items given.

menu = ['avacado', 'granola', 'porridge', 'toast']

# Stock numbers of the food items in menu given, using the dictionary method.
#   Here, menu items are the key, with the value given to each (i.e. being the stock number)

stock = {'avacado' : 30,
         'granola' : 50,
         'porridge' : 35,
         'toast' : 40
         }

# The same method as above is given to the price dictionary. They keys, again, being
#   the menu items and the values being the price of the item.

price = {'avacado' : 5,
         'granola' : 5,
         'porridge' : 6,
         'toast' : 3
         }

# The variable 'total' is given the value of 0 because it will later act as the function 
#   for the total of stock worth in the cafe.

total_stock = 0

# Now, we use a for loop to iterate through all the items in the menu, as well as their
#   corresponding stock number and price. So, the 'items' acts as the index going through 
#   all items in the list and dictionaries.

for items in menu:

# We then use the below calulator operation: total_stock is concatenated with: the stock dictionary,
#   along with iterating through the 'items' inside it times by and the price dictionary, along with iterating
#   through the 'items' inside it, as well.

# Actual calcation of stock[items * price[items] = 
# 30 * 5 = 150
# 50 * 5 = 250
# 35 * 6 = 210
# 40 * 3 = 120
# = 730

# total = 0
# 0 + 730

# total_stock = 730

    total_stock += (stock[items] * price[items])

# IDE will give result of 730.

print(total_stock)