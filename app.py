import src.constants as constants

from time import sleep

from requests import get, Response
from argparse import ArgumentParser

from src.types import (
    DiscordServerId,
    DiscordServer,
    DiscordServers,
    DiscordUserId,
    DiscordUser,
    DiscordUsers,
    List,
)

parser = ArgumentParser()
parser.add_argument(
    f"-{constants.ARG_NAME_SHORT}",
    f"--{constants.ARG_NAME}",
    type=str,
    required=True,
    metavar=constants.METAVAR,
    help=constants.HELP,
)


def sanitize_whitespace(strings: List[str]) -> List[str]:
    sanitized_servers: List[str] = []
    for server in strings:
        sanitized_servers.append(server.strip())
    return strings


def parse_args() -> dict[str, str]:
    args_dict: dict[str, str] = vars(parser.parse_args())
    return args_dict


def validate_args(args: dict[str, str], required: List[str]) -> None:
    for arg in required:
        if not args[arg]:
            parser.print_help()
            raise ValueError(f"Argument {arg} is required")


def validate_server_id_string(server_id: str) -> None:
    if not server_id.isdigit():
        raise ValueError(f"Server ID is invalid: {server_id}. It must be a number.")

    if len(server_id) < 17:
        raise ValueError(
            f"Invalid server ID: {server_id}. Server IDs must be at least 17 characters long."
        )


def validate_server_string(servers: str, validated_servers: List[str]) -> None:
    if ":" not in servers:
        raise ValueError(f"Invalid server: ({servers}). Servers must be in the format ID:NAME")

    params = servers.split(":")

    if len(params) != 2:
        raise ValueError(
            f"Something is missing from this server: {servers}. Servers must be in the format ID:NAME"
        )

    sanitized_params = sanitize_whitespace(params)

    server_id, _ = sanitized_params

    if server_id in validated_servers:
        raise ValueError(f"Duplicate server ID: {server_id}")

    validated_servers.append(server_id)

    validate_server_id_string(server_id)


def is_unique(server: str, server_list: List[str]) -> bool:
    return server not in server_list


def validate_server_list_string(server_list_string: str) -> None:
    split_server_list = server_list_string.split(",")

    if len(split_server_list) == 0:
        parser.print_help()
        raise ValueError("No servers provided!")

    sanitized_server_list = sanitize_whitespace(split_server_list)

    validated_servers: List[str] = []
    for sanitzed_server in sanitized_server_list:
        validate_server_string(sanitzed_server, validated_servers)


def parse_server_string(server_string: str) -> DiscordServer:
    server_params = server_string.split(":")
    server_id, server_name = sanitize_whitespace(server_params)
    discord_server_id = DiscordServerId(int(server_id))
    return DiscordServer(server_id=discord_server_id, server_name=server_name)


def parse_server_list_string(server_list_string: str) -> List[DiscordServer]:
    split_server_list = server_list_string.split(",")
    sanitized_server_list = sanitize_whitespace(split_server_list)

    server_list: List[DiscordServer] = []
    for server in sanitized_server_list:
        server_list.append(parse_server_string(server))

    return server_list


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
        response = request_bot_list(server)
        response_dict = dict(response.json())
        found_users.append(
            DiscordUser(
                user_id=DiscordUserId(response_dict["id"]),
                username=response_dict["username"],
                global_name=response_dict["global_name"],
                avatar_url=response_dict["avatarURL"],
            )
        )
        sleep(int(constants.REQUEST_COOLDOWN))

    for user in found_users:
        print(user)
