import unittest
import click

from Game import Game


class ConsecutiveSixPointsRewardCase(unittest.TestCase):
    def setUp(self):
        self.game = Game(3, 36)
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

    def test_reward_validateConsecutiveSixPointsRewardRule(self):
        self.game.playerId = "1"
        self.game.validateConsecutiveSixPointsRewardRule(6)
        self.assertEqual(self.game.processedPlayerCount, 1)

    def test_nextTurn_validateConsecutiveSixPointsRewardRule(self):
        self.game.playerId = "2"
        self.game.validateConsecutiveSixPointsRewardRule(5)
        self.assertEqual(self.game.processedPlayerCount, 2)
