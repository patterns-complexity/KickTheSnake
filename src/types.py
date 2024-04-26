from typing import NewType, TypedDict, List

from src.Discord.User.DiscordUser import DiscordUser
from src.Discord.Server.DiscordServer import DiscordServer

DiscordServerId = NewType("DiscordServerId", int)

DiscordUserId = NewType("DiscordUserId", int)


DiscordServers = NewType("DiscordServers", List[DiscordServer])
DiscordUsers = NewType("DiscordUsers", List[DiscordUser])
