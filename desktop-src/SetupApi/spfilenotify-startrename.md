---
Description: The SPFILENOTIFY\_STARTRENAME notification is sent to the callback function when the queue starts a file rename operation.
ms.assetid: 005c1840-6aa9-4e94-bfe7-6a9d53735fd9
title: SPFILENOTIFY\_STARTRENAME message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_STARTRENAME message

The **SPFILENOTIFY\_STARTRENAME** notification is sent to the callback function when the queue starts a file rename operation.


```C++
SPFILENOTIFY_STARTRENAME
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) Operation;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure.

</dd> <dt>

*Param2* 
</dt> <dd>

Always has the value FILEOP\_RENAME.

</dd> </dl>

## Return value

The callback routine should return one of the following values.



| Return code                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl> | Abort the queue commit. The callback routine should call [**SetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms680627) to indicate the reason for termination. [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) returns **FALSE** and a subsequent call to [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns the error code set by the callback routine during the call to **SetLastError**.<br/> |
| <dl> <dt>**FILEOP\_DOIT**</dt> </dl>  | Perform the file copy operation.<br/>                                                                                                                                                                                                                                                                                                                                     |
| <dl> <dt>**FILEOP\_SKIP**</dt> </dl>  | Skip the current copy operation.<br/>                                                                                                                                                                                                                                                                                                                                     |



 

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

 

 




