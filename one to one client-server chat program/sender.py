import socket
import json

def load_config():
    # Load server configuration from config.json
    with open('config.json') as config_file:
        config = json.load(config_file)
        host = config['server_address']
        port = config['port']
    return host, port

def sender():
    # calling Load server configuration
    host, port = load_config()

    # Create a socket object and bind it to the specified host and port
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()
    
    # Accept incoming client connection
    client_socket, client_address = server_socket.accept()
    print("Connection from: " + str(client_address))

    while True:
        # Receive data from the client (up to 1024 bytes)
        data = client_socket.recv(1024).decode()
        if not data:
            # If no data received, break the loop
            break
        print("Received from client: " + str(data))
        
        # Send data to the client
        data = input('To client: ')
        client_socket.send(data.encode())

    # Close the client socket when the loop exits
    client_socket.close()

if __name__ == '__main__':
    # calling sender function
    sender()
