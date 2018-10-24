---
Description: WSPGetSockName is used to retrieve the local address for bound sockets.
ms.assetid: 5f3c9aa8-97fe-48a1-a3f5-156c9bddb1b2
title: Determining Local and Remote Names
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Determining Local and Remote Names

[**WSPGetSockName**](https://msdn.microsoft.com/en-us/library/ms742280(v=VS.85).aspx) is used to retrieve the local address for bound sockets. This is especially useful when a [**WSPConnect**](https://msdn.microsoft.com/en-us/library/ms742272(v=VS.85).aspx) call has been made without doing a [**WSPBind**](https://msdn.microsoft.com/en-us/library/ms742268(v=VS.85).aspx) first; **WSPGetSockName** provides the only means to determine the local association which has been set implicitly by the provider.

After a connection has been set up, [**WSPGetPeerName**](https://msdn.microsoft.com/en-us/library/ms742278(v=VS.85).aspx) can be used to determine the address of the peer to which a socket is connected.

 

 



