---
description: The PdhVbOpenQuery function creates and initializes a unique query structure that is used to manage the collection of performance data.
ms.assetid: 9cf535ef-76ad-4773-8414-8e289f3c52f6
title: PdhVbOpenQuery function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbOpenQuery
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbOpenQuery function

The **PdhVbOpenQuery** function creates and initializes a unique query structure that is used to manage the collection of performance data.

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbOpenQuery( \_ ByVal QueryHandle As Long \_ ) As Long

## Parameters

<dl> <dt>

*QueryHandle* 
</dt> <dd>

Variable that is cleared (equals 0) before the function is called and, if the function is successful, contains the unique ID of the query that is created and opened. This handle is used in the subsequent calls to other PDH functions to identify the query.

</dd> </dl>

## Return value

If the function succeeds, it returns a **Long** integer equal to ERROR\_SUCCESS and a new handle in the *QueryHandle* variable.

If the function fails, the return value is a [system error code](/windows/desktop/Debug/system-error-codes) or a [PDH error code](pdh-error-codes.md). The following are possible values.



| Return code                                                                                                     | Description                                                  |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**PDH\_INVALID\_ARGUMENT**</dt> </dl>           | The argument is invalid or incorrect.<br/>             |
| <dl> <dt>**PDH\_MEMORY\_ALLOCATION\_FAILURE**</dt> </dl> | A temporary memory buffer could not be allocated.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhCloseQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhclosequery)
</dt> </dl>

 

