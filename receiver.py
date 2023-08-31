
# Exercise 2 : Client/Server chat program using Python

import socket
import json

with open('config.json') as config_file:
    config = json.load(config_file)
    hostname = config['server_address']
    port = config['port']


def reciever():

    client_socket = socket.socket()  # instantiate
    client_socket.connect((hostname, port))  # connect to the server

    message = input(" To server: ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" To server: ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    reciever()
