# coding=utf-8
import enum

from card import Card
from player import Player

BLACKJACK = 21


class BlackjackRule:
    @staticmethod
    def point(player: Player) -> int:
        hand = player.hand()
        result = sum(min(card.rank().value, 10) for card in hand)
        if result <= 11 and Card.Rank.ACE in (card.rank() for card in hand):
            return result + 10
        return result

    @staticmethod
    def busts(player: Player) -> bool:
        return BlackjackRule.point(player) > BLACKJACK

    @staticmethod
    def judge(*, dealer: Player, guest: Player) -> Player:
        if BlackjackRule.busts(guest):
            return dealer
        if BlackjackRule.busts(dealer):
            return guest
        if BlackjackRule.point(dealer) < BlackjackRule.point(guest):
            return guest
        return dealer
