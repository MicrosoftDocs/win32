---
Description: 'The SPFILENOTIFY\_ENDRENAME notification is sent to the callback routine when the queue completes a rename operation. This notification is sent even if the user cancels or if an error occurs.'
ms.assetid: '8d5a8d17-de4f-4100-aa72-dfefeb8d4db9'
title: 'SPFILENOTIFY\_ENDRENAME message'
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

Pointer to a [**FILEPATHS**](filepaths-str.md) structure. The **Win32Error** member of the **FILEPATHS** structure indicates the outcome of the copy operation.

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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Setupapi.h</dt> </dl> |



## See also

<dl> <dt>

[Overview](overview.md)
</dt> <dt>

[Notifications](notifications.md)
</dt> <dt>

[**FILEPATHS**](filepaths-str.md)
</dt> <dt>

[**SetupCommitFileQueue**](setupcommitfilequeue.md)
</dt> <dt>

[**SetupDefaultQueueCallback**](setupdefaultqueuecallback.md)
</dt> </dl>

 

 




