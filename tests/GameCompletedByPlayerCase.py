import unittest
import click

from Game import Game


class GameCompletedByPlayerCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(3, 36)
        self.game.processedPlayerCount = 1
        self.game.playerId = 1
        self.game.players = {
            "0": {
                "name": "Bhushan",
                "score": 22,
                "round": 9,
                "is_game_completed": False,
            },
            "1": {"name": "Shiva", "score": 36, "round": 9, "is_game_completed": True},
            "2": {"name": "Rama", "score": 30, "round": 9, "is_game_completed": False},
        }

    def test_completeness_validateGameCompletedByPlayer(self):
        self.game.playerId = "1"
        self.assertTrue(self.game.validateGameCompletedByPlayer())
        self.assertEqual(self.game.processedPlayerCount, 2)

    def test_incompleteness_validateGameCompletedByPlayer(self):
        self.game.playerId = "2"
        self.assertFalse(self.game.validateGameCompletedByPlayer())
        self.assertEqual(self.game.processedPlayerCount, 1)
