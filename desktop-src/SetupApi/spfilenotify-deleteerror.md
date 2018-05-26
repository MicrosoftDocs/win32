---
Description: The SPFILENOTIFY\_DELETEERROR notification is sent to the callback routine if an error occurs during a file delete operation.
ms.assetid: b98b62f0-0b59-430e-966d-c1447026b696
title: SPFILENOTIFY\_DELETEERROR message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPFILENOTIFY\_DELETEERROR message

The **SPFILENOTIFY\_DELETEERROR** notification is sent to the callback routine if an error occurs during a file delete operation.


```C++
SPFILENOTIFY_DELETEERROR
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/win32/Setupapi/ns-setupapi-_filepaths_a?branch=master) structure.

</dd> <dt>

*Param2* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

The callback routine should return one of the following values.



| Return code                                                                                  | Description                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl> | Queue processing should be canceled. [**SetupCommitFileQueue**](/windows/win32/Setupapi/nf-setupapi-setupcommitfilequeuea?branch=master) returns zero and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns extended error information such as ERROR\_CANCELLED (if the user canceled) or ERROR\_NOT\_ENOUGH\_MEMORY.<br/> |
| <dl> <dt>**FILEOP\_RETRY**</dt> </dl> | The user is attempting the delete operation again.<br/>                                                                                                                                                                                                                 |
| <dl> <dt>**FILEOP\_SKIP**</dt> </dl>  | The user is skipping the file delete operation.<br/>                                                                                                                                                                                                                    |



 

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

 

 




