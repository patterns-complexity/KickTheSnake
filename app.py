import src.constants as constants

from src.types import List

from time import sleep
from requests import Response

from src.Bundles.Discord.Models.Server.DiscordServer import DiscordServers
from src.Bundles.Discord.Models.User.DiscordUser import DiscordUser
from src.Bundles.Discord.Services.ParserService import parse_server_id_list
from src.Bundles.Discord.Validators.DiscordUserValidator import validate_discord_user_dto

from src.Bundles.Discord.Exceptions.InvalidDiscordUserDtoException import (
    InvalidDiscordUserDtoException,
)

from src.Shared.Ui.Cli import parse_args, validate_args, print_help
from src.Shared.Ui.Validators.CliArgsValidator import validate_server_id_list
from src.Shared.Services.BotUsersDataService import request_bot_list

from src.Shared.Ui.Exceptions.DuplicateServerIdException import DuplicateServerIdException
from src.Shared.Ui.Exceptions.ServerIdIsNanException import ServerIdIsNanException
from src.Shared.Ui.Exceptions.InvalidServerIdException import InvalidServerIdException
from src.Shared.Ui.Exceptions.NoServersProvidedException import NoServersProvidedException


def print_args_error_and_exit(message: str) -> None:
    print_help()
    print(message)
    exit(1)


if __name__ == "__main__":
    try:
        args = parse_args()
        validate_args(args)
        server_id_list: List[str] = args[constants.ARG_NAME]
        validate_server_id_list(server_id_list)
    except DuplicateServerIdException as e:
        print_args_error_and_exit(f"Duplicate server ID {e.server_id}!")
    except ServerIdIsNanException as e:
        print_args_error_and_exit(f"Server ID {e.server_id} is not a number!")
    except InvalidServerIdException as e:
        print_args_error_and_exit(f"Server ID {e.server_id} is invalid!")
    except NoServersProvidedException as e:
        print_args_error_and_exit("No server IDs provided!")
    except Exception as e:
        print_args_error_and_exit(f"Error validating arguments: {e}")

    servers: DiscordServers = parse_server_id_list(server_id_list)

    for server in servers:
        try:
            response: Response = request_bot_list(server)
            response_dict: dict[str, str] = dict(response.json())
        except Exception as e:
            print(f"Error requesting server {server.id}:")
            print(e)
            continue

        try:
            validate_discord_user_dto(response_dict)
        except InvalidDiscordUserDtoException as e:
            print(f"Invalid response from server {server.id}:")
            print(e)
            continue
        except Exception as e:
            print(f"Error validating response from server {server.id}:")
            print(e)
            continue

        found_user = DiscordUser(
            user_id=int(response_dict["id"]),
            username=response_dict["username"],
            global_name=response_dict["global_name"],
            avatar_url=response_dict["avatarURL"],
        )

        print(f"Found user in server {server.id}:")
        print(f"Server: {server.id} | ", found_user)

        if constants.REQUEST_COOLDOWN and int(constants.REQUEST_COOLDOWN) > 0:
            sleep(int(constants.REQUEST_COOLDOWN))
