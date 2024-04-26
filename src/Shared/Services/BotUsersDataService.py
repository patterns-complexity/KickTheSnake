import src.constants as constants

from requests import Response, get
from src.Bundles.Discord.Models.Server.DiscordServer import DiscordServer


def request_bot_list(discord_server: DiscordServer) -> Response:
    if not constants.API_URL:
        raise ValueError("API URL is not set")

    return get(constants.API_URL.format(discord_server_id=discord_server.id))
