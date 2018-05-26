---
Description: The Ws2\_32.dll (and layered protocols) will call WSPCleanup once for each invocation of WSPStartup.
ms.assetid: c3b7b648-5727-47d6-9ddc-9d9f6511949d
title: Cleanup
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cleanup

The Ws2\_32.dll (and layered protocols) will call [**WSPCleanup**](/windows/win32/Ws2spi/?branch=master) once for each invocation of [**WSPStartup**](/windows/win32/Ws2spi/nf-ws2spi-wspstartup?branch=master). On each invocation, **WSPCleanup** should decrement a per-process reference counter, and when the counter reaches zero, the service provider must prepare itself to be unloaded from memory. The first order of business is to finish transmitting any unsent data on sockets that are configured for a graceful close. Thereafter, any and all resources held by the provider are to be freed. The service provider must be left in a state where it can be immediately reinitialized by a call to **WSPStartup**.

 

 



