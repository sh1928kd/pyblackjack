# coding=utf-8
import enum

from card import (
    Card,
    Deck,
)
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


@enum.unique
class GuestDecision(enum.Enum):
    HIT = enum.auto()
    STAND = enum.auto()

    @staticmethod
    def decide() -> 'GuestDecision':
        command_table = dict((v.name.lower()[0], v) for v in GuestDecision)
        print(f'{"/".join(v.name.title() for v in command_table.values())}?')
        while True:
            command = input(f'[{",".join(command_table.keys())}]: ')
            if command in command_table:
                return command_table[command]
            else:
                print(f'Oops, "{command}" is invalid!')


class Blackjack:
    @staticmethod
    def _result(*, dealer: Player, guest: Player):
        print('')
        print("* Judge *")
        print(f'{BlackjackRule.judge(dealer=dealer, guest=guest).name()} win!')

    @staticmethod
    def play():
        print('********************')
        print('* Blackjack')

        dealer = Player(name='Dealer')
        guest = Player(name='Guest')
        deck = Deck().shuffle().shuffle()

        for _ in range(2):
            dealer, deck = Player.draw(dealer, deck)
            guest, deck = Player.draw(guest, deck)

        Blackjack._result(dealer=dealer, guest=guest)
