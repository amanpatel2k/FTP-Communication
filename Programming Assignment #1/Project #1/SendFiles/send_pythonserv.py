import socket
import sys

def grab_info(client, value): 
    
    # Create an acutal and temp buffer
    recvBuff, tempBuff = b"", b""
    
    while len(recvBuff) < value: 
        # Recieve all the data based on value 
        tempBuff = client.recv(value)
        
        # There no closed socket 
        if not tempBuff:
            break
        
        recvBuff += tempBuff
    
    return recvBuff

def server_accept(client, addr): 
    
    print('Accepted connection from client: ', addr)
    fileSize = int(grab_info(client, 10))

    print(f'The file size is {fileSize}')
    fileData = grab_info(client, fileSize)
    
    print('Below is file content: ')
    
    print(fileData)
    
    return 

def main():
    if len(sys.argv) < 2: 
        print('Forgot to specify the port number')
        sys.exit()

    # Running on LocalHost and setting the Port based on the argument
    server_ip = "0.0.0.0" 
    server_port = int(sys.argv[1])


    # Create a TCP socket and a file reading object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind that socket to the server IP and port
    server.bind((server_ip, server_port))

    # Start listening on the socket
    server.listen(1)

    # Display a message of the socket listening 
    print("[*] Listening on %s:%d" % (server_ip, server_port))

    while True:
        
        client, addr = server.accept()
        server_accept(client, addr)
        client.close()
        

if __name__ == '__main__': 
    main()   
    
    