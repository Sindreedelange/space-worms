class Square(object):

    def __init__(self, response):
        self.number = 0
        self.pos_x = 0
        self.pos_y = 0
        self.name = ""
        self.links = {}
        self.wormhole = 0
        self.wormhole_url = ""
        self.serialize_json_square(response)

    def has_next(self):
        cont = False
        for links in self.links:
            if 'next' in links.values():
                cont = True
            else:
                cont = False
        return cont

    def serialize_json_square(self, response):
        print("Response: \n", response)
        self.number = response['number']
        self.pos_x = response['posX']
        self.pos_y = response['posY']
        self.name = response['name']
        self.links = response['links']
        if 'wormhole' in response:
            self.wormhole = response['wormhole']
        if 'wormhole_url' in response:
            self.wormhole_url = response['wormhole_url']
        return self
