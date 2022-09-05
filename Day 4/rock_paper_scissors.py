import random

persons_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computers_choice = random.randint(0,2)
print(f"Computer chose {computers_choice}")

if persons_choice >= 3 or persons_choice < 0:
    print("You typed an invalid number. You lose!")
elif persons_choice == computers_choice:
    print("It's a draw.")
elif persons_choice == 0 and computers_choice == 2:
    print(f"Person chose {persons_choice} Rock and Computer chose {computers_choice} Scissors")
    print("You Won! Since Rock wins over Scissors.")
elif persons_choice == 2 and computers_choice == 0:
    print(f"Person chose {persons_choice} Scissors and Computer chose {computers_choice} Rock")    
    print("You lose! Since Rock wins over Scissors.")
elif computers_choice > persons_choice:
    print(f"Person chose {persons_choice} and Computer chose {computers_choice}")
    print("You lose!")
elif computers_choice < persons_choice:
    print(f"Person chose {persons_choice} and Computer chose {computers_choice}")
    print("You Won!")


