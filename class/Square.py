class Square(object):

    def __init__(self, number, pos_x, pos_y, name, links, wormhole=0, wormhole_url=""):
        self.number = number
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.name = name
        self.links = links
        self.wormhole = wormhole
        self.wormhole_url = wormhole_url

    def has_next(self):
        cont = False
        for links in self.links:
            if 'next' in links.values():
                cont = True
            else:
                cont = False
        return cont
