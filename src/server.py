import os

import bluetooth


def main():
    os.system("cls" if os.name == 'nt' else "clear")
    # Create a Bluetooth socket using RFCOMM protocol
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # Bind the socket to the local adapter address using any port available and listen for incoming connections
    socket.bind(("", bluetooth.PORT_ANY))
    socket.listen(1)

    # Accept the first connection
    address, port = socket.getsockname()
    print("Waiting for connection on address", address, "and port", port)
    client_socket, client_info = socket.accept()
    print("Connected with", client_info)

    # funky wunky stuff goes here

    client_socket.close()
    socket.close()
