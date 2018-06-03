---
title: Listening for FD\_QOS Events
description: QOS status is provided through FD\_QOS events.
ms.assetid: 5e3a8cb1-e841-4050-8083-48838fdc6caf
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Listening for FD\_QOS Events

QOS status is provided through FD\_QOS events. Applications that either send or receive QOS-enabled data can listen for FD\_QOS events by either of the following mechanisms:

-   Register for FD\_QOS events using the [**WSAAsyncSelect**](https://msdn.microsoft.com/library/windows/desktop/ms741540) or [**WSAEventSelect**](https://msdn.microsoft.com/library/windows/desktop/ms741576) function.
-   Perform an overlapped WSAIoctl(SIO\_GET\_QOS) function call.

Each of these approaches is explained in the following sections.

 

 




