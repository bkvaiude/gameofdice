# Welcome to game of dice!

### If you are looking for python dice game, then you reach to right place!

## What can you learn from this game

* https://click.palletsprojects.com/en/7.x/quickstart/#
* How to create python package (click + setuptools) https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration
* Basic understanding of the setuptools
* unittest https://docs.python.org/3/library/unittest.html
* For beginner, it's right sample python project  
    * virtualenv
    * datatype like dict, orderdict, string
    * string formatting, iterators
    * classes, function, unittest 
    * many more things

### Setup

Clone the git repo & follow the setup instructions

#### With virtalenv

1. `virtualenv env`
2. `source env/bin/activate`
3. `python game.py start`
4. `python game.py start --help`

#### With setuptools as Python Package
1. `virtualenv env`
2. `source env/bin/activate`
3. `pip install --editable .`
4. `gameofdice start`
5. `gameofdice start --help`


### To run the testcases

`python -m unittest -v tests/*.py`



-------------------------------------------------

##### Basic workflow of game (it has been changed little bit during the development) -_-

> python game.py start

> Welcome to the Game Arena!

> Enter the number of players:
2

> Enter name for player 1
Ram 

> Enter name for player 2
Shiva

```

    Game will commence on any key press
    - Each player need to score max. 36 points
    - If a player rolls the value "6" then they immediately get another chance to roll again and
    move ahead in the game.
    - If a player rolls the value "1" two consecutive times then they are forced to skip their next
    turn as a penalty.
    - Hit any key to roll the dice!

    Press any key to start the game!

```

Round 1
>Ram's turn to roll the dice, press enter key
2
>Shiv's turn to roll the dice, press enter key
2

Round 2
>Ram's turn to roll the dice, press enter key
6
>Ram's turn to roll the dice, press enter key
2
>Shiv's turn to roll the dice, press enter key
5

Round 3
>Ram's turn to roll the dice, press enter key
1
>Shiv's turn to roll the dice, press enter key
5

Round 4
>Ram's turn to roll the dice, press enter key
1
>Shiv's turn to roll the dice, press enter key
5

Round 5
>Shiv's turn to roll the dice, press enter key
5

Ram 12
Shiv 22

Round 6
>Ram's turn to roll the dice, press enter key
5

Round 7
>Ram's turn to roll the dice, press enter key
1

Round 8
>Ram's turn to roll the dice, press enter key
1

Round 9
>Ram's turn to roll the dice, press enter key
1
Ram 20
Shiv 22
