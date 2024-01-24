---
description: The PdhVbUpdateLog function function updates the current query and writes new data to the log file. This function calls PdhUpdateLog.
ms.assetid: a7a3ad18-2d61-448e-9764-ba363398e804
title: PdhVbUpdateLog function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbUpdateLog
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbUpdateLog function

The **PdhVbUpdateLog** function function updates the current query and writes new data to the log file. This function calls [**PdhUpdateLog**](/windows/desktop/api/Pdh/nf-pdh-pdhupdateloga).

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbUpdateLog( \_ ByVal hLog As PDH\_HLOG, \_ ByVal szUserString As LPCTSTR \_ )

## Parameters

<dl> <dt>

*hLog* \[in\]
</dt> <dd>

Handle to the log file to be updated. This handle is returned by the [**PdhVbOpenLog**](pdhvbopenlog.md) function.

</dd> <dt>

*szUserString* \[in\]
</dt> <dd>

Pointer to a string that specifies the data to be added to the log file. This is generally used for comments within the log file.

</dd> </dl>

## Return value

If the function succeeds, it returns 0.

If the function fails, the return value is a [system error code](/windows/desktop/Debug/system-error-codes) or a [PDH error code](pdh-error-codes.md). The following are possible values.



| Return code                                                                                                | Description                                                                                            |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**PDH\_INSUFFICIENT\_BUFFER**</dt> </dl>   | The requested data is larger than the buffer supplied. Unable to return the requested data.<br/> |
| <dl> <dt>**PDH\_INVALID\_ARGUMENT**</dt> </dl>      | One or more of the string buffers is not the correct size.<br/>                                  |
| <dl> <dt>**PDH\_INVALID\_HANDLE**</dt> </dl>        | The handle is not a valid PDH object.<br/>                                                       |
| <dl> <dt>**PDH\_LOG\_FILE\_OPEN\_ERROR**</dt> </dl> | Unable to open the specified log file.<br/>                                                      |
| <dl> <dt>**PDH\_FILE\_NOT\_FOUND**</dt> </dl>       | Unable to find the specified file.<br/>                                                          |



 

## Remarks

There must be a currently opened query, and the desired counters must be added to it before this function is called.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhUpdateLog**](/windows/desktop/api/Pdh/nf-pdh-pdhupdateloga)
</dt> <dt>

[**PdhVbGetLogFileSize**](pdhvbgetlogfilesize.md)
</dt> <dt>

[**PdhVbOpenLog**](pdhvbopenlog.md)
</dt> </dl>

 

