# coding=utf-8
import enum


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
