---
description: The PdhVbGetCounterPathElements function parses a fully qualified performance counter path string into its individual elements.
ms.assetid: 5459c7dd-e8b6-48cd-a33f-cafdc64dd9ee
title: PdhVbGetCounterPathElements function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbGetCounterPathElements
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbGetCounterPathElements function

The **PdhVbGetCounterPathElements** function parses a fully qualified performance counter path string into its individual elements. Each of the string variables must be the same size (*BufferSize*) and dimensioned and initialized before it is used in this function.

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbGetCounterPathElements( \_ ByVal PathString As String, \_ ByVal MachineName As String, \_ ByVal ObjectName As String, \_ ByVal InstanceName As String, \_ ByVal ParentInstance As String, \_ ByVal CounterName As String, \_ ByVal BufferSize As Long \_ ) As Long

## Parameters

<dl> <dt>

*PathString* 
</dt> <dd>

Counter path string that is to be broken up into its individual elements.

</dd> <dt>

*MachineName* 
</dt> <dd>

String to receive the computer name.

</dd> <dt>

*ObjectName* 
</dt> <dd>

String to receive the object name.

</dd> <dt>

*InstanceName* 
</dt> <dd>

String to receive the instance name, if used.

</dd> <dt>

*ParentInstance* 
</dt> <dd>

String to receive the parent instance, if used.

</dd> <dt>

*CounterName* 
</dt> <dd>

String to receive the counter name.

</dd> <dt>

*BufferSize* 
</dt> <dd>

Maximum size of each string variable used as a parameter to this function call.

</dd> </dl>

## Return value

If the function succeeds, it returns a **Long** integer equal to ERROR\_SUCCESS.

If the function fails, the return value is a [system error code](/windows/desktop/Debug/system-error-codes) or a [PDH error code](pdh-error-codes.md). The following are possible values.



| Return code                                                                                                     | Description                                                                                    |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <dl> <dt>**PDH\_INVALID\_ARGUMENT**</dt> </dl>           | One or more of the string buffers is not the correct size.<br/>                          |
| <dl> <dt>**PDH\_MORE\_DATA**</dt> </dl>                  | One or more of the counter path elements is too large for the return buffer length.<br/> |
| <dl> <dt>**PDH\_MEMORY\_ALLOCATION\_FAILURE**</dt> </dl> | A temporary memory buffer could not be allocated.<br/>                                   |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhVbCreateCounterPathList**](pdhvbcreatecounterpathlist.md)
</dt> <dt>

[**PdhVbGetCounterPathFromList**](pdhvbgetcounterpathfromlist.md)
</dt> <dt>

[**PdhVbGetOneCounterPath**](pdhvbgetonecounterpath.md)
</dt> </dl>

 

