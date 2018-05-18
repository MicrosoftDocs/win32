---
Description: 'The SPFILENOTIFY\_ENDCOPY notification is passed to the callback function when the queue completes a copy operation. This notification is sent even if the user cancels or if an error occurs.'
ms.assetid: 'd58dc397-8803-466c-9069-728faf2c2030'
title: 'SPFILENOTIFY\_ENDCOPY message'
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

Pointer to a [**FILEPATHS**](filepaths-str.md) structure. The **Win32Error** member of the **FILEPATHS** structure indicates the outcome of the copy operation.

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

 

 




