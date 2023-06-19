from utilies import *

new_w = get_waitress(waitress)
new_tips = get_tips(new_w)


def get_start():
    is_running = True

    print(yes_or_not_list())

    while is_running:

        try:
            user_choose = int(input("""
            Please enter a number of action:
            1) Get menu
            2) Quit
            """))

        except:
            print("""
            Incorrect data, AZ-Hole! Try again!!!
            """)
            continue

        match(user_choose):
            case 1:
                add_to_user_bag(client, new_tips, summm)

            case 2:
                if client["bag"] == []:
                    is_running = False

                    print("""
            huck u, az-hole .!..
            i don't want to see you again!!!
            """.upper())

                    continue

                else:
                    print("you choose:".upper())

                    new_arr = []

                    for el in client["bag"]:
                        for key, value in el.items():

                            if key == "price":
                                new_arr.append(round(value * new_tips))

                            if key == "name":
                                print("* " + value + " *")

                    new_summ = sum(new_arr)

                    new_cash = client["cash"] - new_summ

                    print(f"---------\n"
                          f"sum = {new_summ}$\n"
                          f"\nyou have {new_cash}$\n"
                          f"\ngoodbye, az-hole!\n"
                          f"it will be nice to meet u again".upper())

                    is_running = False

                    continue
                    # sum(client["bag"])

            case _:
                print("""
            Choose number of list, please, AZ-Hole!!!
            """)
                continue


def main():
    greeting()

    print(waitress_greeting(new_w))

    get_start()


if __name__ == "__main__":
    main()
