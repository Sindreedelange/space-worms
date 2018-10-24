class Board:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.dimX = int(data['dimX'])
        self.dimY = int(data['dimY'])
        self.start_square_number = int(data['start'])
        self.goal_square = int(data['goal'])
        self.api_ref = data['self']
        self.start_square_api_ref = data['startSquare']
        self.squares = []
        self.size = int(self.dimX * self.dimY)









