---
description: WSPCloseSocket releases the socket descriptor so that any pending operations in any threads of the same process will be aborted, and any further reference to it will fail.
ms.assetid: 658d0c35-05d4-4b51-a4d3-a3b441a2c735
title: Closing Sockets
ms.topic: article
ms.date: 05/31/2018
---

# Closing Sockets

[**WSPCloseSocket**](/previous-versions/windows/hardware/network/ff566273(v=vs.85)) releases the socket descriptor so that any pending operations in any threads of the same process will be aborted, and any further reference to it will fail. Note that a reference count should be employed for shared sockets, and only if this is the last reference to an underlying socket, should the information associated with this socket be discarded, provided graceful close is not requested (that is, SO\_DONTLINGER is not set). In the case of SO\_DONTLINGER being set, any data queued for transmission will be sent, if possible, before information associated with the socket is released. See **WSPCloseSocket** for more information.

For nonIFS service providers, [**WPUCloseSocketHandle**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpuclosesockethandle) must be invoked to release the socket handle back to the Windows Sockets 2 DLL.

 

 
