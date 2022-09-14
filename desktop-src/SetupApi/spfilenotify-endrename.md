---
description: The SPFILENOTIFY\_ENDRENAME notification is sent to the callback routine when the queue completes a rename operation. This notification is sent even if the user cancels or if an error occurs.
ms.assetid: 8d5a8d17-de4f-4100-aa72-dfefeb8d4db9
title: SPFILENOTIFY_ENDRENAME message (Setupapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPFILENOTIFY\_ENDRENAME message

The **SPFILENOTIFY\_ENDRENAME** notification is sent to the callback routine when the queue completes a rename operation. This notification is sent even if the user cancels or if an error occurs.


```C++
SPFILENOTIFY_ENDRENAME
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/desktop/api/Setupapi/ns-setupapi-filepaths_a) structure. The **Win32Error** member of the **FILEPATHS** structure indicates the outcome of the copy operation.

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

[**FILEPATHS**](/windows/desktop/api/Setupapi/ns-setupapi-filepaths_a)
</dt> <dt>

[**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea)
</dt> <dt>

[**SetupDefaultQueueCallback**](/windows/desktop/api/Setupapi/nf-setupapi-setupdefaultqueuecallbacka)
</dt> </dl>

 

 




