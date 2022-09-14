---
description: After initialization, a SOCKET object must be instantiated for use by the client.
ms.assetid: 088a79ef-b430-4860-8edc-902a1a03ed0d
title: Creating a Socket for the Client
ms.topic: article
ms.date: 05/31/2018
---

# Creating a socket for the client

After initialization, a **SOCKET** object must be instantiated for use by the client.

**To create a socket**

1.  Declare an [**addrinfo**](/windows/win32/api/ws2def/ns-ws2def-addrinfoa) object that contains a [**sockaddr**](sockaddr-2.md) structure and initialize these values. For this application, the Internet address family is unspecified so that either an IPv6 or IPv4 address can be returned. The application requests the socket type to be a stream socket for the TCP protocol.
    ```C++
    struct addrinfo *result = NULL,
                    *ptr = NULL,
                    hints;

    ZeroMemory( &hints, sizeof(hints) );
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
    ```

    

2.  Call the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function requesting the IP address for the server name passed on the command line. The TCP port on the server that the client will connect to is defined by DEFAULT\_PORT as 27015 in this sample. The **getaddrinfo** function returns its value as an integer that is checked for errors.
    ```C++
    #define DEFAULT_PORT "27015"

    // Resolve the server address and port
    iResult = getaddrinfo(argv[1], DEFAULT_PORT, &hints, &result);
    if (iResult != 0) {
        printf("getaddrinfo failed: %d\n", iResult);
        WSACleanup();
        return 1;
    }
    ```

    

3.  Create a **SOCKET** object called ConnectSocket.
    ```C++
    SOCKET ConnectSocket = INVALID_SOCKET;
    ```

    

4.  Call the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function and return its value to the ConnectSocket variable. For this application, use the first IP address returned by the call to [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) that matched the address family, socket type, and protocol specified in the *hints* parameter. In this example, a TCP stream socket was specified with a socket type of SOCK\_STREAM and a protocol of IPPROTO\_TCP. The address family was left unspecified (AF\_UNSPEC), so the returned IP address could be either an IPv6 or IPv4 address for the server.

    If the client application wants to connect using only IPv6 or IPv4, then the address family needs to be set to AF\_INET6 for IPv6 or AF\_INET for IPv4 in the *hints* parameter.

    ```C++
    // Attempt to connect to the first address returned by
    // the call to getaddrinfo
    ptr=result;

    // Create a SOCKET for connecting to server
    ConnectSocket = socket(ptr->ai_family, ptr->ai_socktype, 
        ptr->ai_protocol);
    ```

    

5.  Check for errors to ensure that the socket is a valid socket.
    ```C++
    if (ConnectSocket == INVALID_SOCKET) {
        printf("Error at socket(): %ld\n", WSAGetLastError());
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }
    ```

    

The parameters passed to the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function can be changed for different implementations.

Error detection is a key part of successful networking code. If the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) call fails, it returns INVALID\_SOCKET. The **if** statement in the previous code is used to catch any errors that may have occurred while creating the socket. [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns an error number associated with the last error that occurred.

> [!Note]  
> More extensive error checking may be necessary depending on the application.
>
> For example, setting *hints.ai_family* to **AF_UNSPEC** can cause the connect call to fail. If that happens, then use a specific IPv4 (**AF_INET**) or IPv6 (**AF_INET6**) value instead.

[**WSACleanup**](/windows/desktop/api/winsock/nf-winsock-wsacleanup) is used to terminate the use of the WS2\_32 DLL.

Next Step: [Connecting to a Socket](connecting-to-a-socket.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Initializing Winsock](initializing-winsock.md)
</dt> <dt>

[Winsock Client Application](winsock-client-application.md)
</dt> </dl>

 

 
