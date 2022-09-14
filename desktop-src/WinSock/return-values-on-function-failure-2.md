---
description: The manifest constant SOCKET\_ERROR is provided for checking function failure. Although use of this constant is not mandatory, it is recommended. The following example illustrates the use of the SOCKET\_ERROR constant.
ms.assetid: b46203dc-5666-413b-90fe-8432318f3037
title: Return Values on Function Failure
ms.topic: article
ms.date: 05/31/2018
---

# Return Values on Function Failure

The manifest constant **SOCKET\_ERROR** is provided for checking function failure. Although use of this constant is not mandatory, it is recommended. The following example illustrates the use of the **SOCKET\_ERROR** constant.

Typical BSD Style (will not work on Windows)


```C++
        r = recv(ClientSocket, recvbuf, recvbuflen, 0);
        if (r == -1     /* or r < 0 */
            && errno == EWOULDBLOCK) {
            printf("recv failed with error: EWOULDBLOCK\n");
        }    
```



Windows Style


```C++
        iResult = recv(ClientSocket, recvbuf, recvbuflen, 0);
        if (iResult == SOCKET_ERROR ) {
            iError = WSAGetLastError();
            if (iError == WSAEWOULDBLOCK)
                printf("recv failed with error: WSAEWOULDBLOCK\n");
            else
                printf("recv failed with error: %ld\n", iError);

            closesocket(ClientSocket);
            WSACleanup();
            return 1;
        }    
```



## Related topics

<dl> <dt>

[Error Codes - errno, h\_errno and WSAGetLastError](error-codes-errno-h-errno-and-wsagetlasterror-2.md)
</dt> <dt>

[Handling Winsock Errors](handling-winsock-errors.md)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> <dt>

[Windows Sockets Error Codes](windows-sockets-error-codes-2.md)
</dt> </dl>

 

 



