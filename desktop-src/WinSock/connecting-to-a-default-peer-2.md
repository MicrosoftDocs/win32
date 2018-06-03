---
Description: WSPConnect establishes a default destination address to enable a socket to be used with subsequent send (WSPSend) and receive (WSPRecv) operations.
ms.assetid: efd57cb1-9736-4527-8e20-ab9304e3a8f6
title: Connecting to a Default Peer
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to a Default Peer

For a socket bound to a connectionless protocol, the operation performed by [**WSPConnect**](/windows/desktop/api/Ws2spi/) is merely to establish a default destination address so that the socket may be used with subsequent connection-oriented send and receive operations ([**WSPSend**](/windows/desktop/api/Ws2spi/) and [**WSPRecv**](/windows/desktop/api/Ws2spi/)). Any datagrams received from an address other than the destination address specified will be discarded.

 

 



