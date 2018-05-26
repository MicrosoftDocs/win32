---
Description: XP1\_SUPPORT\_MULTIPOINT, XP1\_MULTIPOINT\_CONTROL\_PLANE, and XP1\_MULTIPOINT\_DATA\_PLANE attribute parameters in the Winsock WSAPROTOCOL\_INFO structure.
ms.assetid: 62f5b8b0-a404-49d1-b163-026f79a46845
title: Attributes in WSAPROTOCOL\_INFO Structure
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Attributes in WSAPROTOCOL\_INFO Structure

In support of the taxonomy described above, three attribute parameters in the [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure are used to distinguish the schemes used in the control and data planes respectively:

-   XP1\_SUPPORT\_MULTIPOINT with a value of 1 indicates this protocol entry supports multipoint communications, and that the following two parameters are meaningful.
-   XP1\_MULTIPOINT\_CONTROL\_PLANE indicates whether the control plane is rooted (value = 1) or nonrooted (value = 0).
-   XP1\_MULTIPOINT\_DATA\_PLANE indicates whether the data plane is rooted (value = 1) or nonrooted (value = 0).

Note that two [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) entries would be present if a multipoint protocol supported both rooted and nonrooted data planes, one entry for each.

The application can use [**WSAEnumProtocols**](/windows/win32/Winsock2/nf-winsock2-wsaenumprotocolsa?branch=master) to discover whether multipoint communications is supported for a given protocol and, if so, how it is supported with respect to the control and data planes, respectively.

 

 



