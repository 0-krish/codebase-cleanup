def to_usd(my_price):
    """
    :param my_price: a number to format in USD
    :return: the price formatted in USD
    """
    return '${:,.2f}'.format(my_price)

def determine_winner(user_choice, computer_choice):

    """
    :param user_choice: rock/paper/scissors
    :param computer_choice: rock/paper/scissors
    :return: winner: user/computer based on both params
    """

    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice

if __name__ == "__main__":
    user_input = input("Please choose a price like 4.999: ")
    print(to_usd(float(user_input)))
