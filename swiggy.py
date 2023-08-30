
# Exercise 3 :  single server and multiple clients chat program using Python

import socket
import threading
import json

with open('config.json') as config_file:
  config = json.load(config_file)
  host = config['swiggy_address']
  port = config['port']

def handle_client(client_socket,client_address):
    while True:
        try:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # if data is not received break
                break
            print(f"Received from {client_address}: {message}")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break
    clients.remove(client_socket)
    client_socket.close()   # close the connection



def broadcast(message):
    for client in clients:
            try:
                client.send(message.encode('utf-8'))   # send data to the client

            except:
                continue

def swiggy():
    while True:
        message = input("Server: ")
        formatted_message = f"Server: {message}"
        broadcast(formatted_message)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# look closely. The bind() function takes tuple as argument
server.bind((host, port))  # bind host address and port together
# configure how many client the server can listen simultaneously
server.listen(5)

clients = []

print(f"Server listening on {host}:{port}")

send_thread = threading.Thread(target=swiggy)
send_thread.start()

while True:
    client_socket, client_address = server.accept()      # accept new connection
    print(f"Accepted connection from {client_address}")
    clients.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket,client_address))
    client_thread.start()

if __name__ == "__main__":
    swiggy()


