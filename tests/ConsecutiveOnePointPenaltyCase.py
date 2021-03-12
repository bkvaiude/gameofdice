import unittest
import click

from Game import Game


class ConsecutiveOnePointPenaltyCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(3, 36)
        self.game.processedPlayerCount = 1
        self.game.round = 1
        self.game.playerId = 1
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
                "is_game_completed": True,
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

    def test_zero_validateConsecutiveOnePointPenaltyRule(self):
        self.game.playerId = "0"
        self.assertFalse(self.game.validateConsecutiveOnePointPenaltyRule())
        self.assertEqual(self.game.processedPlayerCount, 1)

    def test_one_validateConsecutiveOnePointPenaltyRule(self):
        self.game.playerId = "1"
        self.assertFalse(self.game.validateConsecutiveOnePointPenaltyRule())
        self.assertEqual(self.game.processedPlayerCount, 1)

    def test_two_validateConsecutiveOnePointPenaltyRule(self):
        self.game.playerId = "2"
        self.assertTrue(self.game.validateConsecutiveOnePointPenaltyRule())
        self.assertEqual(self.game.processedPlayerCount, 2)
