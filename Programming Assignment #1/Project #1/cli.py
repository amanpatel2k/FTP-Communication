import socket
import sys
import os.path

# -------------- FUNCTIONS -------------------------------

# Encodes data from a given valid file side
def encoding_data(filename):
    
    # Open the file in read mode
    myFile = open(filename, "r")
    
    # We read all of 65536 bits from the file
    fileData = myFile.read(65536)
        
    # Assuming that we didn't reach the end of the file 
    if fileData: 
            
        # Store the length of the file
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
 
# Grab data from the client based on a buffer size    
def grab_info(client, value): 
    
    # Create an acutal and temp buffer
    recvBuff, tempBuff = b"", b""
    
    while len(recvBuff) < value: 
        
        # Recieve all the data based on value 
        try: 
            tempBuff = client.recv(value)
        # If we reach an error return -1
        except socket.error:
            return -1 
            
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
    if fileSize.decode() == 'faultydata': return True

    print(f'The file size is {int(fileSize)}')
    
    # Acqurie the entire data from the client 
    fileData = grab_info(client, int(fileSize))
    
    print('Below is file content: ')
    
    # Decode and display the data
    print(fileData.decode())
    
    return 
            
# ------------------------ MAIN CODE ---------------------------------
    
# If the length of the arguments is less than 3 then display a message and program quits
if len(sys.argv) < 3: 
    print('Missing the server machine and server port')
    sys.exit()

# Associate variables of the host IP and port 
target_host = str(sys.argv[1])
target_port = int(sys.argv[2])

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# Reset the byte count and fileData to empty 
byteSent, filedata = 0, None

while True: 
    
    # Grab user input
    my_input = input('ftp> ')
    # Split the input by the space
    comamnd_check = my_input.split(" ")
    # input_no_space = my_input.replace(" ", "")
    
    # If user types quit, then program quits
    if comamnd_check[0] == 'quit': break
    
    # Else if user types 'get'
    elif comamnd_check[0] == 'get': 
        # Send the encoded data of the input and file to the server
        client.send(my_input.replace(" ", "").encode())    
        
        myEmphem = int(client.recv(10).decode())
        data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data_sock.connect((target_host, myEmphem))
        
        # Retrieve the data from the server
        data_empty = server_accept(data_sock)
        
        # If data is empty then return invalid data  
        if data_empty: 
            print(f'File Context of "{comamnd_check[1]}" is not a valid file')
        
        data_sock.close()
    
    # Else if user types 'ls' and length of the command is 1
    elif comamnd_check[0] == 'ls' and len(comamnd_check) == 1: 
        # Send the encoding of the command to the server
        client.send(comamnd_check[0].encode())
        
        myEmphem = int(client.recv(10).decode())
        data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data_sock.connect((target_host, myEmphem))
        temp = data_sock.recv(65536)
        print(temp.decode())
        
        data_sock.close()
    
    # Else if user types 'put'
    elif comamnd_check[0] == 'put': 
        
        # Send the encoding of the command 'put'
        client.send(b'put')
        
        myEmphem = int(client.recv(10).decode())
        data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        data_sock.connect((target_host, myEmphem))
        
        # If file does not exist 
        if not os.path.isfile(comamnd_check[1]):
            data_sock.send(b'faultydata')
            print('FAILURE: Invalid Filename')
    
        else: 
            
            # Encode the data from the file
            print(f'We will be uploading this file: {comamnd_check[1]}')
            filedata = encoding_data(comamnd_check[1])
        
            # If file is empty or doesn't exist
            if filedata == 1:
                print('FAILURE')
            
            else:
                byteSent = 0
                # Loop through and sent the data 
                while len(filedata) > byteSent: 
                    byteSent += data_sock.send(filedata[byteSent:])
        
        data_sock.close()
    
    # If user types invalid command
    else: 
        client.send(b'FAILURE')
        print('Invalid command')

    print('\n')

# If user types quit, then the client closes
client.close()
print('Client Closed\n')
            