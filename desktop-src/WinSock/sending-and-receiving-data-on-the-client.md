---
Description: The following code demonstrates the send and recv functions used by the client once a connection is established.
ms.assetid: 9c6d366d-2bc6-4c92-8d0b-21c51e08ed4f
title: Sending and Receiving Data on the Client
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sending and Receiving Data on the Client

The following code demonstrates the [**send**](/windows/win32/Winsock2/nf-winsock2-send?branch=master) and [**recv**](/windows/win32/winsock/nf-winsock-recv?branch=master) functions used by the client once a connection is established.

## Client


```C++
#define DEFAULT_BUFLEN 512

int recvbuflen = DEFAULT_BUFLEN;

char *sendbuf = "this is a test";
char recvbuf[DEFAULT_BUFLEN];

int iResult;

// Send an initial buffer
iResult = send(ConnectSocket, sendbuf, (int) strlen(sendbuf), 0);
if (iResult == SOCKET_ERROR) {
    printf("send failed: %d\n", WSAGetLastError());
    closesocket(ConnectSocket);
    WSACleanup();
    return 1;
}

printf("Bytes Sent: %ld\n", iResult);

// shutdown the connection for sending since no more data will be sent
// the client can still use the ConnectSocket for receiving data
iResult = shutdown(ConnectSocket, SD_SEND);
if (iResult == SOCKET_ERROR) {
    printf("shutdown failed: %d\n", WSAGetLastError());
    closesocket(ConnectSocket);
    WSACleanup();
    return 1;
}

// Receive data until the server closes the connection
do {
    iResult = recv(ConnectSocket, recvbuf, recvbuflen, 0);
    if (iResult > 0)
        printf("Bytes received: %d\n", iResult);
    else if (iResult == 0)
        printf("Connection closed\n");
    else
        printf("recv failed: %d\n", WSAGetLastError());
} while (iResult > 0);
```



The [**send**](/windows/win32/Winsock2/nf-winsock2-send?branch=master) and [**recv**](/windows/win32/winsock/nf-winsock-recv?branch=master) functions both return an integer value of the number of bytes sent or received, respectively, or an error. Each function also takes the same parameters: the active socket, a **char** buffer, the number of bytes to send or receive, and any flags to use.

Next Step: [Disconnecting the Client](disconnecting-the-client.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Winsock Client Application](winsock-client-application.md)
</dt> <dt>

[Connecting to a Socket](connecting-to-a-socket.md)
</dt> </dl>

 

 



