---
title: IrDA and bind
description: The Windows Sockets bind function is used by IrDA server applications to register to receive incoming connections addressed to a specified service name on the specified socket.
ms.assetid: 686c905b-f393-4bdf-8093-23987a120773
keywords:
- IrDA and bind
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IrDA and bind

The Windows Sockets [**bind**](https://msdn.microsoft.com/library/windows/desktop/ms737550) function is used by IrDA server applications to register to receive incoming connections addressed to a specified service name on the specified socket. The **bind** function associates a server socket with an application-level address.

The following sample demonstrates using the [**bind**](https://msdn.microsoft.com/library/windows/desktop/ms737550) function for an IrDA application:

``` syntax
SOCKADDR_IRDA     ServSockAddr = { AF_IRDA, 0, 0, 0, 0, "SampleIrDAService" };
int               SizeOfSockAddr;

if (bind(ServSock, (const struct sockaddr *) &ServSockAddr, sizeof(SOCKADDR_IRDA)) == SOCKET_ERROR)
{
    // call WSAGetLastError
}
```

A [**bind**](https://msdn.microsoft.com/library/windows/desktop/ms737550) function call in an IrDA application causes the stack to generate a new local LSAP-SEL and add it to the IAS database associated with the service name supplied in [**SOCKADDR\_IRDA**](https://msdn.microsoft.com/library/windows/desktop/ms740502).

 

 




