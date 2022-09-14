---
description: Once the client is completed sending and receiving data, the client disconnects from the server and shutdowns the socket.
ms.assetid: 33165e5b-e304-42b1-9542-45d8fe8a5218
title: Disconnecting the Client
ms.topic: article
ms.date: 05/31/2018
---

# Disconnecting the Client

Once the client is completed sending and receiving data, the client disconnects from the server and shutdowns the socket.

**To disconnect and shutdown a socket**

1.  When the client is done sending data to the server, the [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown) function can be called specifying SD\_SEND to shutdown the sending side of the socket. This allows the server to release some of the resources for this socket. The client application can still receive data on the socket.
    ```C++
    // shutdown the send half of the connection since no more data will be sent
    iResult = shutdown(ConnectSocket, SD_SEND);
    if (iResult == SOCKET_ERROR) {
        printf("shutdown failed: %d\n", WSAGetLastError());
        closesocket(ConnectSocket);
        WSACleanup();
        return 1;
    }
    ```

    

2.  When the client application is done receiving data, the [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function is called to close the socket.

    When the client application is completed using the Windows Sockets DLL, the [**WSACleanup**](/windows/desktop/api/winsock/nf-winsock-wsacleanup) function is called to release resources.

    ```C++
    // cleanup
    closesocket(ConnectSocket);
    WSACleanup();

    return 0;
    ```

    

## Complete Client Source Code

-   [Complete Client Code](complete-client-code.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Client Application](winsock-client-application.md)
</dt> <dt>

[Sending and Receiving Data on the Client](sending-and-receiving-data-on-the-client.md)
</dt> </dl>

 

 



