import random

from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)

lives = 6 

print(logo)

print(f"Psst, the solution is {chosen_word}.")

display = []
for char in chosen_word:
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter.\n").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the chosen word. You lose a life.")
        lives -= 1
        print(f"You have {lives} lives remaining.")
        if lives == 0:
            end_of_game = True
            print("You lose")
        
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])

# Another Method

# while "_" in display:
#     guess = input("Guess a letter.").lower()
#     print(guess)

#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#         else:
#             print("Wrong")

#     print(display)
# print("You won!!!")