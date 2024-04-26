from src.types import List

from src.Bundles.Discord.Models.Server.DiscordServer import DiscordServer, DiscordServers
from src.Shared.Ui.Sanitizers.CliArgsSanitizer import sanitize_whitespace


def parse_server_id(server_id: str) -> DiscordServer:
    return DiscordServer(server_id=int(server_id))


def parse_server_id_list(server_id_list: List[str]) -> DiscordServers:
    server_list: DiscordServers = DiscordServers([])
    for server in server_id_list:
        server_list.append(parse_server_id(server))

    return server_list
