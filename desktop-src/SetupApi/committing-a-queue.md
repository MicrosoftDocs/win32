---
description: After all the desired file operations have been queued, the queue must be committed. This causes the enqueued file operations to be processed.
ms.assetid: 536f47f5-785e-4a83-a500-c769442e3e68
title: Committing a Queue
ms.topic: article
ms.date: 05/31/2018
---

# Committing a Queue

After all the desired file operations have been queued, the queue must be committed. This causes the enqueued file operations to be processed.

A file queue cannot be reused after it has been committed. The best practice is to collect all the required file operations for the file queue and commit the queue only once. If additional processing of the queue is required after it has been committed, the handle to the queue should be closed and a new file queue created. To commit the file queue, call the [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) function, specifying a callback routine. The callback routine will receive notifications from **SetupCommitFileQueue** as the file operations are processed. If you want to use the default queue callback routine, you must first initialize the necessary context by calling either [**SetupInitDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallback) or [**SetupInitDefaultQueueCallbackEx**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex). For more information about the default queue callback routine, see [Default Queue Callback Routine](default-queue-callback-routine.md).

> [!Note]  
> [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) should be called before the queue is closed. Any operations that are uncommitted when [**SetupCloseFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupclosefilequeue) is called will not be performed.

 

 

 



