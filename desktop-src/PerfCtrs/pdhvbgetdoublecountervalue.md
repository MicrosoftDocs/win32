---
description: The PdhVbGetDoubleCounterValue function returns the current value of the specified counter as a double-precision floating point value.
ms.assetid: a2ee63dd-da39-4104-921d-371172bcb45c
title: PdhVbGetDoubleCounterValue function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbGetDoubleCounterValue
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbGetDoubleCounterValue function

The **PdhVbGetDoubleCounterValue** function returns the current value of the specified counter as a double-precision floating point value. You should check *CounterStatus* before using the returned number, because the counter may not be valid when it is read. To check the counter status, call the [**PdhVbIsGoodStatus**](pdhvbisgoodstatus.md) function.

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbGetDoubleCounterValue( \_ ByVal CounterHandle As Long, \_ ByRef CounterStatus As Long \_ ) As Double

## Parameters

<dl> <dt>

*CounterHandle* 
</dt> <dd>

ID of the counter whose current value is to be read.

</dd> <dt>

*CounterStatus* 
</dt> <dd>

Variable in which the current status of the counter value is returned to the caller. The returned data value is valid if and only if the value returned in CounterStatus is PDH\_CSTATUS\_VALID\_DATA or PDH\_CSTATUS\_NEW\_DATA (see PDH error codes). If the value returned in CounterStatus is any other value, do not use the data.

</dd> </dl>

## Return value

The function returns the double-precision floating point value of the current counter, computed and formatted as defined by the counter type.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhVbIsGoodStatus**](pdhvbisgoodstatus.md)
</dt> </dl>

 

 




