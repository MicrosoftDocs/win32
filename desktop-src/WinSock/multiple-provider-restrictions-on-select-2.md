---
description: The select function is used to determine the status of one or more sockets in a set. For each socket, the caller can request information on read, write, or error status. A set of sockets is indicated by an FD\_SET structure.
ms.assetid: 40354d8f-1e8b-48aa-888a-81a421568f23
title: Multiple Provider Restrictions on Select
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Provider Restrictions on Select

The [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) function is used to determine the status of one or more sockets in a set. For each socket, the caller can request information on read, write, or error status. A set of sockets is indicated by an [**FD\_SET**](/windows/desktop/api/winsock/nf-winsock-fd_set) structure.

Windows Sockets 2 allows an application to use more than one service provider, but the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) function is limited to a set of sockets associated with a single service provider. This does not in any way restrict an application from having multiple sockets open through multiple providers.

There are two ways to determine the status of a set of sockets that spans more than one service provider:

-   Using the [**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents) or [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) functions when blocking semantics are employed.
-   Using the [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) function when nonblocking operations are employed and the application is already using a Windows message pump.

When an application needs to use blocking semantics on a set of sockets that spans multiple providers, [**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents) is recommended. The application can also use the [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) function, which allows the FD\_XXX network events (see [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect)) to associate with an event object and be handled from within the event object paradigm (described in [Overlapped I/O and Event Objects](overlapped-i-o-and-event-objects-2.md)).

The [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) function is not restricted to a single provider because it takes a single socket descriptor as an input parameter. Note however, that [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) function offers better performance and scalability over **WSAAsyncSelect** as the overhead of maintaining the message pump with Winsock event messages increases as the total number of sockets being used increases.

 

 



