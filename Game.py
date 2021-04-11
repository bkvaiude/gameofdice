import click
import random
from collections import OrderedDict
from operator import getitem


class Game:
    def __init__(self, numberOfPlayers, targetScore):
        self.numberOfPlayers = numberOfPlayers
        self.targetScore = targetScore
        self.players = {}

    def start(self):
        self.validatePlayersLimit()
        self.validateTargetScoreLimit()
        self.setPlayersName()
        self.decidePlayersTurnOrder()
        self.welcomeAllPlayers()
        self.boostrap()
        NO_OF_PLAYERS = self.numberOfPlayers
        while self.numberOfPlayers > 0:
            self.roundSetup()
            while self.processedPlayerCount < NO_OF_PLAYERS:
                self.setNextPlayer()
                if self.validateGameCompletedByPlayer():
                    continue
                if self.validateConsecutiveOnePointPenaltyRule():
                    continue
                self.rollTheDice()
            self.leaderboard()

    def validatePlayersLimit(self):
        if self.numberOfPlayers > 6 or self.numberOfPlayers < 2:
            click.echo(
                "Wow, We also want to build bigger game! Support for %s players, huh? \nLet's work together to build better one :)"
                % str(self.numberOfPlayers)
            )
            raise click.Abort()

    def validateTargetScoreLimit(self):
        if self.targetScore < 18 or self.targetScore > 100:
            click.echo(
                "Wow, We also want to build bigger game! Support for %s target score, huh? \nLet's work together to build better one :)"
                % str(self.targetScore)
            )
            raise click.Abort()

    def setPlayersName(self):
        for x in range(self.numberOfPlayers):
            value = click.prompt(
                "Please enter a player %s name" % str(x + 1),
                default=random.choice(
                    ["Shiva", "Shankar", "Trinetra", "Rudra", "Mahadev", "Nilkantha"]
                ),
            )
            self.players[x] = {"name": value, "steps": []}

    def decidePlayersTurnOrder(self):
        listOfPlayers = list(self.players.items())
        random.shuffle(listOfPlayers)
        self.players = dict(listOfPlayers)

    def rollTheDice(self):
        click.pause(">>>>It is %s's turn" % self.players[self.playerId]["name"])
        luckyNumber = random.randrange(1, 6)
        click.echo("---->You scored %s point[s]." % str(luckyNumber))
        self.saveScore(luckyNumber)
        self.checkGameCompletedByPlayer()
        self.setContextForConsecutiveOnePointPenaltyRule(luckyNumber)
        if self.validateConsecutiveSixPointsRewardRule(luckyNumber):
            self.validateLastNStepsScoreMatchingToGivenPointsRewardRule(luckyNumber)

    def saveScore(self, luckyNumber):
        self.players[self.playerId]["score"] = (
            self.players[self.playerId].get("score", 0) + luckyNumber
        )
        self.players[self.playerId]["steps"].append(luckyNumber)  # todo

    def checkGameCompletedByPlayer(self):
        if self.targetScore <= self.players[self.playerId]["score"]:
            self.numberOfPlayers = self.numberOfPlayers - 1
            self.players[self.playerId]["is_game_completed"] = True

    def setContextForConsecutiveOnePointPenaltyRule(self, luckyNumber):
        if luckyNumber == 1:
            self.players[self.playerId]["one_counter"] = (
                self.players[self.playerId].get("one_counter", 0) + luckyNumber
            )

    def validateConsecutiveSixPointsRewardRule(self, luckyNumber):
        if 6 != luckyNumber:
            self.processedPlayerCount = self.processedPlayerCount + 1
            result = False
        else:
            result = True
            click.echo("Hurray! you have been rewarded another turn to roll the dice.")
        return result

    def validateLastNStepsScoreMatchingToGivenPointsRewardRule(self, luckyNumber):
        """
        strore the score for each round
        steps = [1,2,1,4]

        travel through the array from reverse for N times & do the sum
        If the sum === given score than offer another chance
        """
        configSteps = -3
        configScoreOfSum = 10
        steps = self.players[self.playerId]["steps"][configSteps:]
        result = sum(steps)
        if self.round > 2 and result == configScoreOfSum:
            result = True
            click.echo(
                "Hurray! you have been rewarded another turn to roll the dice because you score 10 points in last 3 steps."
            )
        else:
            result = False
            self.processedPlayerCount = self.processedPlayerCount + 1

    def validateConsecutiveOnePointPenaltyRule(self):
        self.players[self.playerId][
            "round"
        ] = self.round  # todo redesign this in next phase
        consecutive_one_rule_validation = self.players[self.playerId].get(
            "one_counter", 0
        )
        result = False
        if consecutive_one_rule_validation >= 2:
            self.players[self.playerId]["one_counter"] = 0
            click.echo(
                "---->Skipping %s's turn for rolling 1 two consecutive times!"
                % self.players[self.playerId]["name"]
            )
            self.processedPlayerCount = self.processedPlayerCount + 1
            result = True
        return result

    def setNextPlayer(self):
        self.playerId = self.listOfPlayerKeys[self.processedPlayerCount]

    def validateGameCompletedByPlayer(self):
        isGameCompletedByPlayer = self.players[self.playerId].get(
            "is_game_completed", False
        )
        result = False
        if isGameCompletedByPlayer:
            click.echo(
                "---->Skipping %s's turn, s/he already scored max score!"
                % self.players[self.playerId]["name"]
            )
            self.processedPlayerCount = self.processedPlayerCount + 1
            result = True
        return result

    def boostrap(self):
        self.round = 0
        self.listOfPlayerKeys = list(self.players.keys())

    def roundSetup(self):
        if click.confirm("Do you want to clear a terminal?", default=False):
            click.clear()
        self.processedPlayerCount = 0
        self.playerId = self.listOfPlayerKeys[self.processedPlayerCount]
        self.round = self.round + 1
        click.echo("\n----Round {round}----\n".format(round=self.round))

    def welcomeAllPlayers(self):
        welcome = """
            Game will commence on any key press
            - Each player need to score max. {score} points
            - If a player rolls the value "6" then they immediately get another chance to roll again and
            move ahead in the game.
            - If a player rolls the value "1" two consecutive times then they are forced to skip their next
            turn as a penalty.
            - Hit any key to roll the dice!

            Press any key to start the game!
        """
        click.pause(welcome.format(score=self.targetScore))

    def leaderboard(self):
        """
        Players Round Score Rank
        Ram     10      36  1
        Shiva   12      39  2
        """
        click.echo("\n----Leaderboard----")
        players = OrderedDict(
            sorted(self.players.items(), key=lambda x: getitem(x[1], "round"))
        )
        columns = ["Rank", "Name", "Round", "Score"]
        row_format = "{:>15}" * len(columns)
        click.echo(row_format.format(*columns))
        rank = 1
        for k, v in players.items():
            click.echo(row_format.format(rank, v["name"], v["round"], v["score"]))
            rank = rank + 1
