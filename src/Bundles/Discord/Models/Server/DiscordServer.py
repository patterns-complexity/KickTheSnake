from src.types import List, NewType


class DiscordServer:
    def __init__(self, server_id: int):
        self.id = server_id


DiscordServers = NewType("DiscordServers", List[DiscordServer])
