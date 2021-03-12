import unittest
import click

from Game import Game


class GameTargetScoreLimitCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_maxTargetScore_validateTargetScoreLimit(self):
        localGame = Game(2, 101)
        with self.assertRaises(click.Abort):
            localGame.validateTargetScoreLimit()

    def test_validTargetScore_validateTargetScoreLimit(self):
        localGame = Game(2, 42)
        localGame.validateTargetScoreLimit()
        self.assertEqual(localGame.numberOfPlayers, 2)

    def test_minTargetScore_validateTargetScoreLimit(self):
        localGame = Game(3, 12)
        with self.assertRaises(click.Abort):
            localGame.validateTargetScoreLimit()
