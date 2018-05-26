---
Description: If the default queue callback routine is initialized and specified when SetupCommitFileQueue is called, the queue calls the default queue callback routine internally and you need do nothing more.
ms.assetid: a976c275-f128-490d-a544-efbfc6fd87f4
title: Calling the Default Queue Callback Routine
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Calling the Default Queue Callback Routine

If the default queue callback routine is initialized and specified when [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) is called, the queue calls the default queue callback routine internally and you need do nothing more.

If you create a filter callback routine that relies on the default queue callback routine to handle a subset of the queue notifications, your filter callback routine must call [**SetupDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupdefaultqueuecallbacka?branch=master) explicitly.

> \[!Important\]  
> When you call [**SetupDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupdefaultqueuecallbacka?branch=master) explicitly, you must pass in the void pointer returned by either [**SetupInitDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallback?branch=master) or [**SetupInitDefaultQueueCallbackEx**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex?branch=master).

 

> [!Note]  
> One way to do this is to create a context structure for your custom callback routine that includes as one of its members the void pointer returned by [**SetupInitDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallback?branch=master) or [**SetupInitDefaultQueueCallbackEx**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex?branch=master).

 

 

 



