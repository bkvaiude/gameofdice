import unittest
import click

from Game import Game


class GamePlayerLimitCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_maxPlayerLimit_validatePlayersLimit(self):
        localGame = Game(10, 36)
        with self.assertRaises(click.Abort):
            localGame.validatePlayersLimit()

    def test_validPlayerLimit_validatePlayersLimit(self):
        localGame = Game(2, 36)
        localGame.validatePlayersLimit()
        self.assertEqual(localGame.numberOfPlayers, 2)

    def test_minPlayerLimit_validatePlayersLimit(self):
        localGame = Game(1, 36)
        with self.assertRaises(click.Abort):
            localGame.validatePlayersLimit()
