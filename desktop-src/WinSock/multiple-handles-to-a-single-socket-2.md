---
description: Since what are duplicated are the socket descriptors and not the underlying sockets, all of the states associated with a socket are held in common across all the descriptors.
ms.assetid: f3a2cd5a-bc3a-4aeb-8606-7b8aa6afb105
title: Multiple Handles to a Single Socket
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Handles to a Single Socket

Since what are duplicated are the socket descriptors and not the underlying sockets, all of the states associated with a socket are held in common across all the descriptors. For example a [**WSPSetSockOpt**](/previous-versions/windows/hardware/network/ff566318(v=vs.85)) operation performed using one descriptor is subsequently visible using a [**WSPGetSockOpt**](/previous-versions/windows/hardware/network/ff566292(v=vs.85)) from any or all descriptors.

Notification on shared sockets is subject to the usual constraints of [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85)) and [**WSPEventSelect**](/previous-versions/windows/hardware/network/ff566287(v=vs.85)). Issuing either of these calls using any of the shared descriptors cancels any previous event registration for the socket, regardless of which descriptor was used to make that registration. Thus, for example, it would not be possible to have process A receive FD\_READ events and process B receive FD\_WRITE events. For situations when such tight coordination is required, it is suggested that developers consider using threads instead of separate processes.

 

 
