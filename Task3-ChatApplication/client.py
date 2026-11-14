
import socket
import threading

HOST = "127.0.0.1"
PORT = 5555


# Receive messages from server
def receive_messages(client):
    try:
        while True:
            message = client.recv(4096)

            if not message:
                print("\nServer disconnected.")
                break

            print(message.decode("utf-8"), end="", flush=True)

    except (ConnectionError, OSError):
        print("\nConnection closed.")

    finally:
        print("\nYou are disconnected from the chat.")


# Start client
def start_client():

    username = input("Enter your username: ").strip()

    if not username or "\n" in username:
        print("Please enter a valid username.")
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))

        client.sendall(
            (username + "\n").encode("utf-8")
        )

        print(f"\nWelcome, {username}!")
        print("You are connected to the chat.")
        print("Type your message and press Enter.")
        print("Type /quit to leave.")
        print("-" * 40, flush=True)

        # Start receiving messages
        receiver = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True
        )

        receiver.start()

        # Send messages
        while True:
            message = input()

            if message.strip().lower() == "/quit":
                client.sendall(b"/quit\n")
                break

            if message.strip():
                client.sendall(
                    (message + "\n").encode("utf-8")
                )

    except ConnectionRefusedError:
        print("Server is not running. Start server.py first.")

    except (ConnectionError, OSError):
        print("Unable to communicate with the server.")

    finally:
        try:
            client.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass

        client.close()
        print("Chat client closed.")


if __name__ == "__main__":
    start_client()
