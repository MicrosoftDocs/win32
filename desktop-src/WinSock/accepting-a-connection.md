---
description: Once the socket is listening for a connection, the program must handle connection requests on that socket.
ms.assetid: d01f3d90-4d83-442e-aada-e7b082ef7699
title: Accepting a Connection (Windows Sockets 2)
ms.topic: article
ms.date: 05/31/2018
---

# Accepting a Connection (Windows Sockets 2)

Once the socket is listening for a connection, the program must handle connection requests on that socket.

**To accept a connection on a socket**

1.  Create a temporary **SOCKET** object called ClientSocket for accepting connections from clients.
    ```C++
    
    SOCKET ClientSocket;

    
    ```

    

2.  Normally a server application would be designed to listen for connections from multiple clients. For high-performance servers, multiple threads are commonly used to handle the multiple client connections.

    There are several different programming techniques using Winsock that can be used to listen for multiple client connections. One programming technique is to create a continuous loop that checks for connection requests using the [**listen**](/windows/desktop/api/Winsock2/nf-winsock2-listen) function (see [Listening on a Socket](listening-on-a-socket.md)). If a connection request occurs, the application calls the [**accept**](/windows/desktop/api/Winsock2/nf-winsock2-accept), [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex), or [**WSAAccept**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaccept) function and passes the work to another thread to handle the request. Several other programming techniques are possible.

    Note that this basic example is very simple and does not use multiple threads. The example also just listens for and accepts only a single connection.

    ```C++
    
    ClientSocket = INVALID_SOCKET;

    // Accept a client socket
    ClientSocket = accept(ListenSocket, NULL, NULL);
    if (ClientSocket == INVALID_SOCKET) {
        printf("accept failed: %d\n", WSAGetLastError());
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }
     
    
    ```

    

3.  When the client connection has been accepted, a server application would normally pass the accepted client socket (the ClientSocket variable in the above sample code) to a worker thread or an I/O completion port and continue accepting additional connections. In this basic example, the server continues to the next step.

    There are a number of other programming techniques that can be used to listen for and accept multiple connections. These include using the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) or [**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll) functions. Examples of some of these various programming techniques are illustrated in the [Advanced Winsock Samples](getting-started-with-winsock.md) included with the Microsoft Windows Software Development Kit (SDK).

    > [!Note]  
    > On Unix systems, a common programming technique for servers was for an application to listen for connections. When a connection was accepted, the parent process would call the **fork** function to create a new child process to handle the client connection, inheriting the socket from the parent. This programming technique is not supported on Windows, since the **fork** function is not supported. This technique is also not usually suitable for high-performance servers, since the resources needed to create a new process are much greater than those needed for a thread.

     

Next Step: [Receiving and Sending Data on the Server](receiving-and-sending-data-on-the-server.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Server Application](winsock-server-application.md)
</dt> <dt>

[Listening on a Socket](listening-on-a-socket.md)
</dt> </dl>

 

 
