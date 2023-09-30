import sys

import bluetooth
import os

from chat import Chat

last_address_file = "../data/last_address.txt"


def main():
    os.system("cls" if os.name == "nt" else "clear")

    # Get address and port from file or user input
    address = get_last_address()

    if not address:
        print("No previous connection data found")
    elif not bluetooth.is_valid_address(address):
        print("Previous connection data is invalid")
    else:
        print(f"Found previous connection address: {address}")

    new_address = get_new_address()
    if new_address:
        address = new_address
        save_new_address(address)

    port = get_port()

    # Create socket and connect to server
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    try:
        socket.connect((address, port))
    except OSError:
        print("Failed to connect to server, exiting application")
        socket.close()
        sys.exit(1)

    print("Connected to server at address", address)
    print("Press enter to join the chat")

    # Create chat with remote device
    chat = Chat(address, socket)
    try:
        chat.run()
    except OSError:
        print("Connection ended")

    # Close the socket
    print("Exiting the application")
    socket.close()


def get_last_address():
    if not os.path.exists(last_address_file):
        return
    with open(last_address_file, "r") as f:
        return f.read().strip()


def get_new_address():
    while True:
        address = input("Enter new address (leave blank for last address): ")
        if not address:
            return
        if bluetooth.is_valid_address(address):
            return address
        print("Invalid address")


def save_new_address(address):
    with open(last_address_file, "w") as f:
        f.write(address)


def get_port():
    while True:
        port = input("Enter port: ")
        try:
            port = int(port)
        except ValueError:
            pass
        if port in range(1, 31):
            return port
        print("Port must be an integer between 1 and 30")
