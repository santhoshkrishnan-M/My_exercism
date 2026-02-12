"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# Constants
EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # in minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - remaining bake time (in minutes).

    This function subtracts the elapsed bake time from the expected bake time
    to determine how much longer the lasagna needs to bake.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes).

    Each layer takes a fixed amount of time to prepare, defined by
    the PREPARATION_TIME constant.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - total elapsed time (in minutes).

    This function returns the sum of the preparation time and the
    elapsed bake time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

