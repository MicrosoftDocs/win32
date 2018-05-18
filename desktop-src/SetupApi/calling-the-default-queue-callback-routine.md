---
Description: 'If the default queue callback routine is initialized and specified when SetupCommitFileQueue is called, the queue calls the default queue callback routine internally and you need do nothing more.'
ms.assetid: 'a976c275-f128-490d-a544-efbfc6fd87f4'
title: Calling the Default Queue Callback Routine
---

# Calling the Default Queue Callback Routine

If the default queue callback routine is initialized and specified when [**SetupCommitFileQueue**](setupcommitfilequeue.md) is called, the queue calls the default queue callback routine internally and you need do nothing more.

If you create a filter callback routine that relies on the default queue callback routine to handle a subset of the queue notifications, your filter callback routine must call [**SetupDefaultQueueCallback**](setupdefaultqueuecallback.md) explicitly.

> \[!Important\]  
> When you call [**SetupDefaultQueueCallback**](setupdefaultqueuecallback.md) explicitly, you must pass in the void pointer returned by either [**SetupInitDefaultQueueCallback**](setupinitdefaultqueuecallback.md) or [**SetupInitDefaultQueueCallbackEx**](setupinitdefaultqueuecallbackex.md).

 

> [!Note]  
> One way to do this is to create a context structure for your custom callback routine that includes as one of its members the void pointer returned by [**SetupInitDefaultQueueCallback**](setupinitdefaultqueuecallback.md) or [**SetupInitDefaultQueueCallbackEx**](setupinitdefaultqueuecallbackex.md).

 

 

 



