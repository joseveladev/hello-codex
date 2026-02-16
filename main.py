import sys


def main() -> None:
    message = sys.argv[1] if len(sys.argv) > 1 else "Hello, I'm Codex"
    print(message)


if __name__ == "__main__":
    main()
