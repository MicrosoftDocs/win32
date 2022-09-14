---
description: Introducing overlapped I/O requires a mechanism for applications to unambiguously associate send and receive requests with their subsequent completion indications.
ms.assetid: '944d87bd-388f-420d-ac7d-69c4a28f8a5c'
title: Event Objects (Windows Sockets 2)
ms.topic: article
ms.date: 05/31/2018
---

# Event Objects (Windows Sockets 2)

Introducing overlapped I/O requires a mechanism for applications to unambiguously associate send and receive requests with their subsequent completion indications. In Windows Sockets 2, this is accomplished with event objects that are modeled after Windows events. Windows Sockets event objects are fairly simple constructs that can be created and closed, set and cleared, and waited upon and polled. Their prime utility is the ability of an application to block and wait until one or more event objects become set.

Applications use [**WSACreateEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacreateevent) to obtain an event object handle that can then be supplied as a required parameter to the overlapped versions of send and receive calls ( [**WSASend**](/windows/desktop/api/Winsock2/nf-winsock2-wsasend), [**WSASendTo**](/windows/desktop/api/Winsock2/nf-winsock2-wsasendto), [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv), [**WSARecvFrom**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecvfrom)). The event object, which is cleared when first created, is set by the transport providers when the associated overlapped I/O operation has completed (either successfully or with errors). Each event object created by **WSACreateEvent** should have a matching [**WSACloseEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacloseevent) to destroy it.

Event objects are also used in [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) to associate one or more FD\_XXX network events with an event object. This is described in [Asynchronous Notification Using Event Objects](asynchronous-notification-using-event-objects-2.md).

In 32-bit environments, event object–related functions, including [**WSACreateEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacreateevent), [**WSACloseEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacloseevent), [**WSASetEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsasetevent), [**WSAResetEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsaresetevent), and [**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents) are directly mapped to the corresponding native Windows functions, using the same function name, but without the WSA prefix.

 

 



