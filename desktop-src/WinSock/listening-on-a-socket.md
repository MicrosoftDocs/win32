---
description: After the socket is bound to an IP address and port on the system, the server must then listen on that IP address and port for incoming connection requests.
ms.assetid: 83c9f0e7-2e6d-449b-8d97-3d13154112cd
title: Listening on a Socket
ms.topic: article
ms.date: 05/31/2018
---

# Listening on a Socket

After the socket is bound to an IP address and port on the system, the server must then listen on that IP address and port for incoming connection requests.

## To listen on a socket

Call the [**listen**](/windows/desktop/api/Winsock2/nf-winsock2-listen) function, passing as parameters the created socket and a value for the *backlog*, maximum length of the queue of pending connections to accept. In this example, the *backlog* parameter was set to **SOMAXCONN**. This value is a special constant that instructs the Winsock provider for this socket to allow a maximum reasonable number of pending connections in the queue. Check the return value for general errors.


```C++
if ( listen( ListenSocket, SOMAXCONN ) == SOCKET_ERROR ) {
    printf( "Listen failed with error: %ld\n", WSAGetLastError() );
    closesocket(ListenSocket);
    WSACleanup();
    return 1;
}
```



Next Step: [Accepting a Connection](accepting-a-connection.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Server Application](winsock-server-application.md)
</dt> <dt>

[Binding a Socket](binding-a-socket.md)
</dt> </dl>

 

 



