
import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

clients = {}
lock = threading.Lock()


# Send a message to all connected users
def broadcast(message):
    with lock:
        connected_clients = list(clients.keys())

    for client in connected_clients:
        try:
            client.sendall(message.encode("utf-8"))
        except OSError:
            remove_client(client)


# Remove disconnected clients
def remove_client(client):
    with lock:
        username = clients.pop(client, None)

    try:
        client.close()
    except OSError:
        pass

    if username:
        print(f"{username} disconnected.", flush=True)
        broadcast(f"\n{username} left the chat!\n")


# Handle each client
def handle_client(client, address):
    reader = None
    username = None

    try:
        reader = client.makefile("r", encoding="utf-8")

        username = reader.readline().strip()

        if not username:
            return

        with lock:
            clients[client] = username

        print(f"{username} joined from {address}", flush=True)
        broadcast(f"\n{username} joined the chat!\n")

        for message in reader:
            message = message.strip()

            if message.lower() == "/quit":
                break

            if message:
                print(f"{username}: {message}", flush=True)
                broadcast(f"{username}: {message}\n")

    except (ConnectionError, OSError):
        pass

    finally:
        if reader:
            reader.close()

        remove_client(client)


# Start server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen()

        print("=" * 40)
        print("       PYTHON CHAT SERVER")
        print("=" * 40)
        print(f"Server running on {HOST}:{PORT}")
        print("Waiting for clients...")
        print("Press Control + C to stop.")
        print("=" * 40, flush=True)

        while True:
            client, address = server.accept()

            thread = threading.Thread(
                target=handle_client,
                args=(client, address),
                daemon=True
            )
            thread.start()

    except OSError as error:
        print(f"Server error: {error}", flush=True)

    except KeyboardInterrupt:
        print("\nServer shutting down...", flush=True)

    finally:
        server.close()

        with lock:
            connected_clients = list(clients.keys())

        for client in connected_clients:
            try:
                client.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
            client.close()

        with lock:
            clients.clear()

        print("Server stopped.", flush=True)


if __name__ == "__main__":
    start_server()
