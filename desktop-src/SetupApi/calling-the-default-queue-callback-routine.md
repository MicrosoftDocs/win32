---
description: If the default queue callback routine is initialized and specified when SetupCommitFileQueue is called, the queue calls the default queue callback routine internally and you need do nothing more.
ms.assetid: a976c275-f128-490d-a544-efbfc6fd87f4
title: Calling the Default Queue Callback Routine
ms.topic: article
ms.date: 05/31/2018
---

# Calling the Default Queue Callback Routine

If the default queue callback routine is initialized and specified when [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) is called, the queue calls the default queue callback routine internally and you need do nothing more.

If you create a filter callback routine that relies on the default queue callback routine to handle a subset of the queue notifications, your filter callback routine must call [**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka) explicitly.

> [!IMPORTANT]
> When you call [**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka) explicitly, you must pass in the void pointer returned by either [**SetupInitDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallback) or [**SetupInitDefaultQueueCallbackEx**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex).

 

> [!Note]  
> One way to do this is to create a context structure for your custom callback routine that includes as one of its members the void pointer returned by [**SetupInitDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallback) or [**SetupInitDefaultQueueCallbackEx**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex).

 

 

 



