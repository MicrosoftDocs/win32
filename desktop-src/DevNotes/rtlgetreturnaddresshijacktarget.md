---
description: Gets the address of the function that's used for the OS-supported return address hijacking.
title: RtlGetReturnAddressHijackTarget
ms.topic: reference
ms.date: 10/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetReturnAddressHijackTarget
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlGetReturnAddressHijackTarget function

Gets the address of the function that's used for the OS-supported return address hijacking. When user-mode wants to perform such a hijack, it overwrites a return address on the stack with said address.

## Syntax


```C++
ULONG_PTR
RtlGetReturnAddressHijackTarget (
    VOID
)
```

## Parameters

None.

## Return value

The address that's used to perform an OS-supported return address hijack.

## Remarks 

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------|
| Minimum supported client | Windows 10 Build 19041 |
| DLL                   | Ntdll.dll                                          |



## See also


 

 
