---
Description: 'After the queue has finished committing its operations, it should be closed using the SetupCloseFileQueue function with the handle that was created by SetupOpenFileQueue.'
ms.assetid: '4cb21699-e476-4832-9678-2bf36f3bda08'
title: Closing the File Queue and INF File
---

# Closing the File Queue and INF File

After the queue has finished committing its operations, it should be closed using the [**SetupCloseFileQueue**](setupclosefilequeue.md) function with the handle that was created by [**SetupOpenFileQueue**](setupopenfilequeue.md). The default queue callback must be destroyed and recreated before another queue can be committed.

If a default context was initiated for use by the default callback routine, it should also be terminated by calling the [**SetupTermDefaultQueueCallback**](setuptermdefaultqueuecallback.md) function. The *Context* is a pointer to the structure returned by the [**SetupInitDefaultQueueCallback**](setupinitdefaultqueuecallback.md) function.

When access to the INF information is no longer needed, call the [**SetupCloseInfFile**](setupcloseinffile.md) function with the handle that was created by [**SetupOpenFileQueue**](setupopenfilequeue.md) to free system resources.

 

 



