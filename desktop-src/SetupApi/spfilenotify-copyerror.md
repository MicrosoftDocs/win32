---
Description: 'The SPFILENOTIFY\_COPYERROR notification is sent to the callback routine if an error occurs during a file copy operation.'
ms.assetid: 'd6096954-c6a5-44d4-a358-c1320c50730a'
title: 'SPFILENOTIFY\_COPYERROR message'
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

Pointer to a [**FILEPATHS**](filepaths-str.md) structure.

</dd> <dt>

*Param2* 
</dt> <dd>

Pointer to a buffer, of size MAX\_PATH characters, that stores new path information specified by the user.

</dd> </dl>

## Return value

The callback should return one of the following values.



| Return code                                                                                    | Description                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**FILEOP\_ABORT**</dt> </dl>   | Queue processing should be canceled. [**SetupCommitFileQueue**](setupcommitfilequeue.md) returns zero and [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns extended error information such as ERROR\_CANCELLED (if the user canceled) or ERROR\_NOT\_ENOUGH\_MEMORY.<br/> |
| <dl> <dt>**FILEOP\_NEWPATH**</dt> </dl> | Retry the copy operation using the path the callback function placed in the buffer pointed to by the *Param2* parameter. The callback routine should ensure that the path does not overflow the buffer size of a TCHAR array of MAX\_PATH elements.<br/>                |
| <dl> <dt>**FILEOP\_RETRY**</dt> </dl>   | The user is attempting the copy operation again.<br/>                                                                                                                                                                                                                   |
| <dl> <dt>**FILEOP\_SKIP**</dt> </dl>    | The user is skipping the file copy operation.<br/>                                                                                                                                                                                                                      |



 

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

 

 




