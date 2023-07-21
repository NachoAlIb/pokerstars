from deck.dealer import *
from deck.pokersetuppreflopoutput import PokerSetupPreFlopOutput


def play_poker():

    playing_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    shuffle_deck = playing_deck
    shuffle_deck = get_shuffle_deck(shuffle_deck)

    chispi_hand = deal_cards_player(shuffle_deck)

    pre_flop = deal_pre_flop(shuffle_deck)

    output = PokerSetupPreFlopOutput()
    output.cards_on_deck = shuffle_deck
    output.cards_on_hand = chispi_hand
    output.pre_flop = pre_flop

    print(output.cards_on_hand)
    print(output.pre_flop)
    print(output.cards_on_deck)

if __name__ == '__main__':
    play_poker()

