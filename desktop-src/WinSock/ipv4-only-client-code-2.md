---
description: The following code is the Simplec.c file, which is an IPv4-only Windows Sockets client (an IPv6 enabled version of the Simplec.c file can be found in Appendix B).
ms.assetid: 32a11b37-c2e9-455b-8359-92186d3801d1
title: IPv4-only Client Code
ms.topic: article
ms.date: 05/31/2018
---

# IPv4-only Client Code

The following code is the Simplec.c file, which is an IPv4-only Windows Sockets client (an IPv6 enabled version of the Simplec.c file can be found in Appendix B). This code is provided for comparison purposes only — use Appendix B for an example of how to write an IPv6-enabled client.


```C++
/******************************************************************************\
* simplec.c - Simple TCP/UDP client using Winsock 1.1
* 
*       This is a part of the Microsoft<entity type="reg"/> Source Code Samples.
*       Copyright 1996 - 2000 Microsoft Corporation.
*       All rights reserved.
*       This source code is only intended as a supplement to
*       Microsoft Development Tools and/or WinHelp<entity type="reg"/> documentation.
*       See these sources for detailed information regarding the
*       Microsoft samples programs.
\******************************************************************************/
#ifndef UNICODE
#define UNICODE
#endif

#define WIN32_LEAN_AND_MEAN

#include <winsock2.h>
#include <Ws2tcpip.h>
#include <stdio.h>
#include <stdlib.h>

// Link with ws2_32.lib
#pragma comment(lib, "Ws2_32.lib")

#define DEFAULT_PORT 5001
#define DEFAULT_PROTO SOCK_STREAM // TCP

void Usage(char *progname) {
    fprintf(stderr,"Usage\n%s -p [protocol] -n [server] -e [endpoint] \
    -l [iterations]\n",
        progname);
    fprintf(stderr,"Where:\n\tprotocol is one of TCP or UDP\n");
    fprintf(stderr,"\tserver is the IP address or name of server\n");
    fprintf(stderr,"\tendpoint is the port to listen on\n");
    fprintf(stderr,"\titerations is the number of loops to execute\n");
    fprintf(stderr,"\t(-l by itself makes client run in an infinite loop,");
    fprintf(stderr," Hit Ctrl-C to terminate it)\n");
    fprintf(stderr,"Defaults are TCP , localhost and 5001\n");
    WSACleanup();
    exit(1);
}

int main(int argc, char **argv) {

    char Buffer[128];
    char *server_name= "localhost";
    unsigned short port = DEFAULT_PORT;
    int retval, loopflag=0;
    int i, loopcount,maxloop=-1;
    unsigned int addr;
    int socket_type = DEFAULT_PROTO;
    struct sockaddr_in server;
    struct hostent *hp;
    WSADATA wsaData;
    SOCKET  conn_socket;

    if (argc >1) {
        for(i=1;i <argc;i++) {
            if ( (argv[i][0] == '-') || (argv[i][0] == '/') ) {
                switch(tolower(argv[i][1])) {
                    case 'p':
                        if (!_stricmp(argv[i+1], "TCP") )
                            socket_type = SOCK_STREAM;
                        else if (!_stricmp(argv[i+1], "UDP") )
                            socket_type = SOCK_DGRAM;
                        else
                            Usage(argv[0]);
                        i++;
                        break;

                    case 'n':
                        server_name = argv[++i];
                        break;
                    case 'e':
                        port = (USHORT) atoi(argv[++i]);
                        break;
                    case 'l':
                        loopflag =1;
                        if (argv[i+1]) {
                            if (argv[i+1][0] != '-') 
                                maxloop = atoi(argv[i+1]);
                        }
                        else
                            maxloop = -1;
                        i++;
                        break;
                    default:
                        Usage(argv[0]);
                        break;
                }
            }
            else
                Usage(argv[0]);
        }
    }
    
    if ((retval = WSAStartup(0x202,&wsaData)) != 0) {
        fprintf(stderr,"WSAStartup failed with error %d\n",retval);
        WSACleanup();
        return -1;
    }
    
    if (port == 0){
        Usage(argv[0]);
    }

    //
    // Attempt to detect if we should call gethostbyname() or
    // gethostbyaddr()

    if (isalpha(server_name[0])) {   /* server address is a name */
        hp = gethostbyname(server_name);
    }
    else  { /* Convert nnn.nnn address to a usable one */
        addr = inet_addr(server_name);
        hp = gethostbyaddr((char *)&addr,4,AF_INET);
    }
    if (hp == NULL ) {
        fprintf(stderr,"Client: Cannot resolve address [%s]: Error %d\n",
            server_name,WSAGetLastError());
        WSACleanup();
        exit(1);
    }

    //
    // Copy the resolved information into the sockaddr_in structure
    //
    memset(&server,0,sizeof(server));
    memcpy(&(server.sin_addr),hp->h_addr,hp->h_length);
    server.sin_family = hp->h_addrtype;
    server.sin_port = htons(port);

    conn_socket = socket(AF_INET,socket_type,0); /* Open a socket */
    if (conn_socket <0 ) {
        fprintf(stderr,"Client: Error Opening socket: Error %d\n",
            WSAGetLastError());
        WSACleanup();
        return -1;
    }

    //
    // Notice that nothing in this code is specific to whether we 
    // are using UDP or TCP.
    // We achieve this by using a simple trick.
    //    When connect() is called on a datagram socket, it does not 
    //    actually establish the connection as a stream (TCP) socket
    //    would. Instead, TCP/IP establishes the remote half of the
    //    ( LocalIPAddress, LocalPort, RemoteIP, RemotePort) mapping.
    //    This enables us to use send() and recv() on datagram sockets,
    //    instead of recvfrom() and sendto()


    printf("Client connecting to: %s\n",hp->h_name);
    if (connect(conn_socket,(struct sockaddr*)&server,sizeof(server))
        == SOCKET_ERROR) {
        fprintf(stderr,"connect() failed: %d\n",WSAGetLastError());
        WSACleanup();
        return -1;
    }

    // cook up a string to send
    //
    loopcount =0;
    while(1) {
        sprintf_s(Buffer,sizeof(Buffer), "This is a small test message [number %d]",loopcount++);
        retval = send(conn_socket,Buffer,sizeof(Buffer),0);
        if (retval == SOCKET_ERROR) {
            fprintf(stderr,"send() failed: error %d\n",WSAGetLastError());
            WSACleanup();
            return -1;
        }
        printf("Sent Data [%s]\n",Buffer);
        retval = recv(conn_socket,Buffer,sizeof (Buffer),0 );
        if (retval == SOCKET_ERROR) {
            fprintf(stderr,"recv() failed: error %d\n",WSAGetLastError());
            closesocket(conn_socket);
            WSACleanup();
            return -1;
        }
        //
        // We are not likely to see this with UDP, since there is no
        // 'connection' established. 
        //
        if (retval == 0) {
            printf("Server closed connection\n");
            closesocket(conn_socket);
            WSACleanup();
            return -1;
        }
        printf("Received %d bytes, data [%s] from server\n",retval,Buffer);
        if (!loopflag){
            printf("Terminating connection\n");
            break;
        }
        else {
            if ( (loopcount >= maxloop) && (maxloop >0) )
                break;
        }
    }
    closesocket(conn_socket);
    WSACleanup();
}
```



 

 



