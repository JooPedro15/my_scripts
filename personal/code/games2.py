import random


class MyColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'


# Games list
games_id = {0: 'Exit',
            1: 'Rock, paper, Scissors',
            2: 'Quiz',
            3: 'Guess the number'}


def games_selection():
    while True:
        print('Available options:')
        for key, value in games_id.items():
            print(key, value)
        try:
            user_selection = int(input('Choose a game to play: '))
            if user_selection in games_id.keys():
                print('You selected {} game.'.format(games_id.get(user_selection)))
                if user_selection == 0:
                    print('Thank you for playing.')
                    break
                if user_selection == 1:
                    game_rps()
                elif user_selection == 2:
                    game_quiz()
                elif user_selection == 3:
                    game_guess_number()
            else:
                print('Choose a valid option.')
            print('----------------------------------------------------')
        except ValueError:
            print('Your selection must be a integer number.')


# Rock, Paper, Scissors
choices = ["rock", "paper", "scissors"]


def game_rps():

    i = True
    while i:
        user = input("Enter an option (rock, paper or scissors): ").lower()
        computer = (random.choice(choices))
        if user == "rock":
            if computer == "paper":
                print("User: " + user)
                print("Computer: " + computer)
                print("Lose\n")
            elif computer == "scissors":
                print("User: " + user)
                print("Computer: " + computer)
                print("Win\n")
            else:
                print("User: " + user)
                print("Computer: " + computer)
                print("DRAW\n")
        elif user == "paper":
            if computer == "rock":
                print("User: " + user)
                print("Computer: " + computer)
                print("Win\n")
            elif computer == "scissors":
                print("User: " + user)
                print("Computer: " + computer)
                print("Lose\n")
            else:
                print("User: " + user)
                print("Computer: " + computer)
                print("Draw\n")
        elif user == "scissors":
            if computer == "rock":
                print("User: " + user)
                print("Computer: " + computer)
                print("Lose\n")
            elif computer == "paper":
                print("User: " + user)
                print("Computer: " + computer)
                print("Win\n")
            else:
                print("User: " + user)
                print("Computer: " + computer)
                print("DRAW\n")
        else:
            print("Enter a valid option\n")

        keep_playing = input("Keep playing? y or n ").lower()
        if keep_playing != "y":
            break


# Quiz
def game_quiz():
    rounds = 0
    correct_answers_count = 0
    user_answers = []
    correct_answers = []

    for key in questions:
        print(key)
        for i in options[rounds]:
            print(i)
        user_answer = input("Your answer: ").upper()
        user_answers.append(user_answer)
        correct = questions.get(key)
        correct_answers.append(correct)
        correct_answers_count += answer_check(user_answer, correct)
        rounds += 1
    score_check(user_answers, correct_answers, correct_answers_count, rounds)


def answer_check(user_answer, correct):
    if user_answer == correct:
        print(MyColors.GREEN+"Correct\n"+MyColors.END)
        return 1
    else:
        print(MyColors.RED+"Wrong\n"+MyColors.END)
        return 0


def score_check(user_answers, correct_answers, correct_answers_count, rounds):
    print("Your answers: ", end="")
    for i in user_answers:
        print(i, end=" ")
    print()
    print("Correct answers: ", end="")
    for j in correct_answers:
        print(j, end=" ")
    score = (correct_answers_count / rounds)*100
    print("\n")
    print("Your score is:", score, "%")


questions = {
    "What is the capital of Portugal": "A",
    "Is the earth round?": "C"
}
options = [
    ["A. Lisbon", "B. Porto", "C. Faro", "D. Coimbra"],
    ["A. NO", "B. Maybe", "C. Yes", "D. I don't know"]
]


# Guess a number
def game_guess_number():
    print('In 5 rounds, try to guess a random number between 1 and 3.')
    counter = 1
    correct = 0

    while counter <= 5:
        print('Round: ', counter)
        try:
            user_choice = int(input('Pick your number: '))
        except ValueError:
            print(MyColors.RED + 'Must pick a number between 1 and 3.' + MyColors.END)
        else:
            generator = random.randint(1, 3)
            counter += 1
            correct += check_guess(user_choice, generator)
            print('----------------------------------------------------')
    print('Score: {} out of {}'.format(correct, (counter - 1)))


def check_guess(user, computer):
    if user == computer:
        print('User: ', user)
        print('Computer: ', computer)
        print(MyColors.GREEN + 'WIN' + MyColors.END)
        return 1
    else:
        print('User: ', user)
        print('Computer: ', computer)
        print(MyColors.RED + 'LOSE' + MyColors.END)
        return 0

games_selection()