from random import randint
from database import *


def greeting():
    def decor_wrapp(cb, string, decor_string):

        decor_string = "*" * len(string)

        def decor():
            print(f"""
            {decor_string}
            {cb()}
            {decor_string}
            """)

        return decor

    def get_str():
        string = f"Hallo, {client['name']}! " \
                 f"nice to meet u in our restaurant!".upper()
        return string

    def for_greeting():
        return get_str()

    greeting_client = decor_wrapp(for_greeting, get_str(), client["name"])

    return greeting_client()


def get_waitress(arr):
    waitress_list = []

    for w in arr:
        for key, value in w.items():
            if key == "name":
                waitress_list.append(value)

    random_waitress = randint(0, len(waitress_list) - 1)

    return waitress_list[random_waitress]


def waitress_greeting(new_w):
    return f"""
            Your waitress today is >>{new_w.upper()}<<
            """


def get_tips(new_w):

    for w in waitress:
        if w["name"] == new_w:
            for key, value in w.items():
                if key == "tips":
                    new_tips = value
                    return new_tips


def yes_or_not_list():
    new_list = """
            Do U want to eat/drink or you want to be HUCK???
            """

    return new_list


def get_menu(arr):
    eat, drinks = arr
    menu_list = []
    i = 0

    print("\n------dishes------".upper())

    for e in menu[f"{eat}"]:

        menu_list.append(e)
        print(f"{i + 1}) {e['name']} - {e['price']}$")
        i += 1

    print("\n------drinks------".upper())

    for d in menu[f"{drinks}"]:
        menu_list.append(d)
        print(f"{i + 1}) {d['name']} - {d['price']}$")
        i += 1

    return menu_list


def choose_goods(arr):
    user_choose = int(input("\nPlease input what U want\n"))

    choosen_goods = (arr[user_choose - 1])

    return choosen_goods


def choose_to_bag():
    new_bag = []
    user_choose = choose_goods(get_menu(menu))
    new_bag.append(user_choose)

    return new_bag


def add_to_user_bag(user, new_tips, sum):
    user["bag"] += choose_to_bag()

    print("you want:".upper())

    for b in user["bag"]:
        sum += round(b["price"] * new_tips)
        if sum > user["cash"]:
            print("YOU HAVE NO MONEY, PLEASE CHOOSE SOMETHING ELSE OR GO OUT!")
            sum -= round(b["price"] * new_tips)
            user["bag"].pop()
            print(user["bag"])
            continue
        else:
            print(f"{b['name']}, {b['price']}$")
    print(f"-----------------\nSum = {sum}".upper())

    return user
