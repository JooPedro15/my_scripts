import random

"""
Games index:
Rock, Paper, Scissors
"""


def rps():
    """
    Info: Rock, paper, Scissors game against the computer.
    :return: Computer choice, User choice and outcome.
    """
    win = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input('Type an option: rock, paper, scissors').lower()
    if win[user_choice] == computer_choice:
        print(f"Computer choice: {computer_choice}\n"
              f"User choice: {user_choice}\n"
              f"You WON!")
    if win[computer_choice] == user_choice:
        print(f"Computer choice: {computer_choice}\n"
              f"User choice: {user_choice}\n"
              f"You LOST!")
    else:
        print(f"Computer choice: {computer_choice}\n"
              f"User choice: {user_choice}\n"
              f"DRAW!")


def guess_num():
    """
    Info: This is a game where you try to guess the computer choice.
    The computer pick an integer number between 1 and 3.
    :return: User choice, computer choice and outcome
    """
    while True:
        user_choice = int(input('Type a number  between 1 and 3\n'))
        computer_choice = int(random.choice(range(1, 3)))
        if user_choice == computer_choice:
            print(f'User choose {user_choice}\n'
                  f'Computer choose {computer_choice}\n'
                  f'WON!')
        else:
            print(f'User choose {user_choice}\n'
                  f'Computer choose {computer_choice}\n'
                  f'Lose!')
        out = input('Play again? y or n')
        if out == 'n':
            return False