---
Description: The SPFILENOTIFY\_QUEUESCAN notification is sent to a callback routine by SetupScanFileQueue for each node in the copy subqueue of the file queue. This only occurs if the SetupScanFileQueue function was called specifying the flag SPQ\_SCAN\_USE\_CALLBACK.
ms.assetid: 8aacc6c0-b6fe-4b4a-bbe4-a0351baf1f30
title: SPFILENOTIFY\_QUEUESCAN message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_QUEUESCAN message

The **SPFILENOTIFY\_QUEUESCAN** notification is sent to a callback routine by [**SetupScanFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupscanfilequeuea?branch=master) for each node in the copy subqueue of the file queue. This only occurs if the **SetupScanFileQueue** function was called specifying the flag SPQ\_SCAN\_USE\_CALLBACK.


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

The callback routine should return a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381).

If the callback routine returns NO\_ERROR, the queue scan continues. If the routine returns any other error code, the queue scan aborts and [**SetupScanFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupscanfilequeuea?branch=master) returns **FALSE**.

> [!Note]  
> This notification is not handled by the [**SetupDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupdefaultqueuecallbacka?branch=master) function.

 

## Requirements



|                                     |                                                                                       |
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

[**SetupScanFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupscanfilequeuea?branch=master)
</dt> </dl>

 

 




