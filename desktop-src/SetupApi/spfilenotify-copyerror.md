---
description: The SPFILENOTIFY\_COPYERROR notification is sent to the callback routine if an error occurs during a file copy operation.
ms.assetid: d6096954-c6a5-44d4-a358-c1320c50730a
title: SPFILENOTIFY_COPYERROR message (Setupapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SPFILENOTIFY\_COPYERROR message

The **SPFILENOTIFY\_COPYERROR** notification is sent to the callback routine if an error occurs during a file copy operation.


```C++
SPFILENOTIFY_COPYERROR
  Param1 = (UINT_PTR) FilePathInfo;
  Param2 = (UINT_PTR) ReturnBuffer;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](/windows/desktop/api/Setupapi/ns-setupapi-filepaths_a) structure.

</dd> <dt>

*Param2* 
</dt> <dd>

Pointer to a buffer, of size MAX\_PATH characters, that stores new path information specified by the user.

</dd> </dl>

## Return value

The callback should return one of the following values.



| Return code                                                                                    | Description                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl>   | Queue processing should be canceled. [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea) returns zero and [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns extended error information such as ERROR\_CANCELLED (if the user canceled) or ERROR\_NOT\_ENOUGH\_MEMORY.<br/> |
| <dl> <dt>**FILEOP\_NEWPATH**</dt> </dl> | Retry the copy operation using the path the callback function placed in the buffer pointed to by the *Param2* parameter. The callback routine should ensure that the path does not overflow the buffer size of a TCHAR array of MAX\_PATH elements.<br/>                |
| <dl> <dt>**FILEOP\_RETRY**</dt> </dl>   | The user is attempting the copy operation again.<br/>                                                                                                                                                                                                                   |
| <dl> <dt>**FILEOP\_SKIP**</dt> </dl>    | The user is skipping the file copy operation.<br/>                                                                                                                                                                                                                      |



 

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

 

