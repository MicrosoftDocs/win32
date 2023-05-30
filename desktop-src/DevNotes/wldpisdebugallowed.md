---
description: Gets a value indicating if debugging a specific process is allowed.
title: WldpIsDebugAllowed function
ms.topic: reference
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WldpIsDebugAllowed
api_type: 
- DllExport
api_location: 
- wldp.dll
---

# WldpIsDebugAllowed function

Gets a value indicating if debugging a specific process is allowed.

## Syntax


```C++
STDAPI WldpIsDebugAllowed(
    _In_ HANDLE processHandle,
    _Out_ PBOOL isDebugAllowed
    );
```



## Parameters

### processHandle [in]

A handle to the process for which debugging capability is queried.

## Return value

TRUE if debugging is allowed for the specified process; otherwise, FALSE.

## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from wldp.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows 10 |
| DLL | wldp.dll |



## See also



 

 
