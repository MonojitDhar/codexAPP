"""Minimal runnable entrypoint for the application."""


def get_message() -> str:
    """Return the default startup message."""
    return "Hello from codexAPP"


def main() -> None:
    """Run the application entrypoint."""
    print(get_message())


if __name__ == "__main__":
    main()
