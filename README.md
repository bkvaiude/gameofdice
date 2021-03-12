# Welcome game of dice!

### If you are looking for ludo game, then you reach to right place!

### What can you learn from this game

* https://click.palletsprojects.com/en/7.x/quickstart/#
* How to create python package (click + setuptools) https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration
* Basic understanding of the setuptools
* unittest https://docs.python.org/3/library/unittest.html
* For beginner, it's right sample python project  

To run the testcases

`python -m unittest -v tests/*.py`

Basic workflow of game (it has been changed little bit during the development) -_-

>> python game.py start
>> Welcome to the Game Arena!
>> Enter the number of players:
2
>> Enter name for player 1
Ram 
>> Enter name for player 2
Shiva

```

Game will commence on the enter key press
- Each player need to score max. 20 points
- If a player rolls the value "6" then they immediately get another chance to roll again and
move ahead in the game.
- If a player rolls the value "1" two consecutive times then they are forced to skip their next
turn as a penalty.
- User get 5 secs to roll the dice, after it is auto rolled by computer behalf of user

```

Round 1
>>Ram's turn to roll the dice, press enter key
2
>>Shiv's turn to roll the dice, press enter key
2

Round 2
>>Ram's turn to roll the dice, press enter key
6
>>Ram's turn to roll the dice, press enter key
2
>>Shiv's turn to roll the dice, press enter key
5

Round 3
>>Ram's turn to roll the dice, press enter key
1
>>Shiv's turn to roll the dice, press enter key
5

Round 4
>>Ram's turn to roll the dice, press enter key
1
>>Shiv's turn to roll the dice, press enter key
5

Round 5
>>Shiv's turn to roll the dice, press enter key
5

Ram 12
Shiv 22

Round 6
>>Ram's turn to roll the dice, press enter key
5

Round 7
>>Ram's turn to roll the dice, press enter key
1

Round 8
>>Ram's turn to roll the dice, press enter key
1

Round 9
>>Ram's turn to roll the dice, press enter key
1
Ram 20
Shiv 22
