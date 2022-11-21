import random

print("Do you want to play a game of Blackjack?")

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and total > 21:
        cards.remove(11)
        print("Removed 11")
        print(cards)
        cards.append(1)
        print("Added 1")

    return total

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!!"
    elif computer_score == 0:
        return "Player loses, opponent has Blackjack"
    elif user_score == 0:
        return "Player wins with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over, You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose."    

def play_game():

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score =  calculate_score(computer_cards)

    print(f" Your final hand : {user_cards}, final score : {user_score}")
    print(f" Computer's final hand : {computer_cards}, final score : {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()









