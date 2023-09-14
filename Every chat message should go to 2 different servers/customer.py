import socket
import threading
import json

server_sockets = []

# Function to handle receiving messages from the server
def receive_messages(server_socket):
    while True:
        try:
            server_message = server_socket.recv(1024).decode()
            if not server_message:
                break
            print(server_message)
        except Exception as e:
            print(f"Error: {e}")
            break

# Function to send a message to multiple server sockets
def broadcast_message(message, sockets):
    for sock in sockets:
        try:
            sock.send(message.encode())
        except Exception as e:
            print(f"Error sending message: {str(e)}")

def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        host1 = config['swiggy_address']
        port1 = config['port1']
        host2 = config['zomato_address']
        port2 = config['port2']
    return host1, port1, host2, port2

# main function
def customer():
    host1, port1, host2, port2 = load_config()

    # swiggy Connection
    client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket1.connect((host1, port1))
    print("Connected to Swiggy")
    server_sockets.append(client_socket1)

    # zomato Connection
    client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket2.connect((host2, port2))
    print("Connected to Zomato")
    server_sockets.append(client_socket2)

    # Start threads to receive messages from server1 and server2
    server1_thread = threading.Thread(target=receive_messages, args=(client_socket1,))
    server2_thread = threading.Thread(target=receive_messages, args=(client_socket2,))
    server1_thread.start()
    server2_thread.start()

    try:
        while True:
            message = input("customer: ")
            broadcast_message(f"client: {message}", server_sockets)
            if message.lower() == "exit":
                break

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    customer()

