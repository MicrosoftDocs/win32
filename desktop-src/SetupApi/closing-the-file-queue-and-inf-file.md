---
Description: After the queue has finished committing its operations, it should be closed using the SetupCloseFileQueue function with the handle that was created by SetupOpenFileQueue.
ms.assetid: 4cb21699-e476-4832-9678-2bf36f3bda08
title: Closing the File Queue and INF File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Closing the File Queue and INF File

After the queue has finished committing its operations, it should be closed using the [**SetupCloseFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupclosefilequeue?branch=master) function with the handle that was created by [**SetupOpenFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupopenfilequeue?branch=master). The default queue callback must be destroyed and recreated before another queue can be committed.

If a default context was initiated for use by the default callback routine, it should also be terminated by calling the [**SetupTermDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setuptermdefaultqueuecallback?branch=master) function. The *Context* is a pointer to the structure returned by the [**SetupInitDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallback?branch=master) function.

When access to the INF information is no longer needed, call the [**SetupCloseInfFile**](/windows/win32/Setupapi/nf-setupapi-setupcloseinffile?branch=master) function with the handle that was created by [**SetupOpenFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupopenfilequeue?branch=master) to free system resources.

 

 



