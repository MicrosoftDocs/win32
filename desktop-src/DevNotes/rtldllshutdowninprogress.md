---
description: Gets a value indicating whether a shutdown of the current dll process is in progress.
title: RtlDllShutdownInProgress function
ms.topic: reference
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetVersion
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlDllShutdownInProgress function

Gets a value indicating whether a shutdown of the current dll process is in progress.

## Syntax


```C++
BOOLEAN
RtlDllShutdownInProgress (
    VOID
);
```



## Parameters

None.

## Return value

TRUE if a shutdown of the current dll process is in progress; otherwise, FALSE.

## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from ntdll.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 11 |
| Minimum supported server | Windows 11 |
| DLL | Ntdll.dll |



## See also



 

 
