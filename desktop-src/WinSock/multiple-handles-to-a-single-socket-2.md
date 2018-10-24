---
Description: Since what are duplicated are the socket descriptors and not the underlying sockets, all of the states associated with a socket are held in common across all the descriptors.
ms.assetid: f3a2cd5a-bc3a-4aeb-8606-7b8aa6afb105
title: Multiple Handles to a Single Socket
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Handles to a Single Socket

Since what are duplicated are the socket descriptors and not the underlying sockets, all of the states associated with a socket are held in common across all the descriptors. For example a [**WSPSetSockOpt**](https://msdn.microsoft.com/en-us/library/ms742293(v=VS.85).aspx) operation performed using one descriptor is subsequently visible using a [**WSPGetSockOpt**](https://msdn.microsoft.com/en-us/library/ms742281(v=VS.85).aspx) from any or all descriptors.

Notification on shared sockets is subject to the usual constraints of [**WSPAsyncSelect**](https://msdn.microsoft.com/en-us/library/ms742267(v=VS.85).aspx) and [**WSPEventSelect**](https://msdn.microsoft.com/en-us/library/ms742276(v=VS.85).aspx). Issuing either of these calls using any of the shared descriptors cancels any previous event registration for the socket, regardless of which descriptor was used to make that registration. Thus, for example, it would not be possible to have process A receive FD\_READ events and process B receive FD\_WRITE events. For situations when such tight coordination is required, it is suggested that developers consider using threads instead of separate processes.

 

 



