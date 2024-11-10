def highest_even(li):
    """
    Find the highest even number from a list.
    :param li: list to be evaluated.
    :return: The highest integer.
    """
    highest = 0

    for item in li:
        if item % 2 == 0 and item > highest:
            highest = item
        return highest


def validate_download():
    """
    Simulates the behavior of a download validation script.
    :return: If the downloaded doc is present, as a boolean value.
    """
    ans = bool(input("Doc present?"))
    counter = 10

    if not ans:
        while counter >= 0:
            if not ans and counter > 0:
                counter -= 1
                ans = bool(input("Doc present?"))
            if not ans and counter == 0:
                print("Fail")
                counter = -1
            elif ans and counter > 0:
                counter = -1
    return ans

validate_download()