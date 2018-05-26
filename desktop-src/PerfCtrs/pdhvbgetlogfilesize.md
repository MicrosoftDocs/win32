---
Description: The PdhVbGetLogFileSize function returns the size of the specified log file. This function calls PdhGetLogFileSize.
ms.assetid: 8f4fbb68-b0f5-4163-ae6e-5b7139a35adf
title: PdhVbGetLogFileSize function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PdhVbGetLogFileSize function

The **PdhVbGetLogFileSize** function returns the size of the specified log file. This function calls [**PdhGetLogFileSize**](/windows/win32/Pdh/nf-pdh-pdhgetlogfilesize?branch=master).

Function PdhVbGetLogFileSize( \_ ByVal hLog As PDH\_HLOG, \_ ByRef llSize As LONG \_ ) As DWORD

## Parameters

<dl> <dt>

*hLog* \[in\]
</dt> <dd>

Handle to the log file. This handle is returned by the [**PdhOpenLog**](/windows/win32/Pdh/nf-pdh-pdhopenloga?branch=master) function.

</dd> <dt>

*llSize* \[out\]
</dt> <dd>

Pointer to a variable that receives the size of the log file, in bytes.

</dd> </dl>

## Return value

If the function succeeds, it returns 0.

If the function fails, the return value is a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381) or a [PDH error code](pdh-error-codes.md). The following are possible values.



| Return code                                                                                                | Description                                                                                            |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**PDH\_INSUFFICIENT\_BUFFER**</dt> </dl>   | The requested data is larger than the buffer supplied. Unable to return the requested data.<br/> |
| <dl> <dt>**PDH\_INVALID\_ARGUMENT**</dt> </dl>      | One or more of the string buffers is not the correct size.<br/>                                  |
| <dl> <dt>**PDH\_INVALID\_HANDLE**</dt> </dl>        | The handle is not a valid PDH object.<br/>                                                       |
| <dl> <dt>**PDH\_LOG\_FILE\_OPEN\_ERROR**</dt> </dl> | Unable to open the specified log file.<br/>                                                      |
| <dl> <dt>**PDH\_FILE\_NOT\_FOUND**</dt> </dl>       | Unable to find the specified file.<br/>                                                          |



 

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhGetLogFileSize**](/windows/win32/Pdh/nf-pdh-pdhgetlogfilesize?branch=master)
</dt> <dt>

[**PdhVbOpenLog**](pdhvbopenlog.md)
</dt> <dt>

[**PdhVbUpdateLog**](pdhvbupdatelog.md)
</dt> </dl>

 

 




