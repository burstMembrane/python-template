def hello(name: str | None = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


def main() -> None:
    print(hello())


if __name__ == "__main__":
    main()
