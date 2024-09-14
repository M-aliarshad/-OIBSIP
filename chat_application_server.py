import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received: {message}")
            broadcast(message, client_socket)
        except:
            break
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode('utf-8'))

def server_input():
    while True:
        server_message = input("Server: ")
        broadcast(f"Server: {server_message}", None)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)
print("Server started. Waiting for connections...")

clients = []

threading.Thread(target=server_input, daemon=True).start()

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr} has been established.")
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()