import socket
import os
import sys

# -------------- FUNCTIONS -------------------------------

def encoding_data(myFile):
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
    
    else:
        return 1 
            
# ------------------------ MAIN CODE ---------------------------------

def myMain():
    
    if len(sys.argv) < 4: 
        print('Missing the server machine and server port')
        sys.exit()
    
    # Associate variables of the host IP and port 
    target_host = str(sys.argv[1])
    target_port = int(sys.argv[2])
    
    # Remove this after: but for now testing purpose
    import_file = sys.argv[3]

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Create a file instance
    myFile = open(import_file, "r")
    
    # connect the client
    client.connect((target_host, target_port))
    
    # Reset the byte count and fileData to empty 
    byteSent, fileData = 0, None
    
    while True: 
        fileData = encoding_data(myFile)
    
        if fileData != 1:
            byteSent = 0
            
            # Loop through and sent the data 
            while len(fileData) > byteSent: 
                byteSent += client.send(fileData[byteSent:])
        else: 
            break
    
    print(f"Sent {byteSent} bytes.")
    client.close()  
    myFile.close()


if __name__ == '__main__': 
    myMain()