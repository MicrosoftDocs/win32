---
Description: The SPFILENOTIFY\_ENDCOPY notification is passed to the callback function when the queue completes a copy operation. This notification is sent even if the user cancels or if an error occurs.
ms.assetid: d58dc397-8803-466c-9069-728faf2c2030
title: SPFILENOTIFY\_ENDCOPY message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_ENDCOPY message

The **SPFILENOTIFY\_ENDCOPY** notification is passed to the callback function when the queue completes a copy operation. This notification is sent even if the user cancels or if an error occurs.


```C++
SPFILENOTIFY_ENDCOPY
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

 

 




