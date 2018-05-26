---
Description: The SPFILENOTIFY\_RENAMEERROR notification is sent to the callback routine if an error occurs during a file rename operation.
ms.assetid: b7016cbe-2987-477f-958b-52b7a31c54c2
title: SPFILENOTIFY\_RENAMEERROR message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_RENAMEERROR message

The **SPFILENOTIFY\_RENAMEERROR** notification is sent to the callback routine if an error occurs during a file rename operation.


```C++
SPFILENOTIFY_RENAMEERROR
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure. The **Win32Error** member of the **FILEPATHS** structure specifies the error that occurred during the rename operation.

</dd> <dt>

*Param2* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

The callback routine should return one of the following.



| Return code                                                                                  | Description                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**FILEOP\_RETRY**</dt> </dl> | The user chose to attempt the rename operation again.<br/>                                                                                                                                                                                                  |
| <dl> <dt>**FILEOP\_SKIP**</dt> </dl>  | The user chose to skip the file rename operation.<br/>                                                                                                                                                                                                      |
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl> | Stop the queue commit. [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) returns **FALSE**. [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns extended error information such as ERROR\_CANCELLED (if the user canceled) or ERROR\_NOT\_ENOUGH\_MEMORY.<br/> |



 

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

 

 




