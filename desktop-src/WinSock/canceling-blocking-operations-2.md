---
description: A thread may, at any time, call WSAIsBlocking to determine whether or not a blocking call is currently in progress.
ms.assetid: 6213ded4-feab-404f-86a0-3db9a0a42769
title: Canceling Blocking Operations
ms.topic: article
ms.date: 05/31/2018
---

# Canceling Blocking Operations

A thread may, at any time, call [WSAIsBlocking](/windows/desktop/api/winsock2/nf-winsock2-wsaisblocking) to determine whether or not a blocking call is currently in progress. (This function is implemented within the Windows Sockets 1.1 compatibility shims and hence has no SPI counterpart.) Clearly this is only possible when pseudo blocking, as opposed to true blocking, is being employed by the service provider. When necessary, [**WSPCancelBlockingCall**](/previous-versions/windows/desktop/legacy/ms742269(v=vs.85)) may be called at any time to cancel any current pseudo blocking operation.

 

 
