

class SquareController:

    @staticmethod
    def has_next(square):
        cont = False
        for links in square.links:
            if 'next' in links.values():
                cont = True
            else:
                cont = False
        return cont
