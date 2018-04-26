# coding=utf-8
from card import Cards


class Player:
    def __init__(self, hand: Cards=Cards()) -> None:
        self._hand = hand

    def hand(self) -> Cards:
        return self._hand
