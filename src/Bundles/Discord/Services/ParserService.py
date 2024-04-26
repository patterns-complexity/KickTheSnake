from src.types import List

from src.Bundles.Discord.Models.Server.DiscordServer import DiscordServer, DiscordServers
from src.Shared.Ui.Sanitizers.CliArgsSanitizer import sanitize_whitespace


def is_unique(server: str, server_list: List[str]) -> bool:
    return server not in server_list


def parse_server_string(server_string: str) -> DiscordServer:
    server_params = server_string.split(":")
    server_id, server_name = sanitize_whitespace(server_params)
    return DiscordServer(server_id=int(server_id), server_name=server_name)


def parse_server_list_string(server_list_string: str) -> DiscordServers:
    split_server_list = server_list_string.split(",")
    sanitized_server_list = sanitize_whitespace(split_server_list)

    server_list: DiscordServers = DiscordServers([])
    for server in sanitized_server_list:
        server_list.append(parse_server_string(server))

    return server_list
