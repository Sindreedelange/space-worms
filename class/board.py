import json


class Board(object):

    def __init__(self, initialize=True):
        self.base_url = "https://visningsrom.stacc.com/dd_server_worms/rest/boards/2"
        if initialize:
            self.initialize-board()

    def initialize_board(self):
        response = request.get(self.base_url)
        data = response.json
        print("Response status code", data.status_code)
        print("Data: \n", data.content)

    def function(self, param):
        """ Quick description

        In-depth description

        Args:
            Explain the arguments
        
        Returns:
            Return type 
        """