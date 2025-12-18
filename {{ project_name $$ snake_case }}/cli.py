import argparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def hello(name: str) -> str:
    """Greet the user.

    Parameters
    ----------
    name : str
        the user's name

    Returns
    -------
    str
        a string greeting the user.
    """
    return f"Hello from {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet the user.")
    parser.add_argument(
        "--name", type=str, help="Name of the person to greet", required=True
    )
    args = parser.parse_args()
    logger.info(hello(args.name))
