---
description: Opportunistic locks are requested by first opening a file with permissions and flags appropriate to the application opening the file. All files for which opportunistic locks will be requested must be opened for overlapped (asynchronous) operation.
ms.assetid: a55d38c6-46e3-48e6-9b5b-d4f4234d8c07
title: How to Request an Opportunistic Lock
ms.topic: article
ms.date: 05/31/2018
---

# How to Request an Opportunistic Lock

Client applications directly request opportunistic locks only when the lock is intended for a file on the local server. When accessing files on remote servers, it is the network redirector, and not the client application, that requests the opportunistic lock from the remote server.

Opportunistic locks are requested by first opening a file with permissions and flags appropriate to the application opening the file. All files for which opportunistic locks will be requested must be opened for overlapped (asynchronous) operation. After the files are opened for overlapped operation, use the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the appropriate control code to request an opportunistic lock. For a list of the opportunistic lock operations, see [Opportunistic Lock Operations](opportunistic-lock-operations.md).

Applications are notified that an opportunistic lock is broken by using the **hEvent** member of the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure associated with the file. Applications may also use functions such as [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) and [**HasOverlappedIoCompleted**](/windows/desktop/api/winbase/nf-winbase-hasoverlappediocompleted). The application is responsible for associating the correct file with the broken opportunistic lock.

For more information on notification, see [Synchronization](/windows/desktop/Sync/synchronization).

 

 
