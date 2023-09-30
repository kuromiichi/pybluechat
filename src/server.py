import bluetooth
import os

from chat import Chat


def main():
    os.system("cls" if os.name == "nt" else "clear")
    # Create a Bluetooth socket using RFCOMM protocol
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # Bind the socket to the local adapter address using any port available and listen for incoming connections
    socket.bind(("", bluetooth.PORT_ANY))
    socket.listen(1)

    # Accept the first connection
    address, port = socket.getsockname()
    print("Waiting for connection on address", address, "and port", port)
    client_socket, client_info = socket.accept()

    print("Connected to client at address", client_info[0])
    print("Press enter to join the chat")

    # Create chat with remote device
    chat = Chat(address, client_socket)
    try:
        chat.run()
    except OSError:
        print("Connection ended")

    # Close the sockets
    print("Exiting the application")
    client_socket.close()
    socket.close()
