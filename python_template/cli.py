import argparse


def hello(name: str | None = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet the user.")
    parser.add_argument("--name", type=str, help="Name of the person to greet", required=True)
    args = parser.parse_args()

    if not args.name:
        raise ValueError("Name argument is required.")

    print(hello(args.name))


if __name__ == "__main__":
    main()
