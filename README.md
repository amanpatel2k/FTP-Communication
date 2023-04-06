# CPSC-471-Programming-1


#### Programming Assignment #1

## Project Description: 

The goal of this project is to develop a simplified FTP server and FTP client communication program. The client will have the ability to specify specific commands such as ls, get, put, and quit. All of these commands will allow the client to communicate with the sever in uploading, downloading, and viewing any available files. 

## Project Overview

After running both the server and client, the user can start entering commands such as get, put, ls, and quit. 

Ls Command: If the user types "ls" from the client side, the server will display the list of file

Get Command: If the user types "get" with a filename for instance, "get myText.txt", then the server will downloaded the file and display the content on the client side. 

Put Command: If the user types "put" with a filename for instance, "put myText.txt", then the server will uploaded the file. 

Quit Command: If the user types "quit" then the server and client will close. 

## Group Members:

# Name: Aman Patel, Kanwaljeet Ahluwalia, and Ali Tahami
# Email: amanpatel2k@csu.fullerton.edu, kanahluwalia@csu.Fullerton.edu, Atahami3@csu.Fullerton.edu

## Programming Language: 

Python 

## Instructions to Run:  
1. Have 2 terminals open: one for client and one for server. 
    -> One of the terminal is the client & the other is the server

2. First we run server program. 
    -> Run: "python pythonserv.py 8000
        -> The 8000 is the Port Number 
            -> You can choose any Port Number 

3. After running the server, we run the client program:
    -> Run: "python cli.py 127.0.0.1 8000" 
        -> The 127.0.0.1 is the LocalHost 
        -> The 8000 is the Port Number 
            -> You can choose any Port Number 

4. Once the server and client are both running, then you can start sending commands from the client to the server
