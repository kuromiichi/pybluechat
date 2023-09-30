import os
import sys

import client
import server


def main():
    create_data_directory()
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to PyBlueChat!")

    # Mode selection (server/client)
    if len(sys.argv) == 2:
        if sys.argv[1] not in ["server", "client"]:
            print("Invalid mode, use \"server\" or \"client\"")
            mode = select_mode()
        else:
            mode = sys.argv[1]
    else:
        mode = select_mode()

    if mode == "server":
        server.main()
    else:
        client.main()


def select_mode():
    while True:
        print("Please select a mode:")
        print("1. Server")
        print("2. Client")
        mode = input("> ").lower()
        if mode in ["1", "server", "s"]:
            return "server"
        elif mode in ["2", "client", "c"]:
            return "client"
        else:
            print("Invalid option, use 1 or 2")


def create_data_directory():
    if not os.path.exists("../data"):
        os.mkdir("../data")


if __name__ == "__main__":
    main()
