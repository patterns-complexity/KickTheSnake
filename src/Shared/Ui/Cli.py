from src.types import List

import src.constants as constants

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    f"-{constants.ARG_NAME_SHORT}",
    f"--{constants.ARG_NAME}",
    type=str,
    required=True,
    metavar=constants.METAVAR,
    help=constants.HELP,
)


def validate_args(args: dict[str, str], required: List[str]) -> None:
    for arg in required:
        if not args[arg]:
            parser.print_help()
            raise ValueError(f"Argument {arg} is required")


def parse_args() -> dict[str, str]:
    args_dict: dict[str, str] = vars(parser.parse_args())
    return args_dict
