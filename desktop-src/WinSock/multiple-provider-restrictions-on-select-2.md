---
Description: The select function is used to determine the status of one or more sockets in a set. For each socket, the caller can request information on read, write, or error status. A set of sockets is indicated by an FD\_SET structure.
ms.assetid: 40354d8f-1e8b-48aa-888a-81a421568f23
title: Multiple Provider Restrictions on Select
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multiple Provider Restrictions on Select

The [**select**](/windows/win32/Winsock2/nf-winsock2-select?branch=master) function is used to determine the status of one or more sockets in a set. For each socket, the caller can request information on read, write, or error status. A set of sockets is indicated by an [**FD\_SET**](/windows/win32/winsock/nf-winsock-fd_set?branch=master) structure.

Windows Sockets 2 allows an application to use more than one service provider, but the [**select**](/windows/win32/Winsock2/nf-winsock2-select?branch=master) function is limited to a set of sockets associated with a single service provider. This does not in any way restrict an application from having multiple sockets open through multiple providers.

There are two ways to determine the status of a set of sockets that spans more than one service provider:

-   Using the [**WSAWaitForMultipleEvents**](/windows/win32/Winsock2/nf-winsock2-wsawaitformultipleevents?branch=master) or [**WSAEventSelect**](/windows/win32/Winsock2/nf-winsock2-wsaeventselect?branch=master) functions when blocking semantics are employed.
-   Using the [**WSAAsyncSelect**](/windows/win32/winsock/nf-winsock-wsaasyncselect?branch=master) function when nonblocking operations are employed and the application is already using a Windows message pump.

When an application needs to use blocking semantics on a set of sockets that spans multiple providers, [**WSAWaitForMultipleEvents**](/windows/win32/Winsock2/nf-winsock2-wsawaitformultipleevents?branch=master) is recommended. The application can also use the [**WSAEventSelect**](/windows/win32/Winsock2/nf-winsock2-wsaeventselect?branch=master) function, which allows the FD\_XXX network events (see [**WSAEventSelect**](/windows/win32/Winsock2/nf-winsock2-wsaeventselect?branch=master)) to associate with an event object and be handled from within the event object paradigm (described in [Overlapped I/O and Event Objects](overlapped-i-o-and-event-objects-2.md)).

The [**WSAAsyncSelect**](/windows/win32/winsock/nf-winsock-wsaasyncselect?branch=master) function is not restricted to a single provider because it takes a single socket descriptor as an input parameter. Note however, that [**WSAEventSelect**](/windows/win32/Winsock2/nf-winsock2-wsaeventselect?branch=master) function offers better performance and scalability over **WSAAsyncSelect** as the overhead of maintaining the message pump with Winsock event messages increases as the total number of sockets being used increases.

 

 



