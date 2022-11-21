import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks answer against against guess. Returns the number of guess remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    print(f"The correct answer is {number}")

    attempts = set_difficulty()

    guessed_num = 0
    while guessed_num != number:
        print(f"You have {attempts} attempts to guess the number.")
        guessed_num = int(input("Make a guess: "))
        attempts = check_answer(guessed_num, number, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            exit()
        elif guessed_num != number:
            print("Guess again.\n")

game()
# print("You've run out of guesses, you lose.")



    
