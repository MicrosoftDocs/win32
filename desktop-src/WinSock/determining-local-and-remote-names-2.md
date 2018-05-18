---
Description: 'WSPGetSockName is used to retrieve the local address for bound sockets.'
ms.assetid: '5f3c9aa8-97fe-48a1-a3f5-156c9bddb1b2'
title: Determining Local and Remote Names
---

# Determining Local and Remote Names

[**WSPGetSockName**](wspgetsockname-2.md) is used to retrieve the local address for bound sockets. This is especially useful when a [**WSPConnect**](wspconnect-2.md) call has been made without doing a [**WSPBind**](wspbind-2.md) first; **WSPGetSockName** provides the only means to determine the local association which has been set implicitly by the provider.

After a connection has been set up, [**WSPGetPeerName**](wspgetpeername-2.md) can be used to determine the address of the peer to which a socket is connected.

 

 



