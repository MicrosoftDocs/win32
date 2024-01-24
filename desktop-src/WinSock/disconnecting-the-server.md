---
description: Once the server is completed receiving data from the client and sending data back to the client, the server disconnects from the client and shutdowns the socket.
ms.assetid: 67f33645-d57a-48bd-9f0c-9e816f528204
title: Disconnecting the Server
ms.topic: article
ms.date: 05/31/2018
---

# Disconnecting the Server

Once the server is completed receiving data from the client and sending data back to the client, the server disconnects from the client and shutdowns the socket.

**To disconnect and shutdown a socket**

1.  When the server is done sending data to the client, the [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown) function can be called specifying SD\_SEND to shutdown the sending side of the socket. This allows the client to release some of the resources for this socket. The server application can still receive data on the socket.
    ```C++
    // shutdown the send half of the connection since no more data will be sent
    iResult = shutdown(ClientSocket, SD_SEND);
    if (iResult == SOCKET_ERROR) {
        printf("shutdown failed: %d\n", WSAGetLastError());
        closesocket(ClientSocket);
        WSACleanup();
        return 1;
    }
    ```

    

2.  When the client application is done receiving data, the [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function is called to close the socket.

    When the client application is completed using the Windows Sockets DLL, the [**WSACleanup**](/windows/desktop/api/winsock/nf-winsock-wsacleanup) function is called to release resources.

    ```C++
    // cleanup
    closesocket(ClientSocket);
    WSACleanup();

    return 0;
    ```

    

## Complete Server Source Code

-   [Complete Server Code](complete-server-code.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Server Application](winsock-server-application.md)
</dt> <dt>

[Receiving and Sending Data on the Server](receiving-and-sending-data-on-the-server.md)
</dt> <dt>

[Running the Winsock Client and Server Code Sample](finished-server-and-client-code.md)
</dt> </dl>

 

 



