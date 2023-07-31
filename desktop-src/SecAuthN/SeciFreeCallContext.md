---
description: Frees the memory allocated by SeciAllocateAndSetIPAddress.
ms.assetid: b69a6666-df4b-42fe-98f9-1371df8e4cdb
title: SeciFreeCallContext function
ms.topic: reference
ms.date: 07/31/2023
topic_type: 
- APIRef
api_name: 
- SeciFreeCallContext
api_type: 
- UserDefined
api_location: 
---

# SeciFreeCallContext function

The **SeciFreeCallContext** function frees the memory allocated by [SeciAllocateAndSetIPAddress](SeciAllocateAndSetIPAddress.md).

## Syntax

```C++
VOID SEC_ENTRY SeciFreeCallContext();
```

## Remarks

This function is not present in the SDK headers. To use it, call the [LoadLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) function to obtain a handle to SSPICLI.DLL and then use [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) to obtain the function address.

Call this function if [SeciAllocateAndSetIPAddress](SeciAllocateAndSetIPAddress.md) sets *FreeCallContext* to `TRUE`.

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Windows Vista \[desktop apps \| UWP apps\] |
| Minimum supported server | Windows Server 2008 \[desktop apps \| UWP apps\] |
| Target platform | Windows |
| Header | None |
| Library | None |
| DLL | SSPICLI.DLL |

## See also

[SeciAllocateAndSetIPAddress](SeciAllocateAndSetIPAddress.md)
