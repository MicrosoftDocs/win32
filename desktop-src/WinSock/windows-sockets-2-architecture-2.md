---
description: The Windows Sockets 2 (Winsock) architecture is compliant with the Windows Open System Architecture (WOSA).
ms.assetid: d4cf1462-2e83-49a5-b698-350ff37aa497
title: Windows Sockets 2 Architecture
ms.topic: article
ms.date: 05/31/2018
---

# Windows Sockets 2 Architecture

The Windows Sockets 2 architecture is compliant with the Windows Open System Architecture (WOSA), as illustrated below:

![windows sockets 2 architecture](images/ovrvw2-1.png)

Winsock defines a standard service provider interface (SPI) between the application programming interface (API), with its functions exported from WS2\_32.dll and the protocol stacks. Consequently, Winsock support is not limited to TCP/IP protocol stacks as is the case for Windows Sockets 1.1.

With the Windows Sockets 2 architecture, it is not necessary or desirable, for stack vendors to supply their own implementation of WS2\_32.dll, since a single WS2\_32.dll must work across all stacks. The WS2\_32.dll and compatibility shims should be viewed in the same way as an operating system component.

 

 



