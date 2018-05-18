---
Description: 'Windows Sockets 2 (Winsock) interface elements for multipoint and multicast.'
ms.assetid: 'c6f704cf-031b-4714-9f07-2d7715a157a0'
title: Windows Sockets 2 Interface Elements for Multipoint and Multicast
---

# Windows Sockets 2 Interface Elements for Multipoint and Multicast

The mechanisms that have been incorporated into Windows Sockets 2 for utilizing multipoint capabilities can be summarized as follows:

-   Three attribute bits in the [**WSAPROTOCOL\_INFO**](wsaprotocol-info-2.md) structure.
-   Four flags defined for the *dwFlags* parameter of [**WSASocket**](wsasocket-2.md).
-   One function, [**WSAJoinLeaf**](wsajoinleaf-2.md), for adding leaf nodes into a multipoint session.
-   Two [**WSAIoctl**](wsaioctl-2.md) command codes for controlling multipoint loopback and the scope of multicast transmissions.

The following sections describe these interface elements in more detail:

-   [Semantics for Joining Multipoint Leaves](semantics-for-joining-multipoint-leaves-2.md)
-   [How Existing Multipoint Protocols Support These Extensions](how-existing-multipoint-protocols-support-these-extensions-2.md)

 

 



