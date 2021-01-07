---
description: Windows Sockets event objects are simple constructs that can be created and closed, set and cleared, waited upon and polled.
ms.assetid: '65a7627e-150e-4ca3-bc17-d2b380ee02d1'
title: Using Event Objects (Windows Sockets 2)
ms.topic: article
ms.date: 05/31/2018
---

# Using Event Objects (Windows Sockets 2)

Windows Sockets event objects are simple constructs that can be created and closed, set and cleared, waited upon and polled. The accepted model is for clients to create an event object and supply the handle as a parameter (or as a component of a parameter structure) in functions such as [**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85)) and [**WSPEventSelect**](/previous-versions/windows/hardware/network/ff566287(v=vs.85)). When the nominated condition has occurred, the service provider uses the handle to set the event object by calling [**WPUSetEvent**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpusetevent). Meanwhile, the Winsock SPI client may either block and wait or poll until the event object becomes set (signaled). The client may subsequently clear or reset the event object and use it again.

 

 
