---
Description: The WSADuplicateSocket function is introduced to enable socket sharing across processes.
ms.assetid: f7cf40e9-f3a6-4b62-8a78-df25464e2365
title: Shared Sockets
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shared Sockets

The [**WSADuplicateSocket**](/windows/win32/Winsock2/nf-winsock2-wsaduplicatesocketa?branch=master) function is introduced to enable socket sharing across processes. A source process calls **WSADuplicateSocket** to obtain a special [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure for a target process identifier. It uses some interprocess communications (IPC) mechanism to pass the contents of this structure to a target process. The target process then uses the **WSAPROTOCOL\_INFO** structure in a call to [**WSPSocket**](/windows/win32/Ws2spi/nc-ws2spi-lpwspsocket?branch=master). The socket descriptor returned by this function will be an additional socket descriptor to an underlying socket which thus becomes shared. Sockets can be shared among threads in a given process without using the **WSADuplicateSocket** function because a socket descriptor is valid in all threads of a process.

The two (or more) descriptors that reference a shared socket can be used independently as far as I/O is concerned. However, the Winsock interface does not implement any type of access control, so the processes must coordinate any operations on a shared socket. A typical example of sharing sockets is to use one process for creating sockets and establishing connections. This process then hands off sockets to other processes that are responsible for information exchange.

The [**WSADuplicateSocket**](/windows/win32/Winsock2/nf-winsock2-wsaduplicatesocketa?branch=master) function creates socket descriptors and not the underlying socket. As a result, all the states associated with a socket are held in common across all the descriptors. For example, a [**setsockopt**](/windows/win32/winsock/nf-winsock-setsockopt?branch=master) operation performed using one descriptor is subsequently visible using a [**getsockopt**](/windows/win32/winsock/nf-winsock-getsockopt?branch=master) from any or all descriptors. A process can call [**closesocket**](/windows/win32/winsock/nf-winsock-closesocket?branch=master) on a duplicated socket and the descriptor will become deallocated. The underlying socket, however, remains open until **closesocket** is called with the last remaining descriptor.

Notification on shared sockets is subject to the usual constraints of the [**WSAAsyncSelect**](/windows/win32/winsock/nf-winsock-wsaasyncselect?branch=master) and [**WSAEventSelect**](/windows/win32/Winsock2/nf-winsock2-wsaeventselect?branch=master) functions. Issuing either of these calls using any of the shared descriptors cancels any previous event registration for the socket, regardless of which descriptor was used to make that registration. Thus, for example, it would not be possible to have process A receive FD\_READ events and process B receive FD\_WRITE events. For situations when such tight coordination is required, it is suggested that developers use threads instead of separate processes.

 

 



