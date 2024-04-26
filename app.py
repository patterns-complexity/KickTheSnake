import src.constants as constants

from time import sleep
from requests import get, Response

from src.Shared.Ui.Cli import parse_args, validate_args
from src.Shared.Ui.Validators.CliArgsValidator import validate_server_list_string
from src.Bundles.Discord.Models.Server.DiscordServer import DiscordServer, DiscordServers
from src.Bundles.Discord.Models.User.DiscordUser import DiscordUser, DiscordUsers
from src.Bundles.Discord.Services.ParserService import parse_server_list_string


def request_bot_list(discord_server: DiscordServer) -> Response:
    return get(f"https://kickthespy.pet/getBot?id={discord_server.id}")


if __name__ == "__main__":
    args = parse_args()
    validate_args(args, [constants.ARG_NAME])
    server_list_string: str = args[constants.ARG_NAME]
    validate_server_list_string(server_list_string)
    servers: DiscordServers = DiscordServers(parse_server_list_string(server_list_string))

    found_users: DiscordUsers = DiscordUsers([])

    for server in servers:
        try:
            response = request_bot_list(server)
        except Exception as e:
            print(f"Failed to request bot list for server {server.name}")
            print(e)
            continue

        response_dict = dict(response.json())

        found_users.append(
            DiscordUser(
                user_id=int(response_dict["id"]),
                username=response_dict["username"],
                global_name=response_dict["global_name"],
                avatar_url=response_dict["avatarURL"],
            )
        )
        sleep(int(constants.REQUEST_COOLDOWN))

    for user in found_users:
        print(user)
