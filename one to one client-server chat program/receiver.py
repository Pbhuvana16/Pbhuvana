import socket
import json

# Function to load server configuration from config.json
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        hostname = config['server_address']
        port = config['port']
    return hostname, port

# Main function for the receiver program
def receiver():
    # calling Load server configuration
    hostname, port = load_config()

    # Create a socket server
    client_socket = socket.socket()
    client_socket.connect((hostname, port))

    while True:
        # Take user input to send to the server
        message = input("To server: ")
        client_socket.send(message.encode())
        
        # Check if the user wants to exit
        if message.lower().strip() == 'bye':
            break

        # Receive and display the server's response
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)

    # Close the client socket when the loop exits
    client_socket.close()

if __name__ == '__main__':
 # calling receiver function
    receiver()
