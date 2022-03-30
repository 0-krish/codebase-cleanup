def to_usd(my_price):
    """
    :param my_price: a number to format in USD
    :return: the price formatted in USD
    """
    return '${:,.2f}'.format(my_price)

def determine_winner():

if __name__ == "__main__":
    user_input = input("Please choose a price like 4.999: ")
    print(to_usd(float(user_input)))
