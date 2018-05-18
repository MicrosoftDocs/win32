---
Description: 'The SPFILENOTIFY\_FILEEXTRACTED notification is sent to a callback routine by SetupIterateCabinet to indicate either that a file was extracted from the cabinet or that an extraction failed and cabinet processing has been canceled.'
ms.assetid: '70ffe06c-e72d-4bb8-a13c-e2946ff72fa6'
title: 'SPFILENOTIFY\_FILEEXTRACTED message'
---

# SPFILENOTIFY\_FILEEXTRACTED message

The **SPFILENOTIFY\_FILEEXTRACTED** notification is sent to a callback routine by [**SetupIterateCabinet**](setupiteratecabinet.md) to indicate either that a file was extracted from the cabinet or that an extraction failed and cabinet processing has been canceled.


```C++
SPFILENOTIFY_FILEEXTRACTED
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) 0;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](filepaths-str.md) structure that contains path information for the extracted file. The **SourceFile** member of the **FILEPATHS** structure contains the full source path of the cabinet. The **TargetFile** member supplies the full target path of the file to be installed on the system.

</dd> <dt>

*Param2* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

The cabinet callback routine should return one of the following values.



| Return code                                                                               | Description                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NO\_ERROR**</dt> </dl>  | No error was encountered, continue processing the cabinet.<br/>                                                                                                                                |
| <dl> <dt>**ERROR\_XXX**</dt> </dl> | An error of the specified type occurred. [**SetupIterateCabinet**](setupiteratecabinet.md) will return zero. [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) will return the specified error code.<br/> |



 

> [!Note]  
> There is no default cabinet callback routine supplied with the Setup API. Your setup application should supply a callback routine to handle the notifications sent by the [**SetupIterateCabinet**](setupiteratecabinet.md) function.

 

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

[**SetupIterateCabinet**](setupiteratecabinet.md)
</dt> </dl>

 

 




