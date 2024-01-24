---
description: After the queue has finished committing its operations, it should be closed using the SetupCloseFileQueue function with the handle that was created by SetupOpenFileQueue.
ms.assetid: 4cb21699-e476-4832-9678-2bf36f3bda08
title: Closing the File Queue and INF File
ms.topic: article
ms.date: 05/31/2018
---

# Closing the File Queue and INF File

After the queue has finished committing its operations, it should be closed using the [**SetupCloseFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupclosefilequeue) function with the handle that was created by [**SetupOpenFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenfilequeue). The default queue callback must be destroyed and recreated before another queue can be committed.

If a default context was initiated for use by the default callback routine, it should also be terminated by calling the [**SetupTermDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setuptermdefaultqueuecallback) function. The *Context* is a pointer to the structure returned by the [**SetupInitDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallback) function.

When access to the INF information is no longer needed, call the [**SetupCloseInfFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupcloseinffile) function with the handle that was created by [**SetupOpenFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenfilequeue) to free system resources.

 

 



