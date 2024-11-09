
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# 0 displays a space
# 1 displays a *


def print_multi_lines(pic):
    """
    Info: Prints a list matrix in a series of strings
          The printed character is a *
    :param pic: Source list
    :return: printed strings
    """
    empty = ' '
    fill = '*'
    for row in pic:
        for pixel in row:
            if pixel == 0:  # print the char and remain in the same row
                print(empty, end='')
            elif pixel == 1:
                print(fill, end='')
        print('')  # add a new line


def print_multi_lines2(pic):
    """
    Info: Prints a list matrix in a series of strings
          The printed character is a *
    :param pic: Source list
    :return: printed strings
    """
    empty = ' '
    fill = '*'
    line_list = []  # placeholder for the row char
    line_str = ''  # actual row to be printed
    for row in pic:
        for pixel in row:  # will add the char to a list
            if pixel == 0:
                line_list.append(empty)
            elif pixel == 1:
                line_list.append(fill)
        new_line = line_str.join(line_list)  # add the row list to the row string
        print(new_line)
        line_list.clear()  # clear the row list to build the next row