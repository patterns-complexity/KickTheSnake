from src.types import List

from src.Shared.Ui.Sanitizers.CliArgsSanitizer import sanitize_whitespace


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


def validate_server_list_string(server_list_string: str) -> None:
    split_server_list = server_list_string.split(",")

    if len(split_server_list) == 0:
        raise ValueError("No servers provided!")

    sanitized_server_list = sanitize_whitespace(split_server_list)

    validated_servers: List[str] = []
    for sanitzed_server in sanitized_server_list:
        validate_server_string(sanitzed_server, validated_servers)
