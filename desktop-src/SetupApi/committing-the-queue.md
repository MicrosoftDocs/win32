---
Description: If the default callback function is going to be called during the queue commitment, the context for it must be initialized using the SetupInitDefaultQueueCallback or SetupInitDefaultQueueCallbackEx functions.
ms.assetid: e87f8a66-33e5-4065-98ce-2e904c115b38
title: Committing the Queue
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Committing the Queue

If the default callback function is going to be called during the queue commitment, the context for it must be initialized using the [**SetupInitDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallback?branch=master) or [**SetupInitDefaultQueueCallbackEx**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex?branch=master) functions. If you are using a custom callback function that never calls the default callback function, this step is not necessary.

After the queue is built and the callback function that will process queue notifications has been initialized, you can call [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) to commit the operations that have been enqueued.

The following example uses [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) to commit the queue using the default callback routine.

``` syntax
test = SetupCommitFileQueue (
     OwnerWindow,          //window that will own dialog boxes
                           //created by the callback routine
     MyQueue,              //the queue to commit
  
                           //use the default callback routine
     SetupDefaultQueueCallback,  
  
     Context               //context information that will be 
                           //  used by the callback routine
);
```

In the preceding example, MyQueue is the queue to commit, OwnerWindow is the window that will own any dialog boxes created by the default callback routine, SetupDefaultQueueCallback specifies that the default callback function will be used, and *Context* is a pointer to the structure returned by the previous call to [**SetupInitDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallback?branch=master).

 

 



