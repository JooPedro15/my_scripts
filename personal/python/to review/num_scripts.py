# Find an even number
def is_even(num):
    """
    Info: Checks is a number is even
    :param num: number to be checked
    :return: True if the number is even; False if the number is odd
    """
    return num % 2 == 0


# Find the highest even number from a list
def highest_even(li):
    """
    Info: Returns the highest even number from a list
    :param li: List of numbers
    :return: The highest even
    """
    new_list = []
    for i in li:
        if i % 2 == 0:
            new_list.append(i)
    new_list.sort()
    return new_list[-1]


# same
def highest_even2(li):
    """
    Info: Returns the highest even number from a list
    :param li: List of numbers
    :return: The highest even
    """
    highest = 0
    for item in li:
        if item % 2 and item > highest:
            highest = item
    return highest