---
title: IrDA and closesocket
description: The Windows Sockets closesocket function initiates a graceful close on the connection, and releases the socket handle.
ms.assetid: 220d6437-2c31-4ba7-bd36-36cebaff98a8
keywords:
- IrDA and closesocket
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IrDA and closesocket

The Windows Sockets [**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582) function initiates a graceful close on the connection, and releases the socket handle.

The following sample demonstrates using the [**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582) functions for an IrDA application:

``` syntax
if (closesocket(Sock) == SOCKET_ERROR)
{
    // call WSAGetLastError
}
```

 

 




