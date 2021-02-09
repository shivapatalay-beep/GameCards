import enum
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'Card({self.suit}, {self.rank})'


class Suit(enum.Enum):
    Spades = 1
    Diamonds = 2
    Heart = 3
    Clubs = 4

    def __str__(self):
        return self.name


class Rank(enum.Enum):
    Ace = 14
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    Jack = 11
    Queen = 12
    King = 13

    def __str__(self):
        return self.name[1:] if self.name.startswith('_') else self.name


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in Suit for rank in Rank]

    def shuffle(self):
        random.shuffle(self.cards)

    def getCard(self):
        if len(self.cards) == 0:
            raise Exception("There is no card left in the deck")
        return self.cards.pop()

    def sort(self, suitOrder):
        cards = []
        for suit in suitOrder:
            suitCards = [
                card for card in self.cards if suit.name == card.suit.name]
            suitCards.sort(key=lambda x: x.rank.value)
            cards.extend(suitCards)

        self.cards = cards

    def print(self):
        for idx, card in enumerate(self.cards):
            print(f'{idx+1}.- {card}')


class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.score = 0

    def takeCard(self, card):
        self.cards.append(card)
        self.score += card.suit.value * card.rank.value

    def print(self):
        print(f'Player: {self.name} - Score {self.score}')
        for idx, card in enumerate(self.cards):
            print(f'{idx+1}.- {card}')


class Game:

    def howWins(_, player1, player2):
        return player1 if player1.score > player2.score else player2

    def start(self):
        deck = Deck()

        # Print deck
        deck.print()

        # Shuffle deck
        deck.shuffle()
        deck.print()

        # # Pop a card
        card = deck.getCard()
        print(card)

        # # sort
        deck.sort([Suit.Spades, Suit.Diamonds, Suit.Heart, Suit.Clubs])
        deck.print()

        # pop all cards until exception
        for _ in range(52):
            deck.getCard()

        deck.shuffle()
        player1 = Player("Alice")
        player2 = Player("Bob")

        for _ in range(3):
            player1.takeCard(deck.getCard())
            player2.takeCard(deck.getCard())

        player1.print()
        player2.print()

        winner = self.howWins(player1, player2)

        print(">>>>>>Player wins<<<<<<")
        winner.print()


def main():
    Game().start()


if __name__ == "__main__":
    main()
