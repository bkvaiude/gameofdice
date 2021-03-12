import unittest
import click

from Game import Game


class ContextSetupForConsecutiveOnePointPenaltyCase(unittest.TestCase):
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

    def test_incremented_setContextForConsecutiveOnePointPenaltyRule(self):
        self.game.playerId = "0"
        self.game.setContextForConsecutiveOnePointPenaltyRule(1)
        self.assertEqual(self.game.players[self.game.playerId]["one_counter"], 1)
        self.game.setContextForConsecutiveOnePointPenaltyRule(1)
        self.assertEqual(self.game.players[self.game.playerId]["one_counter"], 2)

    def test_noChange_setContextForConsecutiveOnePointPenaltyRule(self):
        self.game.playerId = "1"
        self.game.setContextForConsecutiveOnePointPenaltyRule(5)
        self.assertEqual(self.game.players[self.game.playerId]["one_counter"], 1)


if __name__ == "__main__":
    unittest.main()