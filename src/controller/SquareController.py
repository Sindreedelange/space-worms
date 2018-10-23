import src.model.Square as Square


class SquareController(object):
    def __init__(self):
        pass

    @staticmethod
    def has_next(square):
        cont = False
        for links in square.links:
            if 'next' in links.values():
                cont = True
            else:
                cont = False
        return cont
