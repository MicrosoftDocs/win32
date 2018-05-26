---
Description: Windows Sockets 2 (Winsock) interface elements for multipoint and multicast.
ms.assetid: c6f704cf-031b-4714-9f07-2d7715a157a0
title: Windows Sockets 2 Interface Elements for Multipoint and Multicast
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Sockets 2 Interface Elements for Multipoint and Multicast

The mechanisms that have been incorporated into Windows Sockets 2 for utilizing multipoint capabilities can be summarized as follows:

-   Three attribute bits in the [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure.
-   Four flags defined for the *dwFlags* parameter of [**WSASocket**](/windows/win32/Winsock2/nf-winsock2-wsasocketa?branch=master).
-   One function, [**WSAJoinLeaf**](/windows/win32/Winsock2/nf-winsock2-wsajoinleaf?branch=master), for adding leaf nodes into a multipoint session.
-   Two [**WSAIoctl**](/windows/win32/Winsock2/nf-winsock2-wsaioctl?branch=master) command codes for controlling multipoint loopback and the scope of multicast transmissions.

The following sections describe these interface elements in more detail:

-   [Semantics for Joining Multipoint Leaves](semantics-for-joining-multipoint-leaves-2.md)
-   [How Existing Multipoint Protocols Support These Extensions](how-existing-multipoint-protocols-support-these-extensions-2.md)

 

 



