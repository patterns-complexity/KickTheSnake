from src.types import List, NewType


class DiscordUser:
    def __init__(self, user_id: int, username: str, global_name: str, avatar_url: str) -> None:
        self.id = user_id
        self.username = username
        self.global_name = global_name
        self.avatar_url = avatar_url

    def __str__(self) -> str:
        return f"User: {self.username} ({self.global_name}) | Avatar: {self.avatar_url} | ID: {self.id}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DiscordUser):
            return NotImplemented
        return self.id == other.id


DiscordUsers = NewType("DiscordUsers", List[DiscordUser])
