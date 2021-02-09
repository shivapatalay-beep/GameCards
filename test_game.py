import main
import pytest


@pytest.fixture
def sorted_ranks():
    deck = [rank for rank in main.Rank]
    deck.append(deck.pop(0))
    return deck


def test_shuffle():
    deck = main.Deck()
    deckShuffle = main.Deck()
    deckShuffle.shuffle()
    assert deck != deckShuffle, "test shuffle failed"


def test_no_shuffle():
    deck = main.Deck()
    deckShuffle = main.Deck()
    assert deck == deckShuffle, "test no shuffle failed"


def test_get_card():
    deck = main.Deck()
    card = deck.cards[-1]
    top_card = deck.get_card()
    assert card == top_card, "test top card failed"


def test_exception_on_empty_deck():
    with pytest.raises(TypeError, match="There is no card left in the deck"):
        deck = main.Deck()
        for _ in range(53):
            deck.get_card()


def test_get_card_no_top():
    deck = main.Deck()
    card = deck.cards[0]
    top_card = deck.get_card()
    assert card != top_card, "test no top card failed"


def test_sort_empty():
    deck = main.Deck()
    deck.sort([])
    assert len(deck.cards) == 0, "test not empty deck failed"


def test_sort_all_card(sorted_ranks):
    sorted_deck = main.Deck()
    sorted_cards = [main.Card(suit, rank)
                    for suit in main.Suit for rank in sorted_ranks]
    sorted_deck.cards = sorted_cards

    deck = main.Deck()
    deck.sort([main.Suit.Spades, main.Suit.Diamonds,
               main.Suit.Hearts, main.Suit.Clubs])

    deck.print()
    assert sorted_deck == deck, "test sort all cards failed"


def test_sort_example():
    deck = main.Deck()
    result_deck = main.Deck()
    deck.cards = [main.Card(main.Suit.Spades, main.Rank._2),
                  main.Card(main.Suit.Diamonds, main.Rank._5),
                  main.Card(main.Suit.Spades, main.Rank.King),
                  main.Card(main.Suit.Hearts, main.Rank._3),
                  main.Card(main.Suit.Clubs, main.Rank.Ace)]

    deck.sort([main.Suit.Spades, main.Suit.Diamonds,
               main.Suit.Hearts, main.Suit.Clubs])

    result_deck.cards = [main.Card(main.Suit.Spades, main.Rank._2),
                         main.Card(main.Suit.Spades, main.Rank.King),
                         main.Card(main.Suit.Diamonds, main.Rank._5),
                         main.Card(main.Suit.Hearts, main.Rank._3),
                         main.Card(main.Suit.Clubs, main.Rank.Ace)]

    assert result_deck == deck, "test sort example failed"


def test_sort_example_failed():
    deck = main.Deck()
    result_deck = main.Deck()
    deck.cards = [main.Card(main.Suit.Spades, main.Rank._2),
                  main.Card(main.Suit.Diamonds, main.Rank._5),
                  main.Card(main.Suit.Spades, main.Rank.King),
                  main.Card(main.Suit.Hearts, main.Rank._3),
                  main.Card(main.Suit.Clubs, main.Rank.Ace)]

    deck.sort([main.Suit.Spades, main.Suit.Diamonds,
               main.Suit.Hearts, main.Suit.Clubs])

    result_deck.cards = [main.Card(main.Suit.Spades, main.Rank._2),
                         main.Card(main.Suit.Diamonds, main.Rank._5),
                         main.Card(main.Suit.Spades, main.Rank.King),
                         main.Card(main.Suit.Hearts, main.Rank._3),
                         main.Card(main.Suit.Clubs, main.Rank.Ace)]

    assert result_deck != deck, "test sort example failed"


def test_first_player_wins():
    player1 = main.Player("Alice")
    player2 = main.Player("Bob")

    player1.take_card(main.Card(main.Suit.Spades, main.Rank._2))
    player1.take_card(main.Card(main.Suit.Diamonds, main.Rank._5))
    player1.take_card(main.Card(main.Suit.Spades, main.Rank.King))

    player2.take_card(main.Card(main.Suit.Spades, main.Rank._2))
    player2.take_card(main.Card(main.Suit.Diamonds, main.Rank._4))
    player2.take_card(main.Card(main.Suit.Spades, main.Rank.King))

    game = main.Game()
    winner = game.how_wins(player1, player2)

    winner.print()

    assert winner == player1, "test first player wins"


def test_second_player_wins():
    player1 = main.Player("Alice")
    player2 = main.Player("Bob")

    player1.take_card(main.Card(main.Suit.Spades, main.Rank._2))
    player1.take_card(main.Card(main.Suit.Diamonds, main.Rank._5))
    player1.take_card(main.Card(main.Suit.Spades, main.Rank.King))

    player2.take_card(main.Card(main.Suit.Diamonds, main.Rank._2))
    player2.take_card(main.Card(main.Suit.Diamonds, main.Rank._4))
    player2.take_card(main.Card(main.Suit.Spades, main.Rank.King))

    game = main.Game()
    winner = game.how_wins(player1, player2)

    winner.print()

    assert winner == player2, "test second player wins"
