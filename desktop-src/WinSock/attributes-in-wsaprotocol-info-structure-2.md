---
description: XP1\_SUPPORT\_MULTIPOINT, XP1\_MULTIPOINT\_CONTROL\_PLANE, and XP1\_MULTIPOINT\_DATA\_PLANE attribute parameters in the Winsock WSAPROTOCOL\_INFO structure.
ms.assetid: 62f5b8b0-a404-49d1-b163-026f79a46845
title: Attributes in WSAPROTOCOL_INFO Structure
ms.topic: article
ms.date: 05/31/2018
---

# Attributes in WSAPROTOCOL\_INFO Structure

In support of the taxonomy described above, three attribute parameters in the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure are used to distinguish the schemes used in the control and data planes respectively:

-   XP1\_SUPPORT\_MULTIPOINT with a value of 1 indicates this protocol entry supports multipoint communications, and that the following two parameters are meaningful.
-   XP1\_MULTIPOINT\_CONTROL\_PLANE indicates whether the control plane is rooted (value = 1) or nonrooted (value = 0).
-   XP1\_MULTIPOINT\_DATA\_PLANE indicates whether the data plane is rooted (value = 1) or nonrooted (value = 0).

Note that two [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) entries would be present if a multipoint protocol supported both rooted and nonrooted data planes, one entry for each.

The application can use [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa) to discover whether multipoint communications is supported for a given protocol and, if so, how it is supported with respect to the control and data planes, respectively.

 

 
