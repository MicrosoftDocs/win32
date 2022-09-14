---
description: After initialization, a SOCKET object must be instantiated for use by the server.
ms.assetid: 2f3a7cab-3296-41ec-ac7e-224655b92a7c
title: Creating a Socket for the Server
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Socket for the Server

After initialization, a **SOCKET** object must be instantiated for use by the server.

**To create a socket for the server**

1.  The [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function is used to determine the values in the [**sockaddr**](sockaddr-2.md) structure:

    -   **AF\_INET** is used to specify the IPv4 address family.
    -   **SOCK\_STREAM** is used to specify a stream socket.
    -   **IPPROTO\_TCP** is used to specify the TCP protocol .
    -   **AI\_PASSIVE** flag indicates the caller intends to use the returned socket address structure in a call to the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function. When the **AI\_PASSIVE** flag is set and *nodename* parameter to the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function is a **NULL** pointer, the IP address portion of the socket address structure is set to **INADDR\_ANY** for IPv4 addresses or **IN6ADDR\_ANY\_INIT** for IPv6 addresses.
    -   27015 is the port number associated with the server that the client will connect to.

    The [**addrinfo**](/windows/win32/api/ws2def/ns-ws2def-addrinfoa) structure is used by the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function.

    ```C++
    #define DEFAULT_PORT "27015"

    struct addrinfo *result = NULL, *ptr = NULL, hints;

    ZeroMemory(&hints, sizeof (hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
    hints.ai_flags = AI_PASSIVE;

    // Resolve the local address and port to be used by the server
    iResult = getaddrinfo(NULL, DEFAULT_PORT, &hints, &result);
    if (iResult != 0) {
        printf("getaddrinfo failed: %d\n", iResult);
        WSACleanup();
        return 1;
    }
    ```

    

2.  Create a **SOCKET** object called ListenSocket for the server to listen for client connections.
    ```C++
    SOCKET ListenSocket = INVALID_SOCKET;
    ```

    

3.  Call the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function and return its value to the ListenSocket variable. For this server application, use the first IP address returned by the call to [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) that matched the address family, socket type, and protocol specified in the *hints* parameter. In this example, a TCP stream socket for IPv4 was requested with an address family of IPv4, a socket type of SOCK\_STREAM and a protocol of IPPROTO\_TCP. So an IPv4 address is requested for the ListenSocket.

    If the server application wants to listen on IPv6, then the address family needs to be set to AF\_INET6 in the *hints* parameter. If a server wants to listen on both IPv6 and IPv4, two listen sockets must be created, one for IPv6 and one for IPv4. These two sockets must be handled separately by the application.

    Windows Vista and later offer the ability to create a single IPv6 socket that is put in dual stack mode to listen on both IPv6 and IPv4. For more information on this feature, see [Dual-Stack Sockets](dual-stack-sockets.md).

    ```C++
    // Create a SOCKET for the server to listen for client connections

    ListenSocket = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
    ```

    

4.  Check for errors to ensure that the socket is a valid socket.
    ```C++
    if (ListenSocket == INVALID_SOCKET) {
        printf("Error at socket(): %ld\n", WSAGetLastError());
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }
    ```

    

Next Step: [Binding a Socket](binding-a-socket.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Initializing Winsock](initializing-winsock.md)
</dt> <dt>

[Winsock Server Application](winsock-server-application.md)
</dt> </dl>

 

 
