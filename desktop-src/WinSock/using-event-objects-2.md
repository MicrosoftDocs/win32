---
Description: Windows Sockets event objects are simple constructs that can be created and closed, set and cleared, waited upon and polled.
ms.assetid: 4254937c-7ee6-49a3-9f30-09aebaf2265b
title: Using Event Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Event Objects

Windows Sockets event objects are simple constructs that can be created and closed, set and cleared, waited upon and polled. The accepted model is for clients to create an event object and supply the handle as a parameter (or as a component of a parameter structure) in functions such as [**WSPSend**](/windows/win32/Ws2spi/?branch=master) and [**WSPEventSelect**](/windows/win32/Ws2spi/?branch=master). When the nominated condition has occurred, the service provider uses the handle to set the event object by calling [**WPUSetEvent**](/windows/win32/Ws2spi/nf-ws2spi-wpusetevent?branch=master). Meanwhile, the Winsock SPI client may either block and wait or poll until the event object becomes set (signaled). The client may subsequently clear or reset the event object and use it again.

 

 



