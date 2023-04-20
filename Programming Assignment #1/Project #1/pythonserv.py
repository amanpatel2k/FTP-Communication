import socket
import sys
import subprocess
import threading
import os.path
# -------------- FUNCTIONS -------------------------------

# Grab data from the client based on a buffer size   
def grab_info(client, value): 
    
    # Create an acutal and temp buffer
    recvBuff, tempBuff = b"", b""
    while len(recvBuff) < value: 
        # Recieve all the data based on value 
        tempBuff = client.recv(value)
        
        # There no closed socket 
        if not tempBuff:
            break
        
        # Append/Update data
        recvBuff += tempBuff
        
    return recvBuff

# Accepts the info and display the entire content receive from the server
def server_accept(client): 
    
    # Calculate the file size
    fileSize = grab_info(client, 10)
    
    # If file size is faulty or doesn't exist
    if fileSize.decode() == 'faultydata': 
        print('FAILURE\n') 
        return
    
    print(f'The file size is {int(fileSize)}')
    
    # Acqurie the entire data from the client 
    fileData = grab_info(client, int(fileSize))
    
    print('Below is file content: \n')
    
    # Decode and display the data
    print(fileData.decode())
    print('SUCCESS\n')
    
    return 

# Encodes data from a given valid file side
def encoding_data(filename):

    # If file does not exist
    if not os.path.isfile(filename):
        return -100
    
    # Open the file in read mode
    myFile = open(filename, "r")
     
    # We read all of 65536 bits from the file
    fileData = myFile.read(65536)
        
    # Assuming that we didn't reach the end of the file 
    if fileData: 
            
        # Store the lenght of the file
        dataSizeStr = str(len(fileData))
            
        # Loop and append 0 to the front of the length of the file 
        while len(dataSizeStr) < 10:
            dataSizeStr = "0" + dataSizeStr
            
        # Concatenate the two file together and encoded the data
        tempfileData = dataSizeStr + fileData
        fileData = tempfileData.encode()
        return fileData
    
    # Return 1 if filedata is empty 
    else:
        return 1 
    
def new_connection(): 
    temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    temp.bind(('',0))
    port_number = str(temp.getsockname()[1])
    client.send(port_number.encode())
    temp.listen(1)
    emph_socket, addr = temp.accept()
    return emph_socket
 
# Handles multiple socket clients 
def handle_client(client_socket):
    
    is_quit = False
    
    while True: 
        
        # Read the recv data from the socket and decode the message
        client_read = client_socket.recv(1024)
        user_input = client_read.decode()


        if user_input == 'FAILURE': 
            print('FAILURE\n')
        
        # If user_input is empty/invalid then server closes
        elif not user_input: 
            print('Server Closed\n')
            is_quit = True
            break
        
        else:
            # If server input is 'get'
            if user_input[:3] == 'get':
                
                data_connect = new_connection()
                
                # Encode the data from the given filename
                filedata = 0
                filedata = encoding_data(user_input[3:])
                
                # If filedata is empty or not existance
                if filedata == 1 or filedata == -100:
                    data_connect.send(b'faultydata')
                    print('FAILURE\n')
                
                else: 
                    byteSent = 0
                    # Loop through and sent the data 
                    while len(filedata) > byteSent: 
                        byteSent += data_connect.send(filedata[byteSent:])
                    print('SUCCESS\n')   
                
                data_connect.close()
                    
            # If user input is 'ls'   
            elif user_input[:2] == 'ls': 
                
                data_connect = new_connection()
                
                # Grab all the data of the server directory
                temp = subprocess.getstatusoutput('ls -l')[1]
                
                # If the data is not empty then display them
                if temp:
                    # print(temp)
                    data_connect.send(temp.encode())
                    print('SUCCESS\n')
                else: 
                    print('FAILURE\n')
                
                data_connect.close()

            # If the user input is 'put'
            elif user_input[:3] == 'put':
                # Server accepts the connection and uploads the filedata
                data_connect = new_connection()
                server_accept(data_connect)
                
                data_connect.close()
    
    # If the server types 'quit' it returns -1            
    if is_quit == True: 
        client_socket.close()
        return -1
    else: 
        client_socket.close()
    
# ------------------------ MAIN CODE ---------------------------------

# If the length of the arguments is less than 2 then display a message and program quits
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
    
    # Accepts the request from the clients
    client, addr = server.accept()
    
    print('Accepted connection from client: ', addr)
    
    # Creates different thread for multiple clients request and star then
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    
    # Once the client presents None then the program quits
    if client_handler.join() == None:
        break

# Server closes  
server.close()
    
