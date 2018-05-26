---
Description: WSPGetSockName is used to retrieve the local address for bound sockets.
ms.assetid: 5f3c9aa8-97fe-48a1-a3f5-156c9bddb1b2
title: Determining Local and Remote Names
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining Local and Remote Names

[**WSPGetSockName**](/windows/win32/Ws2spi/?branch=master) is used to retrieve the local address for bound sockets. This is especially useful when a [**WSPConnect**](/windows/win32/Ws2spi/?branch=master) call has been made without doing a [**WSPBind**](/windows/win32/Ws2spi/?branch=master) first; **WSPGetSockName** provides the only means to determine the local association which has been set implicitly by the provider.

After a connection has been set up, [**WSPGetPeerName**](/windows/win32/Ws2spi/?branch=master) can be used to determine the address of the peer to which a socket is connected.

 

 



