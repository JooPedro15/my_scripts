class MyColors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"


formulas = {"Triangle Area": 1,
            "Square Area": 2}


def calculator():
    while True:
        print("Available formulas:")
        for keys, values in formulas.items():
            print(values, keys)
        print()

        try:
            user_selection = int(input("Select a formula number: "))
        except ValueError:
            print("=========================================")
            print(MyColors.RED + "Your selection must be an integer number." + MyColors.END)
            print("=========================================")
        else:
            selector(user_selection)
        print()
        escape = input("New calculation? Type y to continue : ").lower()
        if escape == "y":
            continue
        else:
            break


def selector(selection):
    if selection == 1:
        print()
        area_triangle()
    elif selection == 2:
        print()
        area_square()
    else:
        print("Not an available formula.")


def area_triangle():
    print("Triangle Area:")
    try:
        s1 = float(input("Side A (cm)= "))
    except ValueError:
        print("=========================================")
        print(MyColors.RED + "You must insert a number with a . as a decimal separator." + MyColors.END)
        print("=========================================")
    else:
        try:
            s2 = float(input("Side B (cm)= "))
        except ValueError:
            print("=========================================")
            print(MyColors.RED + "You must insert a number with a . as a decimal separator." + MyColors.END)
            print("=========================================")
        else:
            a = (s1 * s2) / 2
            print("Area = {:.2f}cm2".format(a))


def area_square():
    print("Square Area:")
    try:
        s = float(input("Side (cm)= "))
    except ValueError:
        print("=========================================")
        print(MyColors.RED + "You must insert a number with a . as a decimal separator." + MyColors.END)
        print("=========================================")
    else:
        a = s * s
        print("Area = {:.2f}cm2".format(a))
        return a


calculator()