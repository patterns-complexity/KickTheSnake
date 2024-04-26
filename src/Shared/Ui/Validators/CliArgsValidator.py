from src.types import List

from src.Shared.Ui.Sanitizers.CliArgsSanitizer import sanitize_whitespace
from src.Shared.Ui.Exceptions.ServerIdIsNanException import ServerIdIsNanException
from src.Shared.Ui.Exceptions.InvalidServerIdException import InvalidServerIdException
from src.Shared.Ui.Exceptions.DuplicateServerIdException import DuplicateServerIdException
from src.Shared.Ui.Exceptions.NoServersProvidedException import NoServersProvidedException


def validate_server_id(server_id: str, validated_servers: List[str]) -> None:
    if server_id in validated_servers:
        raise DuplicateServerIdException(server_id)

    if not server_id.isdigit():
        raise ServerIdIsNanException(server_id)

    if len(server_id) < 15:
        raise InvalidServerIdException(server_id)

    validated_servers.append(server_id)


def validate_server_id_list(server_id_list: List[str]) -> None:
    if len(server_id_list) == 0:
        raise NoServersProvidedException

    validated_servers: List[str] = []
    for sanitzed_server in server_id_list:
        validate_server_id(sanitzed_server, validated_servers)
