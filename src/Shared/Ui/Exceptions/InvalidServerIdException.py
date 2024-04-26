class InvalidServerIdException(Exception):
    def __init__(self, server_id: str):
        super().__init__()
        self.server_id = server_id
