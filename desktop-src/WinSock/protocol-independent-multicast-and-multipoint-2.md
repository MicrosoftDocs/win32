---
Description: Windows Sockets 2 provides a generic method for utilizing the multipoint and multicast capabilities of transports.
ms.assetid: 75cd8f21-a391-4626-b909-0760d12db995
title: Protocol-Independent Multicast and Multipoint
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Protocol-Independent Multicast and Multipoint

Windows Sockets 2 provides a generic method for utilizing the multipoint and multicast capabilities of transports. This generic method implements these features just as it allows the basic data transport capabilities of numerous transport protocols to be accessed. The term, multipoint, is used hereafter to refer to both multicast and multipoint communications.

Current multipoint implementations (for example, IP multicast, ST-II, T.120, and ATM UNI) vary widely. How nodes join a multipoint session, whether a particular node is designated as a central or root node, and whether data is exchanged between all nodes or only between a root node and the various leaf nodes differ among implementations. The [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure for Windows Sockets 2 is used to declare the various multipoint attributes of a protocol. By examining these attributes, the programmer knows what conventions to follow with the applicable Windows Sockets 2 functions to set up, utilize, and tear down multipoint sessions.

The following summarizes Winsock features that support multipoint:

-   Two-attribute bits in the [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure.
-   Four flags defined for the *dwFlags* parameter of the [**WSASocket**](/windows/win32/Winsock2/nf-winsock2-wsasocketa?branch=master) function.
-   One function, [**WSAJoinLeaf**](/windows/win32/Winsock2/nf-winsock2-wsajoinleaf?branch=master), for adding leaf nodes into a multipoint session
-   Two [**WSAIoctl**](/windows/win32/Winsock2/nf-winsock2-wsaioctl?branch=master) command codes for controlling multipoint loopback and establishing the scope for multicast transmissions. (The latter corresponds to the IP multicast time-to-live or TTL parameter.)

> [!Note]  
> The inclusion of these multipoint features in Windows Sockets 2 does not preclude an application from using an existing protocol-dependent interface, such as the Deering socket options for IP multicast.

 

See [Multipoint and Multicast Semantics](multipoint-and-multicast-semantics-2.md) for detailed information on how the various multipoint schemes are characterized and how the applicable features of Windows Sockets 2 are utilized.

 

 



