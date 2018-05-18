---
Description: 'Introducing overlapped I/O requires a mechanism for applications to unambiguously associate send and receive requests with their subsequent completion indications.'
ms.assetid: '4254937c-7ee6-49a3-9f30-09aebaf2265b'
title: Event Objects
---

# Event Objects

Introducing overlapped I/O requires a mechanism for applications to unambiguously associate send and receive requests with their subsequent completion indications. In Windows Sockets 2, this is accomplished with event objects that are modeled after Windows events. Windows Sockets event objects are fairly simple constructs that can be created and closed, set and cleared, and waited upon and polled. Their prime utility is the ability of an application to block and wait until one or more event objects become set.

Applications use [**WSACreateEvent**](wsacreateevent-2.md) to obtain an event object handle that can then be supplied as a required parameter to the overlapped versions of send and receive calls ( [**WSASend**](wsasend-2.md), [**WSASendTo**](wsasendto-2.md), [**WSARecv**](wsarecv-2.md), [**WSARecvFrom**](wsarecvfrom-2.md)). The event object, which is cleared when first created, is set by the transport providers when the associated overlapped I/O operation has completed (either successfully or with errors). Each event object created by **WSACreateEvent** should have a matching [**WSACloseEvent**](wsacloseevent-2.md) to destroy it.

Event objects are also used in [**WSAEventSelect**](wsaeventselect-2.md) to associate one or more FD\_XXX network events with an event object. This is described in [Asynchronous Notification Using Event Objects](asynchronous-notification-using-event-objects-2.md).

In 32-bit environments, event object–related functions, including [**WSACreateEvent**](wsacreateevent-2.md), [**WSACloseEvent**](wsacloseevent-2.md), [**WSASetEvent**](wsasetevent-2.md), [**WSAResetEvent**](wsaresetevent-2.md), and [**WSAWaitForMultipleEvents**](wsawaitformultipleevents-2.md) are directly mapped to the corresponding native Windows functions, using the same function name, but without the WSA prefix.

 

 



