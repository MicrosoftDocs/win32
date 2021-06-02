---
description: The SPFILENOTIFY\_QUEUESCAN notification is sent to a callback routine by SetupScanFileQueue for each node in the copy subqueue of the file queue. This only occurs if the SetupScanFileQueue function was called specifying the flag SPQ\_SCAN\_USE\_CALLBACK.
ms.assetid: 8aacc6c0-b6fe-4b4a-bbe4-a0351baf1f30
title: SPFILENOTIFY_QUEUESCAN message (Setupapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPFILENOTIFY\_QUEUESCAN message

The **SPFILENOTIFY\_QUEUESCAN** notification is sent to a callback routine by [**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea) for each node in the copy subqueue of the file queue. This only occurs if the **SetupScanFileQueue** function was called specifying the flag SPQ\_SCAN\_USE\_CALLBACK.


```C++
SPFILENOTIFY_QUEUESCAN
  Param1 = (UINT) TargetPath;
  Param2 = (UINT) DelayFlag;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Null-terminated string that specifies the target path information for the file queued in the current node.

</dd> <dt>

*Param2* 
</dt> <dd>

If the file in the current node of the queue is in use, *Param2* takes the value SPQ\_DELAYED\_COPY. If the file is not in use, the value is zero.

</dd> </dl>

## Return value

The callback routine should return a [system error code](/windows/desktop/Debug/system-error-codes).

If the callback routine returns NO\_ERROR, the queue scan continues. If the routine returns any other error code, the queue scan aborts and [**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea) returns **FALSE**.

> [!Note]  
> This notification is not handled by the [**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka) function.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Setupapi.h</dt> </dl> |



## See also

<dl> <dt>

[Overview](overview.md)
</dt> <dt>

[Notifications](notifications.md)
</dt> <dt>

[**SetupScanFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupscanfilequeuea)
</dt> </dl>

 

