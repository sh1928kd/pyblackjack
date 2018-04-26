# coding=utf-8
import typing

from card import (
    Cards,
    Deck,
)


class Player:
    @staticmethod
    def draw(
        player: 'Player',
        deck: Deck,
        num: int=1
    ) -> typing.Tuple['Player', Deck]:
        if num not in range(1, len(deck) + 1):
            return player, deck
        return Player(player.hand() + Cards(deck[:num])), Deck(deck[num:])

    def __init__(self, hand: Cards=Cards()) -> None:
        self._hand = hand

    def hand(self) -> Cards:
        return self._hand
