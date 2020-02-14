import random
import requests

MIN_VALUE = 0
MAX_VALUE = 7
COLUMN = 1
BASE = 10
FORMAT = "plain"
RND = "new"


# Function that calls Random Number Generator API
# to generate the random number combinations
# The argument 'complexity' decides the number of digits in random number
def generate_random_number(complexity):
    URL = "https://www.random.org/integers/"
    PARAM = {'num': complexity, 'min': MIN_VALUE, 'max': MAX_VALUE, 'col': COLUMN, 'base': BASE, 'format': FORMAT, 'rnd': RND}

    random_list = []

    try:
        r = requests.get(url=URL, params=PARAM)

        for i in r.iter_lines():
            random_list.append(int(i))

    except TimeoutError:
        random_list = [random.randint(MIN_VALUE, MAX_VALUE) for i in range(int(complexity))]

    return random_list
