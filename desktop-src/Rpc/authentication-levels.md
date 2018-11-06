---
title: Authentication Levels
description: Microsoft RPC provides multiple levels of authentication.
ms.assetid: d9ed938e-4cd4-4355-8d08-830f955dd00c
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Levels

Microsoft RPC provides multiple levels of authentication. Depending on the authentication level, the origin of the traffic (which security principal sent the traffic) can be verified when the connection is established, when the client starts a new remote procedure call, or during each packet exchange between the client and server.

Even when the sender of the traffic is verified, security is still weak, since such verification does not ensure the packet was not modified or corrupted en route; it only verifies that the packet came from the given principal. For greater security, distributed applications can set the RPC run-time library to verify that none of the data exchanged between the client and server is modified. The RPC library can also encrypt the contents of every packet before sending it. In general, applications that want to secure their traffic should use only the last two levels—integrity and privacy.

Be aware that higher levels of authentication require higher computational overhead. You, as the developer, must decide which is more important for your application—speed or security. Most developers find that with some performance testing, they can achieve acceptable performance levels while maintaining adequate security.

The client and the server portions of the distributed application must use the same authentication level. For a list of RPC authentication levels, see [Authentication-Level Constants](authentication-level-constants.md).

 

 




