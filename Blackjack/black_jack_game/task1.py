import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

deck_prime = [
    'ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jck', 'q', 'k',
    'ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jck', 'q', 'k',
    'ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jck', 'q', 'k',
    'ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jck', 'q', 'k'
]

deck_test = ['ace', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jck', 'q', 'k']
random.shuffle(deck_test)

print(deck_test)


def intro():
    print(logo)
    print("Welcome to blackjack!")
    print()
    num_deck = input("How many decks would you like to play with?")

    return num_deck


def winner(deck):
    print("\n\n")
    print("YOU WON THIS HAND!!")
    print("\n\n")

    deck = shuffle_deck_new_game(deck)
    game(deck)


def bust(deck):
    print("\n\n")
    print("Oh dear... You went bust...")
    print("the dealer wins...")
    print("\n\n")

    deck = shuffle_deck_new_game(deck)
    game(deck)


def game(deck):
    my_hand = []
    dealer_hand = []

    while True:
        for i in range(0, 2):
            if len(deck) < 1:
                deck = shuffle_deck_new_game(deck_test)
            my_hand.append(deck.pop(0))
            if len(deck) < 1:
                deck = shuffle_deck_new_game(deck_test)
            dealer_hand.append(deck.pop(0))
        num, hand_val = hand_value(my_hand)
        my_standing(num, my_hand, hand_val, dealer_hand, deck)


def my_standing(num, my_hand, hand_val, dealer_hand, deck):
    if num == 1:
        print("your hand is", my_hand, "for a total of", hand_val[0])
        print("the dealer has a face down card and a", dealer_hand[1])
        if hand_val[0] == 21:
            winner(deck_test)
        else:
            deal_stand(my_hand, dealer_hand, deck)
    else:
        print("your hand is", my_hand, "for a total of", hand_val[0], "OR", hand_val[1])
        print("the dealer has a face down card and a", dealer_hand[1])
        if hand_val[0] == 21 or hand_val[1] == 21:
            winner(deck_test)
        else:
            deal_stand(my_hand, dealer_hand, deck)


def deal_stand(hand, dealer, deck):
    deal_or_stand = input("""
      Would you like the dealer to deal again or would you like to stand?
      (TYPE 'd' for 'Deal' OR 's' for 'Stand') 
      """)

    deal_or_stand = deal_or_stand.capitalize()

    if deal_or_stand == "D":
        hit_me(hand, dealer, deck)
        deal_stand(hand, dealer, deck)
    elif deal_or_stand == "S":
        stand()
    else:
        print("That is not a valid choice... Please try again.")
        deal_stand(hand, dealer, deck)


def hand_value(hand):
    aces = 0
    hand_tots = [0, 0]
    for card in hand:
        if card == "ace" and aces == 0:
            aces += 1
            hand_tots[0] += 1
            hand_tots[1] += 11
        elif card == "ace" and aces >= 1:
            hand_tots[0] += 1
            hand_tots[1] += 1
        elif card == "jck" or card == "q" or card == "k":
            hand_tots[0] += 10
            hand_tots[1] += 10
        else:
            hand_tots[0] += int(card)
            hand_tots[1] += int(card)

    for i in range(len(hand_tots)):
        try:
            if hand_tots[i] > 21:
                hand_tots.pop(i)
        except IndexError:
            bust(deck_test)

    return len(hand_tots), hand_tots


def hit_me(hand, dealer, deck):
    if len(deck) < 1:
        shuffle_deck_new_game(deck_test)  # this is addin cards to the deck that are actually in my hand...
    hand.append(deck.pop(0))
    num, hand_val = hand_value(hand)
    my_standing(num, hand, hand_val, dealer, deck)


def stand():
    return


def shuffle_deck_new_game(deck):
    print("Shuffling Deck!")
    print(deck)
    random.shuffle(deck)
    return deck


def shuffle_deck(deck, myhand, dealershand):
    taken_cards = myhand + dealershand

    present_deck = [x for x in taken_cards if x not in deck]

    print(present_deck)

    return present_deck


game(deck_test)
