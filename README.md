# Space Worms
Implementing the game *Space Worms* - a version of *Snakes and Ladders*, using Python 3

# Building

## Prerequisites
1. Python 3
2. Packet manager, such as **Conda** or **Pip**

## Instructions
1. Clone the repository <br>
`git clone https://github.com/Sindreedelange/space-worms.git`, or download as .zip. 
2. In order to make API requests, install *requests*
  <br> Dependent on your package manager <br>
  `conda install requests` / `pip install requests` <br>
2. Open in editor, such as *PyCharm*
3. Navigate to `src/SpaceWorms.py`
4. Run the file

## Game rules
If a player rolls the dice so that they would end up outside of the board, they start 
from the end of the board, with remaining eyes on the dice left to move. 

## Known problems
There have been a few problems with regards to importing modules. It should
now work in terminal, but if using *PyCharm* add */src* to project interpreter
path (https://stackoverflow.com/questions/48947494/add-directory-to-python-path-in-pycharm) 

## TODO
- Refactor logic in Square
    - SquareResponse w. to_square_model. Possibly relevant for Board as well
- Throw exception instead of returning 'None' if not able to find Board
- Define a *CHANGELOG.md* instead of this **TODO** list 
