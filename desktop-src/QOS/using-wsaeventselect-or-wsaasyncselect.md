---
title: Using WSAEventSelect or WSAAsyncSelect
description: Applications can register their interest in receiving FD\_QOS events by enabling asynchronous event notification with either the WSAAsyncSelect or WSAEventSelect function. Information about how to do so can be found in the Windows Sockets 2 documentation.
ms.assetid: 58868799-948c-4c9c-8835-ed845b84b1f7
keywords:
- Quality of Service QOS , tasks, using WSAEventSelect
- Quality of Service QOS , tasks, using WSAAsyncSelect
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using WSAEventSelect or WSAAsyncSelect

Applications can register their interest in receiving FD\_QOS events by enabling asynchronous event notification with either the [**WSAAsyncSelect**](https://msdn.microsoft.com/library/windows/desktop/ms741540) or [**WSAEventSelect**](https://msdn.microsoft.com/library/windows/desktop/ms741576) function. Information about how to do so can be found in the Windows Sockets 2 documentation.

When registered for event notification using this mechanism, and an event notification occurs, an application can look up the status code (by using the [**WSAEnumNetworkEvents**](https://msdn.microsoft.com/library/windows/desktop/ms741572) function, for example) and subsequently issue a WSAIoctl(SIO\_GET\_QOS) function call to retrieve the [**QOS**](/windows/win32/Winsock2/ns-winsock2-_qualityofservice?branch=master) structure associated with the event.

The associated [**QOS**](/windows/win32/Winsock2/ns-winsock2-_qualityofservice?branch=master) structure contains the current QOS parameters. Applications should inspect the QOS parameters to determine the extent of the changes associated with the event notification. There are a couple of issues to consider when working with FD\_QOS events in this manner:

-   You must issue the WSAIoctl(SIO\_GET\_QOS) to reenable the FD\_QOS event.
-   There may be multiple QOS status indications waiting for retrieval. Use the WSAIoctl(SIO\_GET\_QOS) function call in a loop until SOCKET\_ERROR is returned.

Applications can also register their interest in FD\_QOS events using overlapped WSAIoctl(SIO\_GET\_QOS), as explained in [Using Overlapped WSAIoctl(SIO\_GET\_QOS)](using-overlapped-wsaioctl-sio-get-qos-.md).

 

 




