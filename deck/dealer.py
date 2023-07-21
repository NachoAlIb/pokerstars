import random


def get_shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal_cards_player(deck):
    play_on_hand = [deck[0], deck[1]]
    deck.pop(0)
    deck.pop(0)
    return play_on_hand


def deal_pre_flop(deck):
    pre_flop = [deck[0], deck[1], deck[2]]
    deck.pop(0)
    deck.pop(0)
    deck.pop(0)
    return pre_flop



