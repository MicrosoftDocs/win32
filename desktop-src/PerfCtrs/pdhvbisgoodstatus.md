---
description: The PdhVbIsGoodStatus function tests a status value to determine if it is a success or failure code. If the status value is a successful one, then the return value will be nonzero. If it is a failure status code, the return value will be zero.
ms.assetid: bdca8f64-5dcd-4ecb-ba95-72f7a56c0439
title: PdhVbIsGoodStatus function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbIsGoodStatus
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbIsGoodStatus function

The **PdhVbIsGoodStatus** function tests a status value to determine if it is a success or failure code. If the status value is a successful one, then the return value will be nonzero. If it is a failure status code, the return value will be zero.

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbIsGoodStatus( \_ ByVal StatusValue As Long \_ ) As Long

## Parameters

<dl> <dt>

*StatusValue* 
</dt> <dd>

Status value returned by another PDH function that is to be tested.

</dd> </dl>

## Return value

The function returns zero if the status code is a failure status code. It returns nonzero if the status code is a success status code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhVbGetDoubleCounterValue**](pdhvbgetdoublecountervalue.md)
</dt> </dl>

 

 




