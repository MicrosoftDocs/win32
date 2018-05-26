---
Description: Introducing overlapped I/O requires a mechanism for applications to unambiguously associate send and receive requests with their subsequent completion indications.
ms.assetid: 4254937c-7ee6-49a3-9f30-09aebaf2265b
title: Event Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Event Objects

Introducing overlapped I/O requires a mechanism for applications to unambiguously associate send and receive requests with their subsequent completion indications. In Windows Sockets 2, this is accomplished with event objects that are modeled after Windows events. Windows Sockets event objects are fairly simple constructs that can be created and closed, set and cleared, and waited upon and polled. Their prime utility is the ability of an application to block and wait until one or more event objects become set.

Applications use [**WSACreateEvent**](/windows/win32/Winsock2/nf-winsock2-wsacreateevent?branch=master) to obtain an event object handle that can then be supplied as a required parameter to the overlapped versions of send and receive calls ( [**WSASend**](/windows/win32/Winsock2/nf-winsock2-wsasend?branch=master), [**WSASendTo**](/windows/win32/Winsock2/nf-winsock2-wsasendto?branch=master), [**WSARecv**](/windows/win32/Winsock2/nf-winsock2-wsarecv?branch=master), [**WSARecvFrom**](/windows/win32/Winsock2/nf-winsock2-wsarecvfrom?branch=master)). The event object, which is cleared when first created, is set by the transport providers when the associated overlapped I/O operation has completed (either successfully or with errors). Each event object created by **WSACreateEvent** should have a matching [**WSACloseEvent**](/windows/win32/Winsock2/nf-winsock2-wsacloseevent?branch=master) to destroy it.

Event objects are also used in [**WSAEventSelect**](/windows/win32/Winsock2/nf-winsock2-wsaeventselect?branch=master) to associate one or more FD\_XXX network events with an event object. This is described in [Asynchronous Notification Using Event Objects](asynchronous-notification-using-event-objects-2.md).

In 32-bit environments, event object–related functions, including [**WSACreateEvent**](/windows/win32/Winsock2/nf-winsock2-wsacreateevent?branch=master), [**WSACloseEvent**](/windows/win32/Winsock2/nf-winsock2-wsacloseevent?branch=master), [**WSASetEvent**](/windows/win32/Winsock2/nf-winsock2-wsasetevent?branch=master), [**WSAResetEvent**](/windows/win32/Winsock2/nf-winsock2-wsaresetevent?branch=master), and [**WSAWaitForMultipleEvents**](/windows/win32/Winsock2/nf-winsock2-wsawaitformultipleevents?branch=master) are directly mapped to the corresponding native Windows functions, using the same function name, but without the WSA prefix.

 

 



