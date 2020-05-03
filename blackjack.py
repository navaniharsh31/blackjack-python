#!/usr/bin/env python
import random
import sys

print("--------------------")
print("      BLACKJACK     ")
print("--------------------")
print()
while True:
    player_cards = []
    dealer_cards = []
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 10))
        if len(dealer_cards) == 2:
            print("Dealer has X and", dealer_cards[1])

    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 10))
        if len(player_cards) == 2:
            print("You have ", player_cards)
        if sum(player_cards) == 21:
            print("BLACKJACK")
            print("YOU WON")
            sys.exit()
        if sum(player_cards) == 11 and 1 in player_cards:
            index = player_cards.index(1)
            del player_cards[index]
            player_cards.append(11)
            print("YOU WON BLACKJACK")
            sys.exit()

    while sum(player_cards) <= 21:
        if sum(player_cards) > 21:
            print("YOU BUSTED")
            sys.exit()
        print("Do you want to")
        print("1. STAY")
        print("2. HIT")
        print()
        action = int(input("Enter your choice"))
        if action == 2:
            player_cards.append(random.randint(1, 10))
            print()
            print("You have", player_cards, "Your sum is", sum(player_cards))
            if sum(player_cards) == 21:
                print("----------")
                print("BLACKJACK")
                print("YOU WON")
                sys.exit()

            # print("Now your cards are", player_cards, "and sum is ", sum(player_cards))
        elif action == 1:
            break
        if 1 in player_cards:
            print("Do you want to count 1 as 11")
            print("Y -Yes,  N- No")
            c = (input())
            if c == "y" or c == "Y":
                index = player_cards.index(1)
                del player_cards[index]
                player_cards.append(11)
                print("Now your cards are", player_cards, "and sum is ", sum(player_cards))

            elif c == "N" or c == "n":
                if sum(player_cards) > 21:
                    print("YOU BUSTED")
                    sys.exit()
            # break
    if sum(player_cards) > 21:
        print("YOU BUSTED")
        sys.exit()
    print("Dealer has", dealer_cards, "sum is", sum(dealer_cards))
    while sum(dealer_cards) <= 16:
        dealer_cards.append(random.randint(1, 10))
        if sum(dealer_cards) <= 11 and 1 in dealer_cards:
            index = dealer_cards.index(1)
            del dealer_cards[index]
            dealer_cards.append(11)
            print()
        print("Now the dealer has", dealer_cards, "and sum is", sum(dealer_cards))
    print()
    if sum(dealer_cards) > 21:
        print("----------")
        print("DEALER BUSTED")
        print("YOU WON")

    elif sum(dealer_cards) == 21:
        print("----------")
        print("Dealer BLACKJACK")
        print("You Lost")

    elif sum(dealer_cards) == sum(player_cards):
        print("----------")
        print("PUSH")

    elif sum(dealer_cards) > sum(player_cards):
        print("----------")
        print("Dealer WON")
        print("----------")

    elif sum(player_cards) > sum(dealer_cards):
        print("YOU WON")
        print("----------")

    print("Do you want to play again? Y/N")
    play = input()
    if play == "n" or play == "N":
        print("Goodbye")
        sys.exit()
