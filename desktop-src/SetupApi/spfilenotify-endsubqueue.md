---
description: The SPFILENOTIFY\_ENDSUBQUEUE notification is sent to the callback function when the queue completes all the operations in the delete, rename, or copy subqueue.
ms.assetid: 76bd027a-0f00-46e3-b502-0c97827308a8
title: SPFILENOTIFY_ENDSUBQUEUE message (Setupapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPFILENOTIFY\_ENDSUBQUEUE message

The **SPFILENOTIFY\_ENDSUBQUEUE** notification is sent to the callback function when the queue completes all the operations in the delete, rename, or copy subqueue.


```C++
SPFILENOTIFY_ENDSUBQUEUE
  Param1 = (UINT) SubQueue;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Subqueue that has been completed. This parameter can be one of the following values FILEOP\_DELETE, FILEOP\_RENAME, or FILEOP\_COPY.

</dd> <dt>

*Param2* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

The return value is ignored.

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

[**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea)
</dt> <dt>

[**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka)
</dt> </dl>

 

 




