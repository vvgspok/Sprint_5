import random
import string
from data import domain_name, category, city, price, description


def generation_mail():
    #all_symbols = string.ascii_lowercase+string.ascii_uppercase
    all_symbols = string.ascii_lowercase
    user_name = ''.join(random.choice(all_symbols) for _ in range(10))
    return f"{user_name}@{random.choice(domain_name)}"


def generation_mail_not_mask():
    all_symbols = string.ascii_lowercase+string.ascii_uppercase
    user_name = ''.join(random.choice(all_symbols) for _ in range(7))
    return f"{user_name}@"


def generation_name_ad():
    all_symbols = string.ascii_lowercase+string.ascii_uppercase
    user_name = ''.join(random.choice(all_symbols) for _ in range(7))
    return f"{user_name}"


def generation_pass():
    all_symbols = string.ascii_lowercase+string.ascii_uppercase
    user_name = ''.join(random.choice(all_symbols) for _ in range(7))
    return f"{user_name}"

def random_category():
    return random.choice(category)


def random_city():
    return random.choice(city)


def random_price():
    return random.choice(price)


def random_description():
    return random.choice(description)