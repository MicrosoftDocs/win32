---
description: WSPConnect establishes a default destination address to enable a socket to be used with subsequent send (WSPSend) and receive (WSPRecv) operations.
ms.assetid: efd57cb1-9736-4527-8e20-ab9304e3a8f6
title: Connecting to a Default Peer
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to a Default Peer

For a socket bound to a connectionless protocol, the operation performed by [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85)) is merely to establish a default destination address so that the socket may be used with subsequent connection-oriented send and receive operations ([**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85)) and [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85))). Any datagrams received from an address other than the destination address specified will be discarded.

 

 
