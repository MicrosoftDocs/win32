---
Description: The SPFILENOTIFY\_ENDDELETE notification is returned to the callback routine when a queue completes a delete operation. This notification is sent even if the user cancels or if an error occurs.
ms.assetid: 78859854-8411-4c51-9c3c-628315cf1c41
title: SPFILENOTIFY\_ENDDELETE message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_ENDDELETE message

The **SPFILENOTIFY\_ENDDELETE** notification is returned to the callback routine when a queue completes a delete operation. This notification is sent even if the user cancels or if an error occurs.


```C++
SPFILENOTIFY_ENDDELETE
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure. The **Win32Error** member of the **FILEPATHS** structure indicates the outcome of a copy operation.

</dd> <dt>

*Param2* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

The return code is ignored.

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

 

 




