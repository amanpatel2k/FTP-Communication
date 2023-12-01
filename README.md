# FTP Communication Program

## Programming Assignment #1

## Group Members:

#### Name: Aman Patel, Kanwaljeet Ahluwalia, and Ali Tahami
#### Email: amanpatel2k@csu.fullerton.edu, kanahluwalia@csu.Fullerton.edu, Atahami3@csu.Fullerton.edu

## Project Description: 

The goal of this project is to develop a simplified FTP server and FTP client communication program. The client will have the ability to specify specific commands such as ls, get, put, and quit. All of these commands will allow the client to communicate with the sever in uploading, downloading, and viewing any available files. 

## Project Overview

After running both the server and client, the user can start entering commands such as get, put, ls, and quit. 

LS Command: If the user types "ls" from the client side, the server will display the list of file

GET Command: If the user types "get" with a filename for instance, "get myText.txt", then the server will downloaded the file and display the content on the client side. 

PUT Command: If the user types "put" with a filename for instance, "put myText.txt", then the server will uploaded the file. 

QUIT Command: If the user types "quit" then the server and client will close.

## Images for Each Command Being Used: 

LS Command:  
![Screenshot 2023-04-25 at 1 34 08 PM](https://user-images.githubusercontent.com/50725935/234397243-2d1a3502-29a4-4ec9-85df-9babc24e7ce2.png)

GET Command: 
![Screenshot 2023-04-25 at 1 35 31 PM](https://user-images.githubusercontent.com/50725935/234397507-0fd95902-718f-49fb-bc83-5b11de837797.png)

PUT Command: 
![Screenshot 2023-04-25 at 1 35 57 PM](https://user-images.githubusercontent.com/50725935/234397611-51ebda91-b967-4fde-ad5f-a71d44dc932e.png)

QUIT Command: 
![Screenshot 2023-04-25 at 1 36 29 PM](https://user-images.githubusercontent.com/50725935/234397702-d6b81bef-5af1-4936-8fe0-bb5dae2a8c93.png)

## Side Cases: 
1. If the client types an invalid command, the server and client will be displayed with a message saying that the command is invalid
2. If the client types an invalid filename, the server and client will be displayed with a message saying file is invalid

Examples of the Side Cases: 

<strong>Image for Side Case #1: </strong>
![Screenshot 2023-04-25 at 1 45 32 PM](https://user-images.githubusercontent.com/50725935/234399487-a924b255-ec55-4afa-83a7-170a2e33d8f5.png)


<strong>Image for Side Case #2: </strong> 
![Screenshot 2023-04-25 at 1 43 34 PM](https://user-images.githubusercontent.com/50725935/234399080-66b24f90-f94c-4936-80d1-ba61105ee9f8.png)


## Programming Language: 

Python 

## Prerequisities to Install: 

<br> Sockets: pip install sockets </br>
<br> Subprocess: pip install future </br>
<br> Threading: pip install threading </br>

## Instructions to Run:  
1. Have 2 terminals open: one for client and one for server. 
    <ol><li>One of the terminal is the client & the other is the server </li></ol>

2. First we run server program. 
    <ol> 
      <li> Run: "python pythonserv.py 8000 </li>
      <li> The 8000 is the Port Number in that you can choose any port number </li>
    </ol>

3. After running the server, we run the client program:
    <ol>
      <li> Run: "python cli.py 127.0.0.1 8000" </li>
      <li> The 127.0.0.1 is the LocalHost  </li>
      <li> The 8000 is the Port Number in that you can choose any port number </li>
    </ol> 
   
4. Once the server and client are both running, then you can start sending commands, such as get filename, put filename, ls, or quit, from the client to the server. A template file, myText.txt, is provided to assist with the get or put command. 

## Image Of The Programming Running 
![Screenshot 2023-04-25 at 2 13 23 PM](https://user-images.githubusercontent.com/50725935/234405288-ce756015-e83e-4267-acb6-0ac3210ace35.png)
