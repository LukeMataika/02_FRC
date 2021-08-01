# import libraries 


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
 
 #  *** Main routine starts here *****


# decorates statements to make them stand out...
def statement_generator(statement, decoration, amount):

    multi_dec = decoration * amount

    print("{} {} {}".format(multi_dec, statement, multi_dec))

    return ""

# Main routine goes here

# lists go here...
yes_no_list = ["yes", "no"]


# ask user if they need instructions...

statement_generator("Fund Raising Calculator", "*", 6)
print()

want_help = string_check("Do you want to read the instructions? ", yes_no_list)

if want_help == "yes":
    print("Useful instructions go here")

print()
statement_generator("Lets get started", "-", 3)
print()

get_int = num_check("How many do you need? ",
                    "PLease enter an amount more than 0\n",
                    int)
get_cost = num_check("How much does it cost? $",
                    "Please enter a number more than 0\n",
                    float)

print("You need: {}".format(get_int))
