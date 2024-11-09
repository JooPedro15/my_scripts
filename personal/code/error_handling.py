"""
Error handling
"""

while True:
    try:
        age = int(input('What is your age?'))
        10 / age
    except ZeroDivisionError:
        print('Please enter an non zero integer')
    except ValueError:
        print('Please enter a integer')
    else:
        print('Good')
        break
    finally:
        print('Done')


def sum(num1, num2):
    try:
        return num1 / num2
    except TypeError as err:
        print(f'Please enter numbers.\n{err}')


print(sum(1, 0))


def sum(num1, num2):
    try:
        return num1 / num2
    except TypeError as err:
        print(f'Please enter numbers.\n{err}')


print(sum(1, 0))