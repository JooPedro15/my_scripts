class MyColors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"


countries_list = {"India": 0,
                  "Portugal": 1,
                  "England": 2}

countries_info = (("India", "New Deli", "Indian Rupee"),
                  ("Portugal", "Lisbon", "Euro"),
                  ("England", "London", "Pound"))
request = ()


def request_country():

    while True:
        requested_country = input("Enter a country: ").capitalize()
        if requested_country in countries_list.keys():
            selected_country = countries_list.get(requested_country)
            print("Country:", countries_info[selected_country][0])
            print("Capital:", countries_info[selected_country][1])
            print("Currency:", countries_info[selected_country][2])
            print()
        elif requested_country == "Exit" or requested_country == "":
            print("Goodbye")
            break
        else:
            print(MyColors.RED+"Not a valid country.\n"+MyColors.END)
            print("Here is a list of the available countries:")
            for i in countries_list.keys():
                print(i)
            print()