---
description: The socket function created sockets with the overlapped attribute set by default in the first Wsock32.dll, the 32-bit version of Windows Sockets 1.1.
ms.assetid: 2ebf71fd-fcb3-4f2f-bf52-14cd13af012f
title: Default State for a Socket's Overlapped Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Default State for a Socket's Overlapped Attribute

The [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function created sockets with the overlapped attribute set by default in the first Wsock32.dll, the 32-bit version of Windows Sockets 1.1. In order to ensure backward compatibility with currently deployed Wsock32.dll implementations, this will continue to be the case for Windows Sockets 2 as well. That is, in Windows Sockets 2 sockets created with the **socket** function will have the overlapped attribute. However, in order to be more compatible with the rest of the Windows API, sockets created with [**WSASocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsasocketa) will not, default, have the overlapped attribute. This attribute will only be applied if the WSA\_FLAG\_OVERLAPPED bit is set.

 

 



