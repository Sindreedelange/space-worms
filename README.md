# README
Implementing the game *Space Worms* - a version of *Snakes and Ladders*, using Python > 2.7.x

# Run
To run the program either clone the repo: <br>
`git clone https://github.com/Sindreedelange/space-worms.git`
<br>
or download as .zip. 

The program can be run from `src/SpaceWorms.py` <br>

## Install dependencies
To make API request:
Dependent on your package manager <br>
`conda install requests` / `pip install requests` <br>

## TODO
- Use TDD
- Find some way to serialize JSON objects to *.py* classes <br>
--> Make my own `serialize_objects` class
- Board/Square factory
- Refactor `Board.py` so that it contains no logic
- Implement (model) classes `Player` and `Dice`