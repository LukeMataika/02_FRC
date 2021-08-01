# import libraries 
import pandas


# *** Functions go here ***

# checks that input is either a float or an
# integer that is more than zero. takes in custom error message
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that user has enterd yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0] :
                return var_item

        print("please enter either yes or no...\n")


# checks that string response is not blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nplease try again. \n".format(error))
            continue
        return response



# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# gets expenses, returns list which has
# the data frame and sub total
def get_expenses(var_fixed):
    # set up dictionaries

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    if var_fixed == "fixed":
        get_price = "How much? "
    else:
        get_price = "How much for a single item? "

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx" :

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", 
                                "the component name cant be" 
                                "blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "fixed":
            quantity = 1
        
        else:
        
            quantity = num_check("quantity:",
                                "the amount must be a whole number" 
                                "more than zero", 
                                int)

        price_question = "{} <more than 0>: $".format(get_price) 

        price = num_check(price_question, "Please enter a number more than zero",
                        float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)
    
    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # find sub total
    sub_total = expense_frame['Cost'].sum()

    # currency formatting (uses currency function)
    add_dollars = ['Price','Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


#print expenses frames
def expense_print (heading, frame, subtotal):
    print()
    print("**** {} costs ****".format(heading))
    print(frame)
    print()
    print("{} costs: ${:.2f}".format(heading, subtotal))
    return ""


# work out profit goal and total sales required
def profit_goal(total_costs):

    # initialise variables and error message
    error = "please enter valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("what is your profit goal (eg $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response [-1] == "%":
            profit_type = "%"
            # get amount (everything before the %)
            amount = response [:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero
            amount = float (amount)
            if amount <=0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("do you mean ${:.2f}. " 
                                 "ie  {:.2f} dollars? ,"
                                 "y / n ".format(amount, amount))
                                

            # set profit type based on user answer above 
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("do you mean {}%? , " 
                                   "y/n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

            # return profit goal to main routine
            if profit_type == "$":
                return amount
            else:
                goal = (amount / 100) * total_costs
                return goal


# *** main routine goes here ***
# get product name
produce_name = not_blank("product name: ", "the product name cant be blank.")

how_many = num_check("How many items are you making?", "please enter an integer more than zero", int)

print()
print("please enter your varibale cost...")
# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses [0]
variable_sub = variable_expenses [1]

print()
have_fixed = yes_no("do you have fixed costs ( y / n)? ")

if have_fixed == "yes":
    # get fixed costs
    print("Please enter your fixed costs / xxx for no fixed costs")
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses [0]
    fixed_sub = fixed_expenses [1]
else:
    fixed_sub = 0

#work out total costs and profit target
all_costs = variable_sub + fixed_sub

profit_target = num_check("What is your profit goal? $ ", "please enter a number more than zero, float")

profit_target = profit_goal + all_costs

# calculate reccomended price
selling_price = profit_target / how_many

# find total costs

# ask user for profit goal

# calculate reccomended price

# write data to file

# *** printing area ***

print()
print("**** Fund Raising - {} *****".format(produce_name))
print()
expense_print ("variable", variable_frame, variable_sub)

if have_fixed == "yes":
    print ("***** fixed costs *****")
    print(fixed_frame[['Cost']])
    print()
    print ("fixed costs : ${:.2f}".format(fixed_sub))

    print()
    print("Total Costs: ${:.2f}".format(variable_sub + fixed_sub))



print()
print("**** Total Costs: ${:.2f} ****".format(all_costs))
print()

print()
print("**** Profit & Sales Targets ****")
print("Profit Target: ${:.2f}".format(profit_target))
print("total sales: ${:.2f}".format(all_costs + profit_target))

print()
print("**** recommended selling price: "
      " ${:.2f}".format(selling_price))
