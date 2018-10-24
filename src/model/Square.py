class Square:

    def __init__(self, data):
        self.number = data['number']
        self.pos_x = data['posX']
        self.pos_y = data['posY']
        self.name = data['name']
        self.links = data['links']
        if 'wormhole' in data:
            self.wormhole = data['wormhole']
        if 'wormhole_url' in data:
            self.wormhole_url = data['wormhole_url']
