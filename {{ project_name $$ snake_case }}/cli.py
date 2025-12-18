import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def hello(name: str) -> str:
    """
    Hello function.

    :param name: the name of the person to greet
    :type name: str
    :return: a greeting message
    :rtype: str
    """
    return f"Hello from {name}!"


def main() -> None:
    """
    Main function to parse arguments and print greeting.
    """
    parser = argparse.ArgumentParser(description="Greet the user.")
    parser.add_argument(
        "--name", type=str, help="Name of the person to greet", required=True
    )
    args = parser.parse_args()
    logger.info(hello(args.name))
