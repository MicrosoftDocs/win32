---
description: For a client to communicate on a network, it must connect to a server.
ms.assetid: fb52d2b7-70fa-497a-bbb4-42b25ea9d136
title: Connecting to a Socket
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to a Socket

For a client to communicate on a network, it must connect to a server.

## To connect to a socket

Call the [**connect**](/windows/desktop/api/Winsock2/nf-winsock2-connect) function, passing the created socket and the [**sockaddr**](sockaddr-2.md) structure as parameters. Check for general errors.


```C++
// Connect to server.
iResult = connect( ConnectSocket, ptr->ai_addr, (int)ptr->ai_addrlen);
if (iResult == SOCKET_ERROR) {
    closesocket(ConnectSocket);
    ConnectSocket = INVALID_SOCKET;
}

// Should really try the next address returned by getaddrinfo
// if the connect call failed
// But for this simple example we just free the resources
// returned by getaddrinfo and print an error message

freeaddrinfo(result);

if (ConnectSocket == INVALID_SOCKET) {
    printf("Unable to connect to server!\n");
    WSACleanup();
    return 1;
}
```



The [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function is used to determine the values in the [**sockaddr**](sockaddr-2.md) structure. In this example, the first IP address returned by the **getaddrinfo** function is used to specify the **sockaddr** structure passed to the [**connect**](/windows/desktop/api/Winsock2/nf-winsock2-connect). If the **connect** call fails to the first IP address, then try the next [**addrinfo**](/windows/win32/api/ws2def/ns-ws2def-addrinfoa) structure in the linked list returned from the **getaddrinfo** function.

The information specified in the [**sockaddr**](sockaddr-2.md) structure includes:

-   the IP address of the server that the client will try to connect to.
-   the port number on the server that the client will connect to. This port was specified as port 27015 when the client called the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function.

Next Step: [Sending and Receiving Data on the Client](sending-and-receiving-data-on-the-client.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Client Application](winsock-client-application.md)
</dt> <dt>

[Creating a Socket for the Client](creating-a-socket-for-the-client.md)
</dt> </dl>

 

 
