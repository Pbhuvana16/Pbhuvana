
# Exercise 3 :  single server and multiple clients chat program using Python

import socket
import threading
import json

with open('config.json') as config_file:
  config = json.load(config_file)
  host = config['server_address']
  port = config['port']


def customer2(client_socket):
    while True:
        try:
            #if client_socket != message:
                message = client_socket.recv(1024).decode('utf-8')
                print(message)    # show in terminal
        except:
            print("Disconnected from server.")
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # instantiate
client.connect((host, port))    # connect to the server

print(f"Connected to server at {host}:{port}")

receive_thread = threading.Thread(target=customer2, args=(client,))
receive_thread.start()

while True:
    message = input("customer2:")    # again take input
    client.send(message.encode('utf-8'))
client.close()    # close the connection


if __name__ == "__main__":
    customer2()
