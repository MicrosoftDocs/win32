---
Description: WSPGetSockName is used to retrieve the local address for bound sockets.
ms.assetid: 5f3c9aa8-97fe-48a1-a3f5-156c9bddb1b2
title: Determining Local and Remote Names
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Determining Local and Remote Names

[**WSPGetSockName**](/windows/desktop/api/Ws2spi/) is used to retrieve the local address for bound sockets. This is especially useful when a [**WSPConnect**](/windows/desktop/api/Ws2spi/) call has been made without doing a [**WSPBind**](/windows/desktop/api/Ws2spi/) first; **WSPGetSockName** provides the only means to determine the local association which has been set implicitly by the provider.

After a connection has been set up, [**WSPGetPeerName**](/windows/desktop/api/Ws2spi/) can be used to determine the address of the peer to which a socket is connected.

 

 



