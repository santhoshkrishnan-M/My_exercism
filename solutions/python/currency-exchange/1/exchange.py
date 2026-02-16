"""Functions for calculating steps in exchanging currency."""


def exchange_money(budget, exchange_rate):
    """
    Calculate exchanged foreign currency value.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate remaining money after exchange.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate total value of bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Calculate number of whole bills obtainable.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Calculate leftover amount after taking whole bills.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate maximum exchangeable value after fees and denomination limits.
    """
    # Adjust exchange rate with spread
    effective_rate = exchange_rate * (1 + spread / 100)

    # Exchange the budget
    exchanged_amount = budget / effective_rate

    # Get number of whole bills
    number_of_bills = int(exchanged_amount // denomination)

    # Return total exchangeable value
    return number_of_bills * denomination

