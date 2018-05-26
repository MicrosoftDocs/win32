---
Description: The WSARecv, WSARecvFrom, WSARecvMsg, WSASend, WSASendMsg, and WSASendTo functions all take an array of application buffers as input parameters and can be used for scatter/gather (or vectored) I/O.
ms.assetid: c42e6cea-3b40-44ad-8715-09ce57e82217
title: Scatter/Gather I/O
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Scatter/Gather I/O

The [**WSARecv**](/windows/win32/Winsock2/nf-winsock2-wsarecv?branch=master), [**WSARecvFrom**](/windows/win32/Winsock2/nf-winsock2-wsarecvfrom?branch=master), [**WSARecvMsg**](/windows/win32/Mswsock/nc-mswsock-lpfn_wsarecvmsg?branch=master), [**WSASend**](/windows/win32/Winsock2/nf-winsock2-wsasend?branch=master), [**WSASendMsg**](/windows/win32/winsock2/nf-winsock2-wsasendmsg?branch=master), and [**WSASendTo**](/windows/win32/Winsock2/nf-winsock2-wsasendto?branch=master) functions all take an array of application buffers as input parameters and can be used for scatter/gather (or vectored) I/O. This can be very useful in instances where portions of each message being transmitted consist of one or more fixed-length header components in addition to the message body. Such header components need not be concatenated by the application into a single contiguous buffer prior to sending. Likewise on receiving, the header components can be automatically split off into separate buffers, leaving the message body by itself.

When receiving into multiple buffers, completion occurs as data arrives from the network, regardless of whether all the supplied buffers are utilized.

 

 



