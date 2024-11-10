class MyColors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"


def new_game():
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


def answer_check(user_answer,correct):
    if user_answer == correct:
        print(MyColors.GREEN+"Correct\n"+MyColors.END)
        return 1
    else:
        print(MyColors.RED + "Wrong" + MyColors.END)
        return 0


def score_check(user_answers, correct_answers, correct_answers_count, rounds):
    print("Your answers: ", end="")
    for i in user_answers:
        print(i, end=" ")
    print("Correct answers: ", end="")
    for j in correct_answers:
        print(j, end=" ")
    score = round(correct_answers_count/rounds)*100
    print("\n")
    print("Your score is:", score, "%")


questions = {
    "What is the capital of Portugal": "A",
    "Is the earth round?": "C"
}
options = [
    ["A. Lisbon", "B. Porto", "c. Faro", "C. Coimbra"],
    ["A. NO", "B. Maybe", "C. Yes", "D. I don't know"]
]