import os
import threading


class Chat:
    def __init__(self, local_address, remote_socket):
        self.local_address = local_address
        self.remote_address = remote_socket.getsockname()[0]
        self.remote_socket = remote_socket
        self.messages = []
        self.stop = threading.Event()

    def run(self):
        listen_thread = threading.Thread(target=self.listen_for_messages)
        send_thread = threading.Thread(target=self.send_message)

        send_thread.start()
        listen_thread.start()

        send_thread.join()

    def listen_for_messages(self):
        try:
            while True:
                if self.stop.is_set():
                    break
                message = self.remote_socket.recv(1024).decode('utf-8')
                if message == "exit()":
                    print("Exiting chat (remote disconnected, press enter to exit)")
                    self.stop.set()
                    break
                message = f"({self.remote_address})> {message}"
                self.messages.append(message)
                self.update_chat()
        except OSError:
            print("Connection ended")

    def send_message(self):
        try:
            while True:
                if self.stop.is_set():
                    break
                message = input()
                if message == "exit()":
                    print("Exiting chat")
                    self.remote_socket.send(message)
                    self.stop.set()
                    break
                if message:
                    self.messages.append(f"You ({self.local_address})> {message}")
                self.remote_socket.send(message)
                self.update_chat()
        except OSError:
            print("Connection ended")

    def update_chat(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join(self.messages))
        print("> ", end="", flush=True)
