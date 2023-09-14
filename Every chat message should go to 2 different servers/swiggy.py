import socket
import threading
import json
import os

 
# swiggy Configuration
def load_config():
    with open("config.json") as config_file: 
	    config = json.load(config_file) 
	    host = config['swiggy_address'] 
	    port = config['port1'] 
	    return host, port
	    
# Function to handle receiving messages from the client
def receive_messages(client_socket):
    while True:
        try:
            client_message = client_socket.recv(1024).decode()
            if client_message=="exit":
                os.exit(0)
            print(client_message)
        except Exception as e:
            print(f"Error: {e}")
            break

def swiggy(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"swiggy listening on {host}:{port}")


    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")


    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()



    while True:
        try:
            server_message = input("swiggy:")
            client_socket.send(f"swiggy: {server_message}".encode())
            if server_message.lower() == "exit":
                os._exit(0)
        except Exception as e:
            print(f"Error: {e}")
            os._exit(0)


    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    host, port = load_config()
    swiggy(host, port)
