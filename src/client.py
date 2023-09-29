import bluetooth
import os


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
    socket.connect((address, port))

    # funky wunky stuff goes here

    socket.close()


def get_last_address():
    with open("../data/last_address.txt", "r") as f:
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
    with open("../data/last_address.txt", "w") as f:
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
