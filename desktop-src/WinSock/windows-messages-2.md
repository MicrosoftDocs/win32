---
Description: Windows Sockets 1.1 introduced the async-select mechanism to provide network event indications that did not involve either polling or blocking.
ms.assetid: d536f796-c532-4b57-8dc7-3415661b736b
title: Windows Messages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Messages

Windows Sockets 1.1 introduced the async-select mechanism to provide network event indications that did not involve either polling or blocking. The [**WSPAsyncSelect**](/windows/win32/Ws2spi/?branch=master) function is used to register an interest in one or more network events as listed in the preceding, and supply a window handle to be used for notification. When a nominated network event occurs, a client-specified Windows message is sent to the indicated window. The service provider must use the [**WPUPostMessage**](/windows/win32/Ws2spi/nf-ws2spi-wpupostmessage?branch=master) function to accomplish this.

In Windows, this may not be the most efficient notification mechanism, and is inconvenient for daemons and services that do not want to open any windows. The event object signaling mechanism described in the following is introduced to solve this problem.

 

 



