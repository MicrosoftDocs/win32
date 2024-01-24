---
description: The PdhVbAddCounter function creates a counter entry in the specified query object, and returns a handle to that counter upon successful completion.
ms.assetid: 20a9e6cd-bf0d-497d-b660-88e786e2f004
title: PdhVbAddCounter function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbAddCounter
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbAddCounter function

The **PdhVbAddCounter** function creates a counter entry in the specified query object, and returns a handle to that counter upon successful completion.

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbAddCounter( \_ ByVal QueryHandle As Long, \_ ByVal CounterPath As String, \_ ByVal CounterHandle As Long \_ ) As Long

## Parameters

<dl> <dt>

*QueryHandle* 
</dt> <dd>

ID of the query to which this counter is to be assigned. This value is returned by the [**PdhVbOpenQuery**](pdhvbopenquery.md) function.

</dd> <dt>

*CounterPath* 
</dt> <dd>

Text string that specifies the name of the counter path to add to the query. The contents of this string must be a valid counter path, as obtained from the counter browser or other source.

</dd> <dt>

*CounterHandle* 
</dt> <dd>

Unique reference that identifies this counter in the query. This variable must be initialized to zero before the function is called. It contains a valid value on return only if the function completes successfully.

</dd> </dl>

## Return value

If the function succeeds, it returns a **Long** integer equal to ERROR\_SUCCESS and a new handle in the *CounterHandle* variable.

If the function fails, the return value is a [system error code](/windows/desktop/Debug/system-error-codes) or a [PDH error code](pdh-error-codes.md). The following are possible values.



| Return code                                                                                                     | Description                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**PDH\_INVALID\_ARGUMENT**</dt> </dl>           | One or more of the arguments is invalid or incorrect.<br/>              |
| <dl> <dt>**PDH\_MEMORY\_ALLOCATION\_FAILURE**</dt> </dl> | A memory buffer could not be allocated.<br/>                            |
| <dl> <dt>**PDH\_INVALID\_HANDLE**</dt> </dl>             | The query handle is not valid.<br/>                                     |
| <dl> <dt>**PDH\_CSTATUS\_NO\_COUNTER**</dt> </dl>        | The specified counter was not found.<br/>                               |
| <dl> <dt>**PDH\_CSTATUS\_NO\_OBJECT**</dt> </dl>         | The specified object could not be found.<br/>                           |
| <dl> <dt>**PDH\_CSTATUS\_NO\_MACHINE**</dt> </dl>        | A computer entry could not be created.<br/>                             |
| <dl> <dt>**PDH\_CSTATUS\_BAD\_COUNTERNAME**</dt> </dl>   | An empty counter name path string was passed in.<br/>                   |
| <dl> <dt>**PDH\_FUNCTION\_NOT\_FOUND**</dt> </dl>        | The calculation function for this counter could not be determined.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhVbOpenQuery**](pdhvbopenquery.md)
</dt> </dl>

 

