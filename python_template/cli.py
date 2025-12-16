from typing import Optional


def hello(name: Optional[str] = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


def main() -> None:
    print(hello())


if __name__ == "__main__":
    main()
