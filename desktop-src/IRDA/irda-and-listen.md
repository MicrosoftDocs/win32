---
title: IrDA and listen
description: The Windows Sockets listen function is used by IrDA server applications to place the stack in a mode to receive incoming connections on the specified socket. The listen function does not block.
ms.assetid: 33e5476f-164a-496a-ae90-a08ce756d081
keywords:
- IrDA and listen
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IrDA and listen

The Windows Sockets [**listen**](https://msdn.microsoft.com/library/windows/desktop/ms739168) function is used by IrDA server applications to place the stack in a mode to receive incoming connections on the specified socket. The **listen** function does not block.

``` syntax
if (listen(ServSock, 2) == SOCKET_ERROR)
{
    // call WSAGetLastError
}
```

The *backlog* parameter specifies how many inbound connections the stack should accept on behalf of the application before the application is able to further process (using the Windows Sockets [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function) those connections.

 

 




