from src.types import List, NewType


class DiscordServer:
    def __init__(self, server_id: int, server_name: str):
        self.id = server_id
        self.name = server_name


DiscordServers = NewType("DiscordServers", List[DiscordServer])
