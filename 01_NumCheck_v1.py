#import libraries

# *** Function Goes Here ***


def num_check(question, error, num_type):
    valid = False
    while not valid :

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# main routine goes here
get_int = num_check("how many do you need? ",
                    "please enter an amount more than 0\n",
                    int)
get_cost = num_check("how much does it cost? $",
                    "please enter a number more than 0\n",
                    float)
