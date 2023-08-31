# Exercise 2 : Client/Server chat program using Python

import socket
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    host = config['server_address']
    port = config['port']

def sender():

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen()
    client_socket,client_address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(client_address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = client_socket.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("Received from client: " + str(data))
        data = input(' To client: ')
        client_socket.send(data.encode())  # send data to the client

    client_socket.close()  # close the connection


if __name__ == '__main__':
    sender()
