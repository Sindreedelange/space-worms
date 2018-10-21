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

## TODO
- Use TDD
- Find some way to serialize JSON objects to *.py* classes <br>
--> Make my own `serialize_objects` class
- Board/Square factory
- Refactor `Board.py` so that it contains no logic
- Implement (model) classes `Player` and `Dice`
- Define a *CHANGELOG.md* instead of this **TODO** list 
