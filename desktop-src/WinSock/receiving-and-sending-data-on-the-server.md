---
Description: The following code demonstrates the recv and send functions used by the server.
ms.assetid: 26990b06-196a-4fb1-92d8-c5fa096d2b09
title: Receiving and Sending Data on the Server
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Receiving and Sending Data on the Server

The following code demonstrates the [**recv**](/windows/win32/winsock/nf-winsock-recv?branch=master) and [**send**](/windows/win32/Winsock2/nf-winsock2-send?branch=master) functions used by the server.

### To receive and send data on a socket


```C++
#define DEFAULT_BUFLEN 512

char recvbuf[DEFAULT_BUFLEN];
int iResult, iSendResult;
int recvbuflen = DEFAULT_BUFLEN;

// Receive until the peer shuts down the connection
do {

    iResult = recv(ClientSocket, recvbuf, recvbuflen, 0);
    if (iResult > 0) {
        printf("Bytes received: %d\n", iResult);

        // Echo the buffer back to the sender
        iSendResult = send(ClientSocket, recvbuf, iResult, 0);
        if (iSendResult == SOCKET_ERROR) {
            printf("send failed: %d\n", WSAGetLastError());
            closesocket(ClientSocket);
            WSACleanup();
            return 1;
        }
        printf("Bytes sent: %d\n", iSendResult);
    } else if (iResult == 0)
        printf("Connection closing...\n");
    else {
        printf("recv failed: %d\n", WSAGetLastError());
        closesocket(ClientSocket);
        WSACleanup();
        return 1;
    }

} while (iResult > 0);
```



The [**send**](/windows/win32/Winsock2/nf-winsock2-send?branch=master) and [**recv**](/windows/win32/winsock/nf-winsock-recv?branch=master) functions both return an integer value of the number of bytes sent or received, respectively, or an error. Each function also takes the same parameters: the active socket, a **char** buffer, the number of bytes to send or receive, and any flags to use.

Next Step: [Disconnecting the Server](disconnecting-the-server.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Server Application](winsock-server-application.md)
</dt> <dt>

[Accepting a Connection](accepting-a-connection.md)
</dt> </dl>

 

 



