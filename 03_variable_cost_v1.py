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
    
# Checks user enters valid choice based on a list
def string_check(question, options):

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in options:

            # check if response is in the list
            if response == var_item:
                return var_item
            
            # if response is the first letter of something in the list, return the entire word
            elif response == var_item[0]:
                return var_item

        print("Please enter a valid response")

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

# loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx" :

    print()
    # get name, quantity and item
    item_name = not not_blank("item name: ", 
                              "the component name cant be" 
                              "blank.")
    if item_name.lower() == "xxx":
        break
    
    quantity = num_check("quantity:",
                         "the amount must be a whole number" 
                         "more than zero", 
                         int)
    price = num_check("how much for a single item ? $", 
                      "the price must be a number <more" 
                      "than 0>", 
                      float)

    # add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('item')

# calculate cost of each component
variable_frame['cost'] = variable_frame['quantity']\
                         * variable_frame['frame']

# find sub total
variable_sub = variable_frame['cost'].sum()

# currency formatting (uses currency function)
add_dollars = ['price','cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply()

# *** printing area ***

print (variable_frame)

print()

print("variable cost: ${:.2f}".format(variable_sub))