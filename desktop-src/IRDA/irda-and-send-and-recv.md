---
title: IrDA and send and recv
description: The send and recv functions are used by IrDA applications to transfer data. The recv function blocks until data is available, and the send function normally will not block.
ms.assetid: '703f2912-5d79-4d28-be48-9b6d8f93295a'
keywords: ["IrDA and send and recv"]
---

# IrDA and send and recv

The [**send**](https://msdn.microsoft.com/library/windows/desktop/ms740149) and [**recv**](https://msdn.microsoft.com/library/windows/desktop/ms740121) functions are used by IrDA applications to transfer data. The recv function blocks until data is available, and the send function normally will not block.

The following sample demonstrates using the [**send**](https://msdn.microsoft.com/library/windows/desktop/ms740149) and [**recv**](https://msdn.microsoft.com/library/windows/desktop/ms740121) functions for an IrDA application.

``` syntax
int   BytesRead, BytesSent;
char  Buffer[4096];

// recv() example
if ((BytesRead = recv(Sock, Buffer, sizeof(Buffer), 0)) == SOCKET_ERROR)
{
    // call WSAGetLastError
}
if (BytesRead == 0)
{
    // peer has closed the connection and I have all the data
    // close the socket now
}

// send() example
if ((BytesSent = send(Sock, Buffer, sizeof(Buffer), 0)) == SOCKET_ERROR)
{
    // call WSAGetLastError
}
// check that BytesSent == sizeof(Buffer)
```

The [**send**](https://msdn.microsoft.com/library/windows/desktop/ms740149) function can block if the peer is not receiving data, indicated by its cessation of [**recv**](https://msdn.microsoft.com/library/windows/desktop/ms740121) function calls. The **send** function stops blocking when the peer resumes **recv** calls. A **recv** call with a length of zero has the special meaning: the client has performed a graceful close on the socket. In this case, the application can assume it has received all data that was sent by the peer. If any unrecoverable protocol error occurs during the connection, the **send** or **recv** functions return an error code and the connection is aborted.

 

 




