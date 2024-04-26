import src.constants as constants

from argparse import ArgumentParser

from src.Shared.Ui.Exceptions.NoServersProvidedException import NoServersProvidedException

from src.types import List


parser = ArgumentParser()

parser.add_argument(
    type=str, nargs="+", metavar=constants.METAVAR, help=constants.HELP, dest=constants.ARG_NAME
)


def print_help() -> None:
    parser.print_help()


def validate_args(args: dict[str, List[str]]) -> None:
    if not args[constants.ARG_NAME]:
        raise NoServersProvidedException


def parse_args() -> dict[str, List[str]]:
    return vars(parser.parse_args())
