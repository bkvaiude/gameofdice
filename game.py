import click
from Game import Game


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--number-of-players",
    "numberOfPlayers",
    type=int,
    default=2,
    prompt="How many players are joining the game party?",
    help="Number of players join the games. Minimum 2 or Maximum 6 are allowed!",
)
@click.option(
    "--target-score",
    "targetScore",
    type=int,
    default=36,
    prompt="How many players are joining the game party?",
    help="Target score of the games. Minimum 18 or Maximum 100 are allowed!",
)
def start(numberOfPlayers,targetScore):
    game = Game(numberOfPlayers,targetScore)
    game.start()


if __name__ == "__main__":
    cli()
