from src.Bundles.Discord.Exceptions.InvalidDiscordUserDtoException import (
    InvalidDiscordUserDtoException,
)

required_user_keys = ["id", "username", "global_name", "avatarURL"]


def validate_discord_user_dto(user_dict: dict[str, str]) -> None:
    for key in required_user_keys:
        if key not in user_dict:
            raise InvalidDiscordUserDtoException
