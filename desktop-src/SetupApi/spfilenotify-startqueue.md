---
Description: 'The SPFILENOTIFY\_STARTQUEUE notification is sent to the callback routine when the queue commitment process starts.'
ms.assetid: '682c2ce0-0c82-402c-a487-db5f2c377f3f'
title: 'SPFILENOTIFY\_STARTQUEUE message'
---

# SPFILENOTIFY\_STARTQUEUE message

The **SPFILENOTIFY\_STARTQUEUE** notification is sent to the callback routine when the queue commitment process starts.


```C++
SPFILENOTIFY_STARTQUEUE
  Param1 = (UINT) OwnerWindow;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Handle to the window that is to own the dialog boxes that the callback routine generates.

</dd> <dt>

*Param2* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

If an error occurs, the callback routine should call [**SetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms680627), specifying the error, and then return zero. The [**SetupCommitFileQueue**](setupcommitfilequeue.md) function will return **FALSE** and a subsequent call to [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) will return the error code set by the callback routine.

If no error occurs, the callback routine should return a nonzero value.

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

[**SetupCommitFileQueue**](setupcommitfilequeue.md)
</dt> <dt>

[**SetupDefaultQueueCallback**](setupdefaultqueuecallback.md)
</dt> </dl>

 

 




