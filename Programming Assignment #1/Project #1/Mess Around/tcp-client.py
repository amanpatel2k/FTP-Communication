import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# Send Continous Message

user = input('Enter a message to server: ')

while user != 'quit': 
    # Send data
    client.send(user.encode())
    # receive data
    response = client.recv(4096)
    
    print(response)
    
    user = input('Enter a message to server: ')

client.close()
    
