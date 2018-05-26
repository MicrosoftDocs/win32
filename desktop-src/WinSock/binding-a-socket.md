---
Description: For a server to accept client connections, it must be bound to a network address within the system.
ms.assetid: d08fb1a5-af17-4116-8757-ba0a513fb323
title: Binding a Socket
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Binding a Socket

For a server to accept client connections, it must be bound to a network address within the system. The following code demonstrates how to bind a socket that has already been created to an IP address and port. Client applications use the IP address and port to connect to the host network.

## To bind a socket

The [**sockaddr**](sockaddr-2.md) structure holds information regarding the address family, IP address, and port number.

Call the [**bind**](/windows/win32/winsock/nf-winsock-bind?branch=master) function, passing the created **socket** and [**sockaddr**](sockaddr-2.md) structure returned from the [**getaddrinfo**](/windows/win32/Ws2tcpip/nf-ws2tcpip-getaddrinfo?branch=master) function as parameters. Check for general errors.


```C++
    // Setup the TCP listening socket
    iResult = bind( ListenSocket, result->ai_addr, (int)result->ai_addrlen);
    if (iResult == SOCKET_ERROR) {
        printf("bind failed with error: %d\n", WSAGetLastError());
        freeaddrinfo(result);
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }
```



Once the [**bind**](/windows/win32/winsock/nf-winsock-bind?branch=master) function is called, the address information returned by the [**getaddrinfo**](/windows/win32/Ws2tcpip/nf-ws2tcpip-getaddrinfo?branch=master) function is no longer needed. The [**freeaddrinfo**](/windows/win32/Ws2tcpip/nf-ws2tcpip-freeaddrinfo?branch=master) function is called to free the memory allocated by the **getaddrinfo** function for this address information.


```C++
    freeaddrinfo(result);

```



Next Step: [Listening on a Socket](listening-on-a-socket.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Server Application](winsock-server-application.md)
</dt> <dt>

[Creating a Socket for the Server](creating-a-socket-for-the-server.md)
</dt> </dl>

 

 



