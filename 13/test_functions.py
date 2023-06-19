from database import waitress
from utilies import *


def get_waitress(arr):
    waitress_list = []

    for w in arr:
        for key, value in w.items():
            if key == "name":
                waitress_list.append(value)

    random_waitress = randint(0, len(waitress_list) - 1)

    return waitress_list[random_waitress]



get_tips(get_waitress)
