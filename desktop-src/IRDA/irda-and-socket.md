---
title: IrDA and socket
description: The Windows Sockets socket function creates a connection endpoint of type SOCKET.
ms.assetid: a43d0c18-3936-46f9-acec-232711420c93
keywords:
- IrDA and socket
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IrDA and socket

The Windows Sockets [**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506) function creates a connection endpoint of type SOCKET. The connection endpoint is an application anchor for future references to a connection; the connection is not established with this function call. Clients and servers begin all communication by opening a socket.

The following sample demonstrates using the [**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506) function for an IrDA application:

``` syntax
SOCKET ServSock;

if ((ServSock = socket(AF_IRDA, SOCK_STREAM, 0)) == INVALID_SOCKET)
{
    // call WSAGetLastError
}
```

 

 




