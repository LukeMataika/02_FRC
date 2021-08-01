from typing import MutableMapping
import pandas 


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


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nplease try again. \n".format(error))
            continue
        return response


# curreny formatting function
def currency(x):
    return "${:.2f}".format(x)


# get expenses, return list which has
# the data frame and subtotal
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
        
        quantity = num_check("quantity:",
                            "the amount must be a whole number" 
                            "more than zero", 
                            int)
        price = num_check("how much for a single Item ? $", 
                        "the price must be a number <more" 
                        "than 0>", 
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


# *** main routine starts here ***

# set up dictionaries and lists

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# get user data
produce_name = not_blank("product name: ", "the product name cant be blank.")

variable_expenses = get_expenses ("variable")
variable_frame = variable_expenses [0]
variable_sub = variable_expenses [1]

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
    
    quantity = num_check("quantity:",
                         "the amount must be a whole number" 
                         "more than zero", 
                         int)
    price = num_check("how much for a single Item ? $", 
                      "the price must be a number <more" 
                      "than 0>", 
                      float)

    # add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# calculate cost of each component
variable_frame['Cost'] = variable_frame['Quantity']\
                         * variable_frame['Price']

# find sub total
variable_sub = variable_frame['Cost'].sum()

# currency formatting (uses currency function)
add_dollars = ['Price','Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# *** printing area ***

print (variable_frame)

print()

print("variable cost: ${:.2f}".format(variable_sub))