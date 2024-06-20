import random

my_list1 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]
my_list2 = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]

def card_value(card):
    if card == "A":
        return 14  
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    else:
        return card

random.shuffle(my_list1)
random.shuffle(my_list2)

while True:
    player1_card = random.choice(my_list1)
    player2_card = random.choice(my_list2)

    player1_value = card_value(player1_card)
    player2_value = card_value(player2_card)

    print(f'Player 1 drew: {player1_card}')
    print(f'Player 2 drew: {player2_card}')

    if player1_value > player2_value:
        print("Player 1 is the winner")
        break
    elif player1_value < player2_value:
        print("Player 2 is the winner")
        break
    else:
        print("It's a tie! Drawing new cards...")
