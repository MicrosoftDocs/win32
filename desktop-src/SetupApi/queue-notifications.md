---
description: After a queue is committed by calling SetupCommitFileQueue, it will begin to process the queued operations. At each step, the queue sends a notification to the callback routine specified in the call to SetupCommitFileQueue.
ms.assetid: '866e1066-b6e0-43d3-8af4-bd37fbc024e2'
title: Queue Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Queue Notifications

After a queue is committed by calling [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea), it will begin to process the queued operations. At each step, the queue sends a notification to the callback routine specified in the call to **SetupCommitFileQueue**.

Following is the syntax that [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) uses to send a notification to the callback routine.

``` syntax
MsgHandler(          //the specified callback routine
    Context,         //context used by the callback routine
    Notification,    //queue notification code
    Param1,          //additional notification information
    Param2               //additional notification information
);
```

The values of *Param1* and *Param2* contain additional information relevant to the notification being sent to the callback routine. Each notification, its *Param1* and *Param2* values, and how the default queue callback routine handles that notification, is described in detail in [File Queue Notifications](file-queue-notifications.md).

 

 



