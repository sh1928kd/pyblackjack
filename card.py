# coding=utf-8
import collections
import enum
import typing
import random


class Card:
    @enum.unique
    class Suit(enum.Enum):
        CLUB = '♧'
        DIA = '♢'
        HEART = '♡'
        SPADE = '♤'

        def __str__(self):
            return self.value

    @enum.unique
    class Rank(enum.Enum):
        ACE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13

    def __init__(self, suit: Suit, rank: Rank) -> None:
        self._suit = suit
        self._rank = rank

    def suit(self) -> Suit:
        return self._suit

    def rank(self) -> Rank:
        return self._rank


class Cards(collections.abc.Sequence):
    def __getitem__(self, key):
        return self._cards[key]

    def __len__(self):
        return len(self._cards)

    def __init__(self, cards: typing.Sequence[Card]=tuple()) -> None:
        self._cards = cards


class Deck(Cards):
    @staticmethod
    def oneset() -> typing.Sequence[Card]:
        return tuple(
            Card(suit, rank)
            for suit in Card.Suit for rank in Card.Rank)

    def __init__(self, cards: typing.Sequence[Card]=None) -> None:
        super().__init__(cards or Deck.oneset())

    def shuffle(self) -> 'Deck':
        return Deck(tuple(random.sample(self, k=len(self))))
