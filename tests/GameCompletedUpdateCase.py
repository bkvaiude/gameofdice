import unittest
import click

from Game import Game


class GameCompletedUpdateCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(3)
        self.game.processedPlayerCount = 1
        self.game.round = 1
        self.game.players = {
            "0": {
                "name": "Bhushan",
                "score": 22,
                "round": 9,
                "is_game_completed": False,
            },
            "1": {
                "name": "Shiva",
                "score": 36,
                "round": 9,
                "is_game_completed": False,
                "one_counter": 1,
            },
            "2": {
                "name": "Rama",
                "score": 30,
                "round": 9,
                "is_game_completed": False,
                "one_counter": 2,
            },
        }

    def test_completed_checkGameCompletedByPlayer(self):
        self.game.playerId = "1"
        self.game.checkGameCompletedByPlayer()
        self.assertTrue(self.game.players[self.game.playerId]["is_game_completed"])

    def test_incomplete_checkGameCompletedByPlayer(self):
        self.game.playerId = "2"
        self.game.checkGameCompletedByPlayer()
        self.assertFalse(self.game.players[self.game.playerId]["is_game_completed"])
