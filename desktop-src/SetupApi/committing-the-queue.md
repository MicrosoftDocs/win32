---
Description: 'If the default callback function is going to be called during the queue commitment, the context for it must be initialized using the SetupInitDefaultQueueCallback or SetupInitDefaultQueueCallbackEx functions.'
ms.assetid: 'e87f8a66-33e5-4065-98ce-2e904c115b38'
title: Committing the Queue
---

# Committing the Queue

If the default callback function is going to be called during the queue commitment, the context for it must be initialized using the [**SetupInitDefaultQueueCallback**](setupinitdefaultqueuecallback.md) or [**SetupInitDefaultQueueCallbackEx**](setupinitdefaultqueuecallbackex.md) functions. If you are using a custom callback function that never calls the default callback function, this step is not necessary.

After the queue is built and the callback function that will process queue notifications has been initialized, you can call [**SetupCommitFileQueue**](setupcommitfilequeue.md) to commit the operations that have been enqueued.

The following example uses [**SetupCommitFileQueue**](setupcommitfilequeue.md) to commit the queue using the default callback routine.

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

In the preceding example, MyQueue is the queue to commit, OwnerWindow is the window that will own any dialog boxes created by the default callback routine, SetupDefaultQueueCallback specifies that the default callback function will be used, and *Context* is a pointer to the structure returned by the previous call to [**SetupInitDefaultQueueCallback**](setupinitdefaultqueuecallback.md).

 

 



