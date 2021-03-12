import click
import random
from collections import OrderedDict
from operator import getitem
from Game import Game


def randamize(dictionary):
    d = {"a": 1, "b": 2, "c": 3, "d": 4}
    l = list(dictionary.items())
    random.shuffle(l)
    return dict(l)


def welcomeAllPlayers():
    welcome = """
Game will commence on the enter key press
- Each player need to score max. 36 points
- If a player rolls the value "6" then they immediately get another chance to roll again and
move ahead in the game.
- If a player rolls the value "1" two consecutive times then they are forced to skip their next
turn as a penalty.
- Hit any key to roll the dice!
Do you want to continue?
    """
    return welcome


def scoreboard(players):
    """
    Players Round Score Rank
    Ram     10      36  1
    Shiva   12      39  2
    """
    players = OrderedDict(sorted(players.items(), key=lambda x: getitem(x[1], "round")))
    columns = ["Rank", "Name", "Round", "Score"]
    row_format = "{:>15}" * len(columns)
    print(row_format.format(*columns))
    # print "{:<8} {:<15} {:<10}".format("Key", "Label", "Number")
    rank = 1
    for k, v in players.items():
        print(row_format.format(rank, v["name"], v["round"], v["score"]))
        rank = rank + 1


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "-nop",
    "--number-of-players",
    "nop",
    type=int,
    default=2,
    prompt="How many players are joining the game party?",
    help="Number of players join the games. Minimum 2 or Maximum 6 are allowed!",
)
def game(nop):
    game = Game(nop)
    game.start()


def game2(nop):
    players = {}
    if nop > 6:
        click.echo(
            "Wow, we didn't see that coming! Support for %s players. 0.o Let's work together to fix it :)"
            % str(nop)
        )
        raise click.Abort()

    for x in range(nop):
        value = click.prompt(
            "Please enter a player %s name" % str(x + 1),
            default=random.choice(
                ["Shiva", "Shankar", "Trinetra", "Rudra", "Mahadev", "Nilkantha"]
            ),
        )
        players[x] = {"name": value}
    players = randamize(players)
    click.echo("Hello %s!" % str(players))
    welcome_message = welcomeAllPlayers()
    click.pause(welcome_message)
    numberOfUsersWhoYetToCompletedAGame = nop
    round = 0
    listOfPlayerKeys = list(players.keys())
    countOfPlayers = len(listOfPlayerKeys)

    while numberOfUsersWhoYetToCompletedAGame > 0:
        # todo testcase of schema
        # click.clear()
        processedPlayerCount = 0
        playerId = listOfPlayerKeys[processedPlayerCount]
        round = round + 1
        click.echo("\n\n----Round {round}----".format(round=round))
        while processedPlayerCount < nop:
            playerId = listOfPlayerKeys[processedPlayerCount]
            # todo testcase for rand generator
            isGameCompletedByPlayer = players[playerId].get("is_game_completed", False)
            if isGameCompletedByPlayer:
                click.echo(
                    "Skipping %s's turn, s/he already scored max score!"
                    % players[playerId]["name"]
                )
                processedPlayerCount = processedPlayerCount + 1
                continue

            players[playerId]["round"] = round
            consecutive_one_rule_validation = players[playerId].get("one_counter", 0)
            if consecutive_one_rule_validation == 2:
                players[playerId]["one_counter"] = 0
                click.echo(
                    "Skipping %s's turn for rolling 1 two consecutive times!"
                    % players[playerId]["name"]
                )
                processedPlayerCount = processedPlayerCount + 1
                continue
            click.pause(
                "It's %s's turn, hit enter key to roll the dice!"
                % players[playerId]["name"]
            )
            luckyNumber = random.randrange(1, 6)
            click.echo("And the number is %s!" % str(luckyNumber))
            players[playerId]["score"] = players[playerId].get("score", 0) + luckyNumber
            if 36 <= players[playerId]["score"]:
                numberOfUsersWhoYetToCompletedAGame = (
                    numberOfUsersWhoYetToCompletedAGame - 1
                )
                players[playerId]["is_game_completed"] = True
            if luckyNumber == 1:
                players[playerId]["one_counter"] = (
                    players[playerId].get("one_counter", 0) + luckyNumber
                )
            if 6 != luckyNumber:
                processedPlayerCount = processedPlayerCount + 1
        click.echo(
            "Well done! Here is the scoreboard after round {round}.".format(round=round)
        )
        scoreboard(players)


if __name__ == "__main__":
    cli()
