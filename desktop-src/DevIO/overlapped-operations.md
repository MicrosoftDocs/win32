---
description: Overlapped operations enable a thread to perform a time-consuming I/O operation in the background, leaving the thread free to perform other tasks.
ms.assetid: 8c0eb20d-685a-4750-8253-a87089b68509
title: Overlapped Operations
ms.topic: article
ms.date: 05/31/2018
---

# Overlapped Operations

Overlapped operations enable a thread to perform a time-consuming I/O operation in the background, leaving the thread free to perform other tasks. To enable overlapped I/O operations on a communications resource, the thread must specify the **FILE\_FLAG\_OVERLAPPED** flag in the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function when the handle is opened. To run the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) or [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) function as an overlapped operation, the calling thread must specify a pointer to an [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure. The **OVERLAPPED** structure must contain a handle to a manual-reset (not an auto-reset) event object. The system sets the state of the event object to not-signaled when a call to the I/O function returns before the operation has been completed. The system sets the state of the event object to signaled when the operation has been completed. The thread uses a wait function to check the current state of the event object or to wait for its state to be signaled.

The [**ReadFileEx**](/windows/desktop/api/fileapi/nf-fileapi-readfileex) and [**WriteFileEx**](/windows/desktop/api/fileapi/nf-fileapi-writefileex) functions can be performed only as overlapped operations. The calling thread specifies a pointer to the [**FileIOCompletionRoutine**](/windows/desktop/api/minwinbase/nc-minwinbase-lpoverlapped_completion_routine) function, which is performed when the overlapped operation is completed. The completion routine is executed only if the calling thread performs an alertable operation.

For more information about event objects, wait functions, alertable waits, and completion routines, see [About Synchronization](/windows/desktop/Sync/about-synchronization).

 

 
