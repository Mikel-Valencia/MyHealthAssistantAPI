# Author: Mikel Valencia

import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=16))


def random_fraction() -> float:
    return round(1-random.random(), 2)


def random_positive_float() -> float:
    return round(10000*random_fraction()+random_fraction(), 2)
