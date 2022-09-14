---
description: WSPGetSockName is used to retrieve the local address for bound sockets.
ms.assetid: 5f3c9aa8-97fe-48a1-a3f5-156c9bddb1b2
title: Determining Local and Remote Names
ms.topic: article
ms.date: 05/31/2018
---

# Determining Local and Remote Names

[**WSPGetSockName**](/previous-versions/windows/desktop/legacy/ms742280(v=vs.85)) is used to retrieve the local address for bound sockets. This is especially useful when a [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85)) call has been made without doing a [**WSPBind**](/previous-versions/windows/hardware/network/ff566268(v=vs.85)) first; **WSPGetSockName** provides the only means to determine the local association which has been set implicitly by the provider.

After a connection has been set up, [**WSPGetPeerName**](/previous-versions/windows/desktop/legacy/ms742278(v=vs.85)) can be used to determine the address of the peer to which a socket is connected.

 

 
