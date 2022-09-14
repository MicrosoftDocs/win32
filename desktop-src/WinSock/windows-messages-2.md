---
description: Windows Sockets 1.1 introduced the async-select mechanism to provide network event indications that did not involve either polling or blocking.
ms.assetid: d536f796-c532-4b57-8dc7-3415661b736b
title: Windows Messages
ms.topic: article
ms.date: 05/31/2018
---

# Windows Messages

Windows Sockets 1.1 introduced the async-select mechanism to provide network event indications that did not involve either polling or blocking. The [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85)) function is used to register an interest in one or more network events as listed in the preceding, and supply a window handle to be used for notification. When a nominated network event occurs, a client-specified Windows message is sent to the indicated window. The service provider must use the [**WPUPostMessage**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpupostmessage) function to accomplish this.

In Windows, this may not be the most efficient notification mechanism, and is inconvenient for daemons and services that do not want to open any windows. The event object signaling mechanism described in the following is introduced to solve this problem.

 

 
