---
Description: The SPFILENOTIFY\_ENDRENAME notification is sent to the callback routine when the queue completes a rename operation. This notification is sent even if the user cancels or if an error occurs.
ms.assetid: 8d5a8d17-de4f-4100-aa72-dfefeb8d4db9
title: SPFILENOTIFY\_ENDRENAME message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Pointer to a [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure. The **Win32Error** member of the **FILEPATHS** structure indicates the outcome of the copy operation.

</dd> <dt>

*Param2* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

The return value is ignored.

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

[**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master)
</dt> <dt>

[**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master)
</dt> <dt>

[**SetupDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupdefaultqueuecallbacka?branch=master)
</dt> </dl>

 

 




