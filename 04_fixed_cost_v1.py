# import libraries
import pandas


# *** functions go here ***

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


# checks that user has entered yes / no to a question
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


# *** main routine goes here ***
# get product name
produce_name = not_blank("product name: ", "the product name cant be blank.")

# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses [0]
variable_sub = variable_expenses [1]

print()
print("Fixed Costs...")

# get fixed costs
fixed_expenses = get_expenses("fixed")
fixed_frame = variable_expenses [0]
fixed_sub = fixed_expenses [1]

# find total costs

# ask user for profit goal

# calculate reccomended price

# write data to file

# *** printing area ***

print ("***** variable costs *****")
print (variable_frame)
print()

print("variable costs : ${:.2f}".format(variable_sub))

print ("***** fixed costs *****")
print(fixed_frame[['Cost']])
print()
print ("fixed costs : ${:.2f}".format(fixed_sub))